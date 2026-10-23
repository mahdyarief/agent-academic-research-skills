---
name: thesis-supervisor-outreach
description: "Use when approaching a prospective thesis supervisor."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thesis, supervisor, pembimbing, proposal, briefing, research]
    related_skills: [thesis-proposal, paper-reading-mentoring, journal-scouting]
---

# Thesis Supervisor Outreach

Mahdy names a lecturer he wants as pembimbing and asks for help. Job: verify who
the person actually is, judge genuine fit against Mahdy's gap, and produce a
one-page briefing he can bring to the meeting. Deliver in relaxed Bahasa Indonesia.

## When to use
- "gw mau bimbingan sama dosen X", "cari dosen namanya <nama>", "cocok gak dia jadi pembimbing?"
- Preparing the meeting artefact (bahan bimbingan) for a named lecturer.
- Do NOT use for finding the paper's gap (thesis-proposal) or reading papers
  (paper-reading-mentoring) — those feed this one.

## Procedure

1. **Find the person, don't assume the profile.** Two searches in one turn:
   `"<nama lengkap>" <kampus> dosen <prodi>` and
   `site:<kampus-domain> "<nama>"`. The prodi's own faculty page is the
   authoritative record for NIP, kode dosen, kelompok keahlian (KK), and jabatan
   fungsional; a Google Scholar profile cross-checks the research area and that
   the email is domain-verified.
2. **Correct the degree in your reply, unprompted.** The user's label for the
   person is often stale ("dia S2" when they have since earned a doctorate).
   State the current gelar and the year it was awarded — it changes both how you
   address them and their eligibility as a supervisor.
3. **Pull the research line, not just the title.** From the search snippets,
   collect: dissertation/thesis topic, graduating institution, and recent
   co-authored papers with students (these show what they will actually
   supervise). Student co-authorship is a positive signal.
4. **Build the FIT BRIDGE explicitly.** Name one mechanism the supervisor's own
   research cares about and map Mahdy's gap onto it in a single sentence.
   Then state the KK overlap (their KK vs Mahdy's BIS/DigiBiz track). Also
   quote any forward-looking statement by the person saying the research should
   be extended to field Y — that is the door in.
5. **Write the 1-page briefing** and hand over the gap, never the reading pile.
6. **Flag the admin gate before the meeting**, not after: check S2 supervisor
   eligibility rules (minimum jabfung / gelar) against the person's recorded
   jabfung, and tell Mahdy to confirm with the kaprodi.

## The 1-page briefing artefact

Fixed order, one page, no tables (WhatsApp-legible): 1-paragraf topik (versi
lisan) → jembatan ke riset calon pembimbing → draft gap I-N-G-J ringkas →
posisi novelty jujur → rencana jalur → pertanyaan untuk dosen INCLUDING the
direct one: kesediaan membimbing + syarat administrasi.

Reusable starter: `templates/bahan-bimbingan-1pager.md`.

## Naming and honesty rules for the topic paragraph

- Mnemonic **O-P-O-I** for the spoken topic sentence: Objek teknologi, Populasi,
  Outcome (dual), Intervensi. A sentence missing any of the four leaves the
  supervisor guessing.
- **Name the technology explicitly, never its generic category.** Writing bare
  "multi-agent" lets the supervisor misread the object as a non-AI system.
  Define, in one clause, what the alternative architectures are.
- **State the DUAL outcome when the study has two.** Cost alone reads as finance;
  decision quality alone reads as psychology. Name both; match the emphasized
  outcome to the supervisor's own line while keeping the other present.
- **Every topic sentence needs an INTERVENTION, not only a problem.** Name the
  artefact/mechanism he will build and test.
- **Label self-coined terms as self-coined, in the same breath.** When the
  intervention name is Mahdy's own coinage rather than a term from the papers he
  read, say so plainly, define it in one concrete line with a worked example, and
  present it as a draft concept whose final shape the supervisor should direct —
  never as established literature. If Mahdy asks "what is <term>?" it means the
  coinage was introduced without a definition — answer with the definition and an
  example, then say explicitly where the term came from.
- Keep a mnemonic when the artefact has a fixed shape, and keep it one line.

## Confidence and defense coaching (when user expresses doubt / \"belum pede\")

A student pitching to a doctoral lecturer naturally feels under-confident.
When the user says \"belum pede\", \"takut ditanya\", \"ragu\", do NOT give a generic
pep talk. Coach the defense across three predictable lecturer challenges —
mnemonic **M-P-K**:

- **M — Masalah bisnis, bukan teknis**: Lecturer challenge: \"Ini ranah Informatika /
  teknis AI, bukan Sistem Informasi.\" Counter: frame the dependent variable as
  **decision quality & IT cost governance**, not building algorithms. Non-technical
  practitioners choose multi-agent architectures using misleading human-org analogies;
  the research studies the misconception and intervenes to prevent cost blowouts.
- **P — Populasi spesifik, bukan general**: Lecturer challenge: \"Siapa yang pakai
  token-based di Indonesia?\" Counter: purposive sample of digital builders, agencies,
  and automation consultants (N=30–50) with verified usage-based API/credit spend,
  not the general public.
- **K — Kontribusi / intervensi XAI**: Lecturer challenge: \"Apa hubungannya dengan
  bidang saya? / Apa itu decision card?\" Counter: link directly to the supervisor's
  core expertise (e.g. XAI for decision-making). The decision card is an explainable
  AI intervention artefact that makes architectural trade-offs legible before
  execution.

Always close coaching with a concrete **spoken 2-minute elevator pitch** the
user can read aloud, and offer a short roleplay simulation before the actual meeting.

## Pitfalls
- Do not claim fit from the supervisor's topic title alone — read what their
  students actually publish with them.
- An Asisten Ahli / recent-doctor jabfung restricts supervisor eligibility at
  many Indonesian programmes; surface it as a question for the kaprodi, not as a
  disqualification you decided.
- A supervisor's home-field can pull the topic off Mahdy's lens. Say plainly
  that Mahdy keeps the BIS lens dominant and borrows only the bridge.
- Faculty profile fields (NIP, KK, jabfung) are usually already in the
  search-result snippet — read them there before attempting page extraction,
  which may be blocked.
- Never quote a degree, jabfung, or affiliation that only appeared in a social /
  aggregator page when the prodi's own page contradicts it — reconcile first.
