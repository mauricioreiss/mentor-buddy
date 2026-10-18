"""Checks every http(s) link in the skill's Markdown files and prints a Markdown report.

Exit code 1 when at least one link is broken, so CI can react. Standard library only.
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

SKILL_ROOT = Path(__file__).resolve().parent.parent
URL_PATTERN = re.compile(r"https?://[^\s)<>|\]\"'`]+")
USER_AGENT = "Mozilla/5.0 (compatible; mentor-buddy-link-check/1.0; +https://github.com/mauricioreiss/mentor-buddy)"
TIMEOUT_SECONDS = 20
# Sites that refuse automated requests answer with these; a person has to open the link.
BLOCKED_STATUSES = {401, 403, 429}


@dataclass(frozen=True)
class LinkResult:
    url: str
    status: int | None
    final_url: str
    error: str = ""

    @property
    def is_broken(self) -> bool:
        return self.status is None or (self.status >= 400 and self.status not in BLOCKED_STATUSES)

    @property
    def is_blocked(self) -> bool:
        return self.status in BLOCKED_STATUSES

    @property
    def has_moved(self) -> bool:
        before, after = urlsplit(self.url), urlsplit(self.final_url)
        if before.netloc.lower() != after.netloc.lower():
            return True
        # A redirect deeper into the same path is the site's landing page (often the latest version), not a move.
        return not after.path.rstrip("/").startswith(before.path.rstrip("/"))


def find_links() -> dict[str, set[str]]:
    """Maps each URL to the files that mention it, skipping dot folders such as .git."""
    links: dict[str, set[str]] = {}
    for markdown_file in SKILL_ROOT.rglob("*.md"):
        relative = markdown_file.relative_to(SKILL_ROOT)
        if any(part.startswith(".") for part in relative.parts):
            continue
        for url in URL_PATTERN.findall(markdown_file.read_text(encoding="utf-8")):
            links.setdefault(url.rstrip(".,;:"), set()).add(relative.as_posix())
    return links


def request(url: str, method: str) -> LinkResult:
    http_request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(http_request, timeout=TIMEOUT_SECONDS) as response:
            return LinkResult(url, response.status, response.geturl())
    except urllib.error.HTTPError as error:
        return LinkResult(url, error.code, error.geturl() or url)
    except (urllib.error.URLError, TimeoutError, ConnectionError) as error:
        return LinkResult(url, None, url, str(getattr(error, "reason", error)))


def check(url: str) -> LinkResult:
    # Many servers mishandle HEAD, so anything but a clean answer gets a second try with GET.
    result = request(url, "HEAD")
    if result.status is None or result.status >= 400:
        result = request(url, "GET")
    return result


def format_section(title: str, results: list[LinkResult], links: dict[str, set[str]], describe) -> list[str]:
    if not results:
        return []
    lines = [f"## {title} ({len(results)})", ""]
    for result in sorted(results, key=lambda item: item.url):
        lines.append(f"- {result.url} - {describe(result)} - in {', '.join(sorted(links[result.url]))}")
    return lines + [""]


def build_report(results: list[LinkResult], links: dict[str, set[str]]) -> str:
    broken = [result for result in results if result.is_broken]
    blocked = [result for result in results if result.is_blocked]
    moved = [result for result in results if not result.is_broken and not result.is_blocked and result.has_moved]
    files = {file for mentioned_in in links.values() for file in mentioned_in}
    lines = [f"# Doc link check - {date.today().isoformat()}", "",
             f"Checked {len(results)} links in {len(files)} files: "
             f"{len(broken)} broken, {len(moved)} moved, {len(blocked)} blocked.", ""]
    lines += format_section("Broken", broken, links, lambda item: f"status {item.status}" if item.status else item.error)
    lines += format_section("Moved", moved, links, lambda item: f"now {item.final_url}")
    lines += format_section("Blocked (open by hand)", blocked, links, lambda item: f"status {item.status}")
    return "\n".join(lines)


def main() -> int:
    links = find_links()
    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(check, sorted(links)))
    sys.stdout.write(build_report(results, links) + "\n")
    return 1 if any(result.is_broken for result in results) else 0


if __name__ == "__main__":
    sys.exit(main())
