"""Builds the learner's completion certificate as a one-page A4 landscape .docx.

Reads the certificate data from a UTF-8 JSON file (--data) and writes the file
given with --out. Standard library only, so it runs wherever Python 3.9+ does.
Fields:

  language              "pt" or "en"
  name                  learner's name as they typed it ("" leaves the line blank)
  project               project name
  problem               one-line problem from the brief
  programming_language  for example "C#"
  stack_detail          framework and version, for example "ASP.NET Core minimal APIs, .NET 10"
  level                 for example "Junior" / "Júnior"
  first_session         YYYY-MM-DD, the oldest date in the session log
  issued_on             YYYY-MM-DD, today
  sessions              number of sessions in the session log
  built                 1 to 6 short lines: what the learner built
  live_url              optional: the live address or published artifact
  stops                 optional: phase names, only for the cybersecurity track

Example:
  python scripts/make_certificate.py --data certificate-data.json --out certificado-league-table-api-2026-10-18.docx

A file and not stdin: on Windows, PowerShell 5.1 pipes text to programs as
ASCII, which would strip every accent from the learner's name.
"""
from __future__ import annotations

import argparse
import json
import struct
import sys
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape

SKILL_ROOT = Path(__file__).resolve().parent.parent

INK = "1D2740"
MUTED = "4E586B"
SOFT = "8A8F99"
ACCENT = "B12F25"
LINK = "1F5FBF"
SERIF = "Georgia"
SANS = "Calibri"

# Twips (1/1440 inch) for layout, EMU (1/914400 inch) for the image.
PAGE_WIDTH, PAGE_HEIGHT, PAGE_MARGIN = 16838, 11906, 720
# Both tables share one width and one cell gap, so their edges line up.
CONTENT_WIDTH = 12400
CELL_GAP = 50
HIGHLIGHT_WIDTH = CONTENT_WIDTH // 4
BUILT_WIDTH = 7200
TRAIL_WIDTH = CONTENT_WIDTH - BUILT_WIDTH
EMU_PER_TWIP = 635

LABELS = {
    "pt": {
        "title": "Certificado de conclusão", "certify": "Certificamos que",
        "completed": "concluiu, da pasta vazia ao deploy, o projeto",
        "language": "LINGUAGEM", "level": "NÍVEL", "duration": "DURAÇÃO", "sessions": "SESSÕES",
        "sessions_detail": "de mentoria", "built": "O QUE FOI CONSTRUÍDO", "live": "NO AR EM",
        "trail": "TRILHA COMPLETA", "trail_count": "{done} de {done} paradas",
        "one_day": "1 dia", "days": "{n} dias", "period": "{start} a {end}", "issued": "Emitido em {date}",
        "months": ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
                   "setembro", "outubro", "novembro", "dezembro"],
        "long_date": "{day} de {month} de {year}", "short_date": "{day:02d}/{month:02d}/{year}",
        "footer": "Certificado de conclusão de projeto emitido pela skill Mentor Buddy "
                  "(github.com/mauricioreiss/mentor-buddy). Não é uma certificação oficial.",
        "stops": ["Entrevista", "Projeto", "Ambiente", "Pastas", "Esqueleto", "Features", "Banco",
                  "Qualidade", "Docker", "CI", "Deploy", "Retro"],
    },
    "en": {
        "title": "Certificate of completion", "certify": "This certifies that",
        "completed": "completed, from an empty folder to deploy, the project",
        "language": "LANGUAGE", "level": "LEVEL", "duration": "DURATION", "sessions": "SESSIONS",
        "sessions_detail": "of mentoring", "built": "WHAT WAS BUILT", "live": "LIVE AT",
        "trail": "FULL TRAIL", "trail_count": "{done} of {done} stops",
        "one_day": "1 day", "days": "{n} days", "period": "{start} to {end}", "issued": "Issued on {date}",
        "months": ["January", "February", "March", "April", "May", "June", "July", "August",
                   "September", "October", "November", "December"],
        "long_date": "{month} {day}, {year}", "short_date": "{year}-{month:02d}-{day:02d}",
        "footer": "Project-completion certificate issued by the Mentor Buddy skill "
                  "(github.com/mauricioreiss/mentor-buddy). It is not an official certification.",
        "stops": ["Interview", "Project", "Environment", "Folders", "Skeleton", "Features", "Database",
                  "Quality", "Docker", "CI", "Deploy", "Retro"],
    },
}


class CertificateError(ValueError):
    """Invalid certificate data; the message says which field and why."""


@dataclass(frozen=True)
class Certificate:
    language: str
    name: str
    project: str
    problem: str
    programming_language: str
    stack_detail: str
    level: str
    first_session: date
    issued_on: date
    sessions: int
    built: list[str]
    live_url: str
    stops: list[str]


def text_field(data: dict, key: str, max_length: int, required: bool = True) -> str:
    value = data.get(key, "")
    if not isinstance(value, str):
        raise CertificateError(f"{key} must be text")
    value = value.strip()
    if required and not value:
        raise CertificateError(f"{key} is required")
    if len(value) > max_length:
        raise CertificateError(f"{key} is longer than {max_length} characters")
    return value


def date_field(data: dict, key: str) -> date:
    try:
        return date.fromisoformat(text_field(data, key, 10))
    except ValueError as error:
        raise CertificateError(f"{key} must be a date as YYYY-MM-DD") from error


def list_field(data: dict, key: str, max_items: int, max_length: int, required: bool = True) -> list[str]:
    items = data.get(key, [])
    if not isinstance(items, list) or not all(isinstance(item, str) and item.strip() for item in items):
        raise CertificateError(f"{key} must be a list of non-empty texts")
    if (required and not items) or len(items) > max_items:
        raise CertificateError(f"{key} needs 1 to {max_items} items")
    if any(len(item) > max_length for item in items):
        raise CertificateError(f"each item of {key} must fit in {max_length} characters")
    return [item.strip() for item in items]


def parse_certificate(data: dict) -> Certificate:
    language = data.get("language")
    if language not in LABELS:
        raise CertificateError('language must be "pt" or "en"')
    sessions = data.get("sessions")
    if not isinstance(sessions, int) or not 1 <= sessions <= 1000:
        raise CertificateError("sessions must be a whole number from 1 to 1000")
    certificate = Certificate(
        language=language,
        name=text_field(data, "name", 80, required=False),
        project=text_field(data, "project", 60),
        problem=text_field(data, "problem", 160),
        programming_language=text_field(data, "programming_language", 30),
        stack_detail=text_field(data, "stack_detail", 80, required=False),
        level=text_field(data, "level", 20),
        first_session=date_field(data, "first_session"),
        issued_on=date_field(data, "issued_on"),
        sessions=sessions,
        built=list_field(data, "built", 6, 90),
        live_url=text_field(data, "live_url", 200, required=False),
        stops=list_field(data, "stops", 16, 30, required=False) or LABELS[language]["stops"],
    )
    if certificate.issued_on < certificate.first_session:
        raise CertificateError("issued_on is before first_session")
    if certificate.live_url and not certificate.live_url.startswith(("https://", "http://")):
        raise CertificateError("live_url must start with https:// or http://")
    return certificate


def long_date(value: date, labels: dict) -> str:
    return labels["long_date"].format(day=value.day, month=labels["months"][value.month - 1], year=value.year)


def short_date(value: date, labels: dict) -> str:
    return labels["short_date"].format(day=value.day, month=value.month, year=value.year)


def duration_text(certificate: Certificate, labels: dict) -> str:
    # Both ends count: a project started and finished on the same day took one day.
    days = (certificate.issued_on - certificate.first_session).days + 1
    return labels["one_day"] if days == 1 else labels["days"].format(n=days)


# --- WordprocessingML building blocks -------------------------------------

def run(text: str, size: int, color: str = MUTED, bold: bool = False, italic: bool = False,
        font: str = SANS, spacing: int = 0) -> str:
    properties = (
        f'<w:rFonts w:ascii="{font}" w:hAnsi="{font}" w:cs="{font}"/>'
        + ("<w:b/><w:bCs/>" if bold else "") + ("<w:i/><w:iCs/>" if italic else "")
        + f'<w:color w:val="{color}"/>' + (f'<w:spacing w:val="{spacing}"/>' if spacing else "")
        + f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    )
    return f'<w:r><w:rPr>{properties}</w:rPr><w:t xml:space="preserve">{escape(text)}</w:t></w:r>'


def paragraph(content: str, align: str = "center", before: int = 0, after: int = 0,
              indent: str = "", border_top: bool = False) -> str:
    border = '<w:pBdr><w:top w:val="single" w:sz="6" w:space="4" w:color="8A8F99"/></w:pBdr>' if border_top else ""
    return (f'<w:p><w:pPr>{border}<w:spacing w:before="{before}" w:after="{after}"/>{indent}'
            f'<w:jc w:val="{align}"/></w:pPr>{content}</w:p>')


def label(text: str, align: str = "center", before: int = 0) -> str:
    return paragraph(run(text, 15, SOFT, bold=True, spacing=20), align, before=before, after=40)


def cell(content: str, width: int, accent_top: bool = False) -> str:
    top = f'<w:top w:val="single" w:sz="18" w:space="0" w:color="{ACCENT}"/>' if accent_top else '<w:top w:val="nil"/>'
    borders = f'<w:tcBorders>{top}<w:left w:val="nil"/><w:bottom w:val="nil"/><w:right w:val="nil"/></w:tcBorders>'
    margins = '<w:tcMar><w:top w:w="100" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/></w:tcMar>'
    return f'<w:tc><w:tcPr><w:tcW w:w="{width}" w:type="dxa"/>{borders}{margins}</w:tcPr>{content}</w:tc>'


def table(cells: list[str], widths: list[int], spacing: int = 0) -> str:
    gap = f'<w:tblCellSpacing w:w="{spacing}" w:type="dxa"/>' if spacing else ""
    borders = "".join(f'<w:{side} w:val="nil"/>' for side in ("top", "left", "bottom", "right", "insideH", "insideV"))
    grid = "".join(f'<w:gridCol w:w="{width}"/>' for width in widths)
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(widths)}" w:type="dxa"/><w:jc w:val="center"/>{gap}'
            f'<w:tblBorders>{borders}</w:tblBorders><w:tblLayout w:type="fixed"/></w:tblPr>'
            f'<w:tblGrid>{grid}</w:tblGrid><w:tr>{"".join(cells)}</w:tr></w:tbl>')


# --- Page sections ----------------------------------------------------------

def image_extent(png: bytes) -> tuple[int, int]:
    """The header spans the content width; its height follows the PNG's own proportions."""
    pixel_width, pixel_height = struct.unpack(">II", png[16:24])
    width = CONTENT_WIDTH * EMU_PER_TWIP
    return width, width * pixel_height // pixel_width


def header_image(title: str, extent: tuple[int, int]) -> str:
    cx, cy = extent
    drawing = (
        f'<wp:inline distT="0" distB="0" distL="0" distR="0"><wp:extent cx="{cx}" cy="{cy}"/>'
        f'<wp:docPr id="1" name="Header" descr="{escape(title)}"/>'
        '<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect="1"/></wp:cNvGraphicFramePr>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture"><pic:pic>'
        '<pic:nvPicPr><pic:cNvPr id="1" name="certificate-header.png"/><pic:cNvPicPr/></pic:nvPicPr>'
        '<pic:blipFill><a:blip r:embed="rIdHeaderImage"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic></wp:inline>'
    )
    return paragraph(f"<w:r><w:drawing>{drawing}</w:drawing></w:r>", after=120)


def name_block(certificate: Certificate, labels: dict) -> str:
    # A blank name keeps its line, so the learner can type it in Word.
    return "".join([
        paragraph(run(labels["certify"], 21), after=20),
        paragraph(run(certificate.name or " ", 60, INK, bold=True, font=SERIF), after=40),
        paragraph(run(labels["completed"], 21), after=20),
        paragraph(run(certificate.project, 36, INK, bold=True, font=SERIF), after=10),
        paragraph(run(certificate.problem, 19, MUTED, italic=True), after=200),
    ])


def highlight(title: str, value: str, detail: str) -> str:
    return cell(label(title) + paragraph(run(value, 32, INK, bold=True), after=20)
                + paragraph(run(detail or " ", 16, SOFT), after=40), HIGHLIGHT_WIDTH, accent_top=True)


def highlights(certificate: Certificate, labels: dict) -> str:
    period = labels["period"].format(start=short_date(certificate.first_session, labels),
                                     end=short_date(certificate.issued_on, labels))
    return table([
        highlight(labels["language"], certificate.programming_language, certificate.stack_detail),
        highlight(labels["level"], certificate.level, ""),
        highlight(labels["duration"], duration_text(certificate, labels), period),
        highlight(labels["sessions"], str(certificate.sessions), labels["sessions_detail"]),
    ], [HIGHLIGHT_WIDTH] * 4, spacing=CELL_GAP)


def built_cell(certificate: Certificate, labels: dict) -> str:
    bullet_indent = '<w:ind w:left="284" w:hanging="284"/>'
    items = "".join(paragraph(run(f"•\t{item}", 19, INK), align="left", after=40, indent=bullet_indent)
                    for item in certificate.built)
    return cell(label(labels["built"], align="left") + items, BUILT_WIDTH)


def trail_cell(certificate: Certificate, labels: dict) -> str:
    live = ""
    if certificate.live_url:
        link = (f'<w:hyperlink r:id="rIdLiveUrl" w:history="1"><w:r><w:rPr><w:color w:val="{LINK}"/>'
                f'<w:u w:val="single"/><w:sz w:val="19"/><w:szCs w:val="19"/></w:rPr>'
                f'<w:t xml:space="preserve">{escape(certificate.live_url)}</w:t></w:r></w:hyperlink>')
        live = label(labels["live"], align="left") + paragraph(link, align="left", after=120)
    done = len(certificate.stops)
    trail = (label(labels["trail"], align="left")
             + paragraph(run(labels["trail_count"].format(done=done), 19, INK, bold=True), align="left", after=20)
             + paragraph(run(" · ".join(certificate.stops), 15, SOFT), align="left"))
    return cell(live + trail, TRAIL_WIDTH)


def signature(certificate: Certificate, labels: dict) -> str:
    narrow = '<w:ind w:left="5600" w:right="5600"/>'
    return "".join([
        paragraph(run("Mentor Buddy", 22, INK, bold=True), before=280, indent=narrow, border_top=True),
        paragraph(run(labels["issued"].format(date=long_date(certificate.issued_on, labels)), 17, SOFT)),
    ])


NAMESPACES = (
    'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
    'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
    'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
    'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
    'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture"'
)
XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'


def document_xml(certificate: Certificate, image_size: tuple[int, int]) -> str:
    labels = LABELS[certificate.language]
    section = (f'<w:sectPr><w:footerReference w:type="default" r:id="rIdFooter"/>'
               f'<w:pgSz w:w="{PAGE_WIDTH}" w:h="{PAGE_HEIGHT}" w:orient="landscape"/>'
               f'<w:pgMar w:top="{PAGE_MARGIN}" w:right="{PAGE_MARGIN}" w:bottom="{PAGE_MARGIN}" w:left="{PAGE_MARGIN}" '
               'w:header="360" w:footer="360" w:gutter="0"/></w:sectPr>')
    body = "".join([
        header_image(labels["title"], image_size),
        name_block(certificate, labels),
        highlights(certificate, labels),
        paragraph("", after=160),
        table([built_cell(certificate, labels), trail_cell(certificate, labels)], [BUILT_WIDTH, TRAIL_WIDTH], spacing=CELL_GAP),
        signature(certificate, labels),
    ])
    return f"{XML_DECLARATION}<w:document {NAMESPACES}><w:body>{body}{section}</w:body></w:document>"


def footer_xml(labels: dict) -> str:
    return (f'{XML_DECLARATION}<w:ftr {NAMESPACES}>'
            + paragraph(run(labels["footer"], 15, SOFT)) + "</w:ftr>")


def styles_xml(language: str) -> str:
    locale = "pt-BR" if language == "pt" else "en-US"
    return (f'{XML_DECLARATION}<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            f'<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="{SANS}" w:hAnsi="{SANS}" w:cs="{SANS}"/>'
            f'<w:sz w:val="20"/><w:szCs w:val="20"/><w:lang w:val="{locale}"/></w:rPr></w:rPrDefault>'
            '<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault>'
            '</w:docDefaults><w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/>'
            '<w:qFormat/></w:style></w:styles>')


def package_parts(certificate: Certificate, header_png: bytes) -> dict[str, bytes | str]:
    labels = LABELS[certificate.language]
    relationship = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
    link = (f'<Relationship Id="rIdLiveUrl" Type="{relationship}/hyperlink" Target="{escape(certificate.live_url, {chr(34): "&quot;"})}" '
            'TargetMode="External"/>') if certificate.live_url else ""
    return {
        "[Content_Types].xml": (
            f'{XML_DECLARATION}<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/><Default Extension="png" ContentType="image/png"/>'
            '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
            '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
            '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>'
            '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
            '</Types>'),
        "_rels/.rels": (
            f'{XML_DECLARATION}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rId1" Type="{relationship}/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
            'Target="docProps/core.xml"/></Relationships>'),
        "docProps/core.xml": (
            f'{XML_DECLARATION}<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f'<dc:title>{escape(labels["title"])}</dc:title><dc:creator>Mentor Buddy</dc:creator></cp:coreProperties>'),
        "word/_rels/document.xml.rels": (
            f'{XML_DECLARATION}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rIdStyles" Type="{relationship}/styles" Target="styles.xml"/>'
            f'<Relationship Id="rIdFooter" Type="{relationship}/footer" Target="footer1.xml"/>'
            f'<Relationship Id="rIdHeaderImage" Type="{relationship}/image" Target="media/certificate-header.png"/>'
            f'{link}</Relationships>'),
        "word/document.xml": document_xml(certificate, image_extent(header_png)),
        "word/styles.xml": styles_xml(certificate.language),
        "word/footer1.xml": footer_xml(labels),
        "word/media/certificate-header.png": header_png,
    }


def write_docx(path: Path, parts: dict[str, bytes | str]) -> None:
    # A fixed timestamp keeps two builds of the same certificate byte-identical.
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in parts.items():
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, content.encode("utf-8") if isinstance(content, str) else content)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Mentor Buddy completion certificate (.docx).")
    parser.add_argument("--data", required=True, help="UTF-8 JSON file with the certificate data")
    parser.add_argument("--out", required=True, help="path of the .docx to write")
    args = parser.parse_args()
    try:
        certificate = parse_certificate(json.loads(Path(args.data).read_text(encoding="utf-8-sig")))
    except json.JSONDecodeError as error:
        print(f"certificate data is not valid JSON: {error}", file=sys.stderr)
        return 2
    except CertificateError as error:
        print(f"certificate data: {error}", file=sys.stderr)
        return 2
    header_png = (SKILL_ROOT / "assets" / f"certificate-header-{certificate.language}.png").read_bytes()
    output = Path(args.out)
    write_docx(output, package_parts(certificate, header_png))
    print(f"certificate written to {output.resolve()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
