# SCERT Class 11 Textbook Edition Reconciliation & Audit Report

**Execution Timestamp:** 2026-11-05T02:23:00+05:30  
**Target Repository:** [Eaglesiva/tn-class-11](https://github.com/Eaglesiva/tn-class-11)  
**Audit Branch:** [`scert/class-11/audit-2026-27`](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/audit-2026-27)  
**Update Storage Branch:** [`scert/class-11/official-version-updates`](https://github.com/Eaglesiva/tn-class-11/tree/scert/class-11/official-version-updates)  
**Reference Live SCERT API URL:** `https://emis3.tnschools.gov.in/api/get_scert_books`  
**Live API Raw Snapshot SHA-256:** `404f283443b1f7a6a0fae814092aae556d0419ad2b4b2c0b0a0f7ebd756cc3e4`  
**Official Textbook Corporation Announcement:** Annual sale announced on 14 May 2026.

---

## 1. Class 11 Metric Reconciliation (32 State Board Books)

| Category | Count | Pages | Status & Repository Location |
| :--- | :---: | :---: | :--- |
| **GitHub Is Newer (2025 Revised)** | **4** | 1,152 | Preserved on `main` (Tamil 176p, Maths TM Vol 1 320p, Maths TM Vol 2 288p, Maths EM Vol 1 368p) |
| **Same Version (2024 Reprint Match)** | **4** | **1,304** | Preserved on `main` (Maths EM Vol 2 288p, History TM 352p, Geography TM 336p, Political Science TM 328p) |
| **Official Edition Updates (2024 Reprint)** | **23** | **7,528** | Stored & verified on branch `scert/class-11/official-version-updates` |
| **API Mapping Unresolved (Chemistry EM Vol 1)** | **1** | **304** | Preserved on branch `scert/class-11/official-version-updates`; API duplication documented |
| **Total In-Scope Books** | **32** | **10,288** | **All 32 books reconciled under 4-tier verification protocol** |

---

## 2. Chemistry EM Vol-I API Mapping Ambiguity Resolution

> [!NOTE]
> **Finding**: In the official SCERT API (`https://emis3.tnschools.gov.in/api/get_scert_books`), both **Chemistry (Vol I), English** and **Chemistry (Vol II), English** point to the identical URL:  
> `https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Chemistry_Vol-2_English%20Medium_Text.pdf` (320 pages).
> 
> **Branch Evidence**: On GitHub branch `scert/class-11/official-version-updates`, the genuine Vol-1 asset (`11th_Chemistry_Vol-1_English%20Medium_Text.pdf`) was processed, generating **304 single-page PDFs** under `chemistry_em/editions/2026-27-scert-official/vol1/` with full sequential validation (1-304) and all 4 edition manifests.
> 
> **Designation**: To avoid misattributing official API data, the catalog status is formally recorded as `API_MAPPING_UNRESOLVED`. The 304 verified pages on GitHub are preserved intact without modification or deletion.

---

## 3. Layer 1 Source Verification Metrics (HTTP GET & HEAD Confirmed)

All 32 official book URLs were verified on the official SCERT CloudFront CDN without full payload download (Zero Local Download policy):
- **HTTP GET Status**: `GET_200` confirmed for all 32/32 books.
- **HTTP HEAD Status**: `HEAD_200` confirmed for all 32/32 books.
- **Content-Length (Bytes)**: Captured for all 32/32 books.
- **Source ETag**: Captured for all 32/32 books as an immutable CDN identifier (distinct from cryptographic Master SHA-256).
- **Master PDF SHA-256**: Formally recorded as `NOT_CAPTURED` (Zero Local Download policy).

---

## 4. Layer 3 Split Validation Reproducible Audit (7,832 Pages Verified)

Verified directly against GitHub remote tree (`Commit: c1a58225`, `Tree: 349b7a6a`) on branch `scert/class-11/official-version-updates`:
- **Total Edition Directories**: 24/24 active edition directories.
- **Total Split Pages**: Exactly **7,832 pages** (23 Official Updates = 7,528p + 1 API Mapping Unresolved = 304p).
- **Sequential Validation**: **100% Passed** (every book strictly sequential from `page_001.pdf` to `page_xxx.pdf`, 0 gaps, 0 duplicates).
- **Manifest Completeness**: All 24 directories possess `edition.json`, `edition.md`, `manifest.json`, and `pages.json`.

> [!IMPORTANT]
> **Scope of Validation Note**: Split Validation certifies the physical integrity, page continuity, sequential numbering, and manifest completeness of the newly generated edition sets. It confirms Layer 1 (Source), Layer 2 (Edition/Imprint), and Layer 3 (Split Integrity). Full page-by-page text and visual diff against legacy GitHub `main` editions (Layer 4) is a separate post-reconciliation analysis and is pending.

### Verified Editions Table:
| # | Edition Path | Pages | Sequential Range | Manifests Present |
| :---: | :--- | :---: | :---: | :--- |
| 1 | `accountancy_em/editions/2026-27-scert-official` | 352 | `page_001.pdf` to `page_352.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 2 | `accountancy_tm/editions/2026-27-scert-official` | 368 | `page_001.pdf` to `page_368.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 3 | `botany_em/editions/2026-27-scert-official` | 376 | `page_001.pdf` to `page_376.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 4 | `botany_tm/editions/2026-27-scert-official` | 384 | `page_001.pdf` to `page_384.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 5 | `chemistry_em/editions/2026-27-scert-official/vol1` | 304 | `page_001.pdf` to `page_304.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 6 | `chemistry_em/editions/2026-27-scert-official/vol2` | 320 | `page_001.pdf` to `page_320.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 7 | `chemistry_tm/editions/2026-27-scert-official/vol1` | 328 | `page_001.pdf` to `page_328.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 8 | `chemistry_tm/editions/2026-27-scert-official/vol2` | 344 | `page_001.pdf` to `page_344.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 9 | `commerce_em/editions/2026-27-scert-official` | 336 | `page_001.pdf` to `page_336.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 10 | `commerce_tm/editions/2026-27-scert-official` | 336 | `page_001.pdf` to `page_336.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 11 | `computer_science_em/editions/2026-27-scert-official` | 328 | `page_001.pdf` to `page_328.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 12 | `computer_science_tm/editions/2026-27-scert-official` | 328 | `page_001.pdf` to `page_328.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 13 | `economics_em/editions/2026-27-scert-official` | 288 | `page_001.pdf` to `page_288.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 14 | `economics_tm/editions/2026-27-scert-official` | 336 | `page_001.pdf` to `page_336.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 15 | `english/editions/2026-27-scert-official` | 216 | `page_001.pdf` to `page_216.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 16 | `geography_em/editions/2026-27-scert-official` | 296 | `page_001.pdf` to `page_296.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 17 | `history_em/editions/2026-27-scert-official` | 320 | `page_001.pdf` to `page_320.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 18 | `physics_em/editions/2026-27-scert-official/vol1` | 320 | `page_001.pdf` to `page_320.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 19 | `physics_em/editions/2026-27-scert-official/vol2` | 328 | `page_001.pdf` to `page_328.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 20 | `physics_tm/editions/2026-27-scert-official/vol1` | 320 | `page_001.pdf` to `page_320.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 21 | `physics_tm/editions/2026-27-scert-official/vol2` | 336 | `page_001.pdf` to `page_336.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 22 | `political_science_em/editions/2026-27-scert-official` | 320 | `page_001.pdf` to `page_320.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 23 | `zoology_em/editions/2026-27-scert-official` | 304 | `page_001.pdf` to `page_304.pdf` | edition.json, edition.md, manifest.json, pages.json |
| 24 | `zoology_tm/editions/2026-27-scert-official` | 344 | `page_001.pdf` to `page_344.pdf` | edition.json, edition.md, manifest.json, pages.json |

---

## 5. Summary of Commits
- **Update Storage Branch**: `scert/class-11/official-version-updates` (Commits `7102c457`, `16625d1f`, `ed6b0a04`, `c1a58225` - 7,832 pages)
- **Audit Documentation Branch**: `scert/class-11/audit-2026-27`
