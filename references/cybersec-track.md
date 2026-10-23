# Cybersecurity track

An alternative journey for a learner who wants hands-on offensive security the way a lab teaches it: set up the environment, understand a vulnerability class to its root, exploit it with real tools, then build their own tool so they understand the mechanism and not just the button. The same deal holds as in the rest of the skill: the learner is the driver. They run every tool and write every line; you are the navigator who explains, reviews and keeps the map. Crypto, recon and exploitation are learned by doing, in a lab the learner controls.

When the learner picks this track in the interview, the phase plan in STUDY-MEMORY.md comes from here instead of [phases.md](phases.md). The step loop, the miss ladder, the review training and the doc check all work exactly as in the main skill. Perishable facts (tool versions, flags, install steps) are looked up live in [docs-cybersec.md](docs-cybersec.md).

## The lab contract (hard gate: CS1 does not pass without it)

This track teaches attacking so the learner can defend and can pass authorized work. It never teaches attacking systems that are not theirs. Before any tool runs, the learner sets up an isolated lab and states the rule back in their own words. Record it in `Decisions` and do not move past CS1 until it holds.

| Rule | What it means in the lab |
|---|---|
| **Isolated network** | Attacker and target VMs on a host-only or internal network with no bridge to the home network or the internet during exercises. Snapshots before each session so a broken target rolls back. |
| **Targets you own or sanctioned ranges only** | The vulnerable VM/app the learner installed, or a range built for this: PortSwigger Web Security Academy, OWASP Juice Shop, DVWA, HTB, TryHackMe, VulnHub, picoCTF. Never a real site, app, network or account that is not the learner's and not a sanctioned range. |
| **Authorization is the line** | Outside the lab, the same techniques need written permission from the owner (a pentest contract, a bug-bounty scope). No permission, no test. This is law, not etiquette. |
| **No real-world harm tooling** | The track does not build persistence, evasion, or anything aimed at a live third-party target. Tools stay pointed at the lab. |

If the learner asks to point a tool at something outside this, stop and restate the contract in one line; do not help with the target. This is the one place the mentor refuses rather than guides.

## Choosing a focus

In the interview, after the lab is agreed, pick one focus for the project (they can do another track later). Offer the ones that fit their level and language:

| Focus | What they build | Core tools | Level |
|---|---|---|---|
| **Web app security** | Find and exploit OWASP Top 10 bugs in a vulnerable app, then write a scanner of their own | Burp Suite (Community), the app's own forms, Python `requests` | junior to senior |
| **Network** | Map and sniff an isolated network, then write a port scanner and a packet parser | nmap, Wireshark, Python `scapy` | mid to senior |
| **Binary / pwn (CTF)** | Understand memory, solve CTF-style binary challenges, write exploit scripts | a debugger, Python `pwntools`, picoCTF/HTB challenges | senior |
| **Cryptography** | Understand symmetric, asymmetric and hashing; implement each, break deliberately weak uses, send something securely | the stack's crypto library (see docs-cybersec) | mid to senior |

The learner writes the tools; standard tools (Burp, nmap, sqlmap, Metasploit) are used to see the attack work first, then the learner reimplements the core in their language so the mechanism is understood, not memorised.

## The journey

| # | Phase | Done when |
|---|---|---|
| CS0 | Interview and focus | Level, language and one focus agreed; lab contract understood |
| CS1 | Lab setup | Isolated lab running (hypervisor, attacker and target VMs, snapshot); the learner states the contract back |
| CS2 | Foundations | The theory of the focus explained back (how the vuln class or primitive works), with the official reference read |
| CS3 | Recon | The target mapped by hand for this focus (endpoints, ports, inputs, binary layout) and written up |
| CS4 | Exploit with a tool | One vulnerability exploited in the lab with a standard tool; the learner explains each step and what the tool did under it |
| CS5 | Build your own tool | The learner reimplements the core of that attack in their language, with tests where it makes sense; you review it like production code |
| CS6 | Crypto module | Symmetric, asymmetric and hashing understood and used correctly; one deliberately weak use broken to see why it fails; something sent or stored securely |
| CS7 | Writeup | A short report of one finding: what, impact, steps to reproduce, the fix, the official reference. Reviewed like code; delivered as the `.docx` ([final-report.md](final-report.md)); once it passes, the completion certificate ([certificate.md](certificate.md)) |

Focus shapes which phases weigh most: web and network spend CS3 to CS5 on their tool; the crypto focus makes CS6 the main body; a binary focus turns CS3 to CS5 into debugging and the exploit script. CS6 is always present at least as the module that teaches how to protect data, because an attacker who does not understand crypto misreads half of what they find.

## Per-focus outlines

Each outline is a list of steps; expand them in the memory and run the step loop on each. Everything perishable (versions, commands, flags) is verified live in [docs-cybersec.md](docs-cybersec.md).

**Web app security**
1. Install the vulnerable target in the lab (Juice Shop or DVWA); snapshot.
2. Proxy traffic through Burp; read how a request becomes a response.
3. One class at a time, from the OWASP Top 10: injection, broken access control, XSS. For each: the theory (WSTG + cheat sheet), find it in the target by hand, exploit it in Burp, then explain the root cause and the fix.
4. CS5: write a small scanner in their language (`requests`) that probes one class automatically, with a test against the lab target. Review it; discuss false positives and why a real scanner is hard.

**Network**
1. Build the isolated network with two or three VMs; snapshot.
2. Map it with nmap; read what each scan type sends and why.
3. Capture traffic in Wireshark; follow one TCP stream by hand.
4. CS5: write a port scanner and a packet parser with `scapy`; compare results to nmap and explain the gaps.

**Binary / pwn**
1. Set up the challenge environment (a CTF VM or picoCTF); snapshot.
2. Memory and the stack: how a function call is laid out; read the binary in a debugger.
3. One classic primitive (buffer overflow on a training binary) understood and reached by hand.
4. CS5: write the exploit as a `pwntools` script, with the offsets found, explained line by line.

**Cryptography**
1. Hashing: what it is for, why not for secrecy; implement a salted hash correctly, see why an unsalted one leaks.
2. Symmetric: encrypt and decrypt with an authenticated mode; break a hand-rolled ECB example to see the pattern leak.
3. Asymmetric: key pairs, signatures; send an encrypted, signed message to a second identity.
4. Pull it together: protect data at rest and in transit in a small app, each choice justified against the official guidance.

## How review training applies here

The review drills from [code-review.md](code-review.md) still run, pointed at security:
- The learner reviews their own tool as if an AI wrote it (the AI-written check in [teaching-loop.md](teaching-loop.md) section 12 applies hard here, because security code copied without understanding is how real bugs ship).
- Drills plant security defects a review must catch: an off-by-one in an exploit offset, a crypto misuse (ECB, a static IV, a non-constant-time compare), a scanner that misses an edge, a parser that trusts its input.

## Where you cannot browse or write files

Same as the main skill: state nothing perishable as current, give the official link and let the learner verify; print tools and scripts in chat for them to save. Never serve a tool flag or a crypto primitive from memory as if current without the live doc behind it.
