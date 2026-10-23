---
name: thesis-proposal
description: "Use when drafting a thesis proposal or problem statement."
version: 0.1.0
author: Mahdy, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [thesis, proposal, novelty, problem-statement, research]
    related_skills: [journal-scouting, paper-writing, paper-reading-mentoring]
---

# Thesis & Proposal Design

Help Mahdy (S2 SI Telkom, Digital Business) turn an AREA into a defensible
proposal: clear problem statement, checked novelty, sharp research question, and
the correct Telkom proposal skeleton. Mindset: M-B-S — Masalah dulu, Berpikir,
baru Solusi/tools. Never start from a "cool title".

## When to Use
- Mahdy asks "judul proposal apa ya?", "bingung masalahnya", "gimana bikin problem statement", "apa novelty-nya?".
- Week-by-week Metodologi progress: this skill answers the PREPARATION FOR PROPOSAL phase.
- Do NOT use for paper discovery (journal-scouting) or manuscript drafting (paper-writing).

## Core: what a research "Masalah" is
- Masalah = kesenjangan antara das Sollen (seharusnya: standar/teori/regulasi/ekspektasi)
  dan das Sein (nyatanya: data/fenomena/observasi). Mnemonic: SE-HA-RUS-nya vs NYA-TA-nya.
- Distinguish 4 things (mnemonic TO-GE-TA-MA): TOPIK (area luas) → GEJALA (yang kelihatan,
  = akibat, bukan masalah) → TANTANGAN (keluhan umum, belum tentu masalah riset) →
  MASALAH (gap spesifik, bisa diteliti, ada bukti). Jangan berhenti sebelum Tahap Masalah.
- Layak-teliti filter (mnemonic FIS-BEL): Feasible, Interesting, Significant, Baru (novelty),
  Etis, Luasnya pas.

## Dua jenis masalah empiris
- SUDAH ada literaturnya: fenomena sudah diteliti tapi belum tuntas (konteks/populasi/teori
  bolong) → jalur INCREMENTAL/CONTESTED. Aman buat S2: pijakan teori ada, pustaka gampang.
  Syarat: diferensiasi eksplisit — jangan ulang yang sudah ada.
- BELUM ada literaturnya: fenomena nyata tapi belum ditulis siapa pun → jalur GENUINELY NOVEL.
  Risiko tinggi: teori tipis, metode eksploratif (kualitatif/DSR), pembimbing bisa skeptis;
  bukti lapangan (data/observasi) harus kuat.
- Cara bedain: LIVE SWEEP (bukan feeling) di OpenAlex/Scopus. Ketemu paper dekat → jenis 1,
  petakan apa yang belum dijawab. Tidak ketemu → curiga jenis 2, tapi longgarkan keyword +
  cek citation graph dulu sebelum klaim novel.
- Mnemonic: SUDAH = pijakannya ada, buktikan bedanya. BELUM = ladang kosong, buktikan datanya.
- Rekomendasi S2: ambil jenis 1 untuk thesis (lulus tepat waktu > heroik novelty); jenis 2
  simpan untuk paper berikutnya.

## Tanya balik kalau kurang jelas
- Kalau deskripsi area/fenomena Mahdy ambigu (konteks, populasi, bukti belum jelas),
  JANGAN langsung sweep atau menebak — tanya dulu: fenomena apa yang dia lihat, di konteks
  industri mana, bukti apa yang dia punya, kenapa ini penting.
- Konfirmasi pilihan (area, jenis masalah, RQ) di tiap gate sebelum lanjut.

## Problem statement: the I-N-G-J paragraph
One 1-3 paragraph statement of the gap. Structure (Ali & Pandya four-stage framework,
Modul 2):
1. I — kondisi IDEAL (seharusnya: literatur/regulasi/target)
2. N — kondisi NYATA + bukti (data/penelitian sebelumnya)
3. G — GAP di antara keduanya + konsekuensi kalau dibiarkan
4. J — JAWABAN: apa yang penelitian ini akan lakukan
Title follows from a complete I-N-G-J, not the reverse.

## Novelty check (anti-reinvention, from paper-writer novelty-check)
Run a LIVE sweep on the candidate question using real literature tools
(journal-scouting API path: OpenAlex keyless; Scopus via fastmcp-browser; also
Scopus Sources per-quartile for journal targeting). Never judge novelty from
memory. Classify into 4 verdicts:
- GENUINELY NOVEL → proceed
- INCREMENTAL (narrower pop/older data/lower design) → proceed, differentiator MUST be explicit
- ALREADY ANSWERED → kill or reframe; state why existing evidence falls short
- CONTESTED → strong warrant; design to adjudicate, not add a vote
Anti-pattern: Sakana v2 rated itself novel while territory was mapped. The
corrective = live query + honest verdict. Human (Mahdy) owns the final call;
AI only executes the sweep and presents evidence.

## Research question
- Derive RQ from the GAP, not from the method. Format: one sentence, falsifiable,
  scoped to context (Digital Business lens: value creation, governance, decision
  quality — not usability/technicality alone).
- Generate 5-15 candidate RQs, rank by FINER (Feasible, Interesting, Novel,
  Ethical, Relevant), let Mahdy pick — never auto-select.

## Proposal skeleton (Telkom S2 SI)
1. Pendahuluan: latar belakang (I-N-G-J) → rumusan masalah → tujuan → kontribusi
2. Kajian Pustaka: teori + literature matrix (lihat paper-writing) → posisi riset (gap)
3. Metodologi: pendekatan (kualitatif/kuantitatif/mixed/DSR), instrumen, analisis
4. Rencana: jadwal, risiko, luaran (riset/kursus/projek mode)
Output: docx via `docx` skill; save per-proposal folder under
<WORKSPACE>/ (or proposal/<slug>/), never loose files.

## Pitfalls
- Judul boleh ganti 3-4x selama proposal — arah masalah yang dijual, bukan judulnya.
- Jangan mix 3 area riset (governance/lakehouse/AI agent) dalam satu proposal; pilih satu.
- Pustaka awal cukup 3-5 paper relevan untuk mengisi N dan G — tidak perlu 50.
- Data/angka di bagian N harus bisa dirujuk (literatur atau sumber resmi); jangan mengarang.
