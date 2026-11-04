# SCERT Class 11 Textbook Edition Reconciliation & Audit Report

**Execution Timestamp:** 2026-11-04T20:22:18Z  
**Target Repository:** [Eaglesiva/tn-class-11](https://github.com/Eaglesiva/tn-class-11)  
**Target Branch:** `scert/class-11/audit-2026-27`  
**Reference Live SCERT API URL:** `https://emis3.tnschools.gov.in/api/get_scert_books`  
**Live API Raw Snapshot SHA-256:** `404f283443b1f7a6a0fae814092aae556d0419ad2b4b2c0b0a0f7ebd756cc3e4`  
**Official Textbook Corporation Announcement:** Annual sale announced on 14 May 2026.

---

## 1. Class 11 Metric Reconciliation (32 State Board Books)

| Category | Count | Pages | Status & Repository Location |
| :--- | :---: | :---: | :--- |
| **GitHub Is Newer (2025 Revised)** | **4** | 1,152 | Preserved on `main` (Tamil 176p, Maths TM Vol 1 320p, Maths TM Vol 2 288p, Maths EM Vol 1 368p) |
| **Same Version (2024 Reprint Match)** | **4** | 1,264 | Preserved on `main` (Maths EM Vol 2 288p, History TM 352p, Geography TM 336p, Political Science TM 328p) |
| **Official Edition Updates (2024 Reprint)** | **24** | **7,832** | Downloaded & split into 1-page PDFs on branch `scert/class-11/official-version-updates` |
| **Total In-Scope Books** | **32** | **10,248** | **All 32 books reconciled under 4-tier verification protocol** |

---

## 2. The 24 Cloud-Updated Books Breakdown (7,832 Pages Verified)

- **Batch 1 (Commit `7102c457` - 1,848p)**: General English (216p), Physics TM Vol 1 (320p), Physics TM Vol 2 (336p), Physics EM Vol 1 (320p), Physics EM Vol 2 (328p), Chemistry TM Vol 1 (328p).
- **Batch 2 (Commit `16625d1f` - 2,072p)**: Chemistry TM Vol 2 (344p), Chemistry EM Vol 1 (304p), Chemistry EM Vol 2 (320p), Botany TM (384p), Botany EM (376p), Zoology TM (344p).
- **Batch 3 (Commit `ed6b0a04` - 2,000p)**: Zoology EM (304p), Computer Science TM (328p), Computer Science EM (328p), Commerce TM (336p), Commerce EM (336p), Accountancy TM (368p).
- **Batch 4 (Commit `c1a58225` - 1,912p)**: Accountancy EM (352p), Economics TM (336p), Economics EM (288p), History EM (320p), Geography EM (296p), Political Science EM (320p).

Each book includes `manifest.json`, `edition.json`, `edition.md`, `pages.json`, and complete continuous 1-page PDF sequences.
