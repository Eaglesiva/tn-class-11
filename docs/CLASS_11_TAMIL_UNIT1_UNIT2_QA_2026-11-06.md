# Class 11 Tamil — Unit 1 & Unit 2 Book Back / Quiz QA
Date: 2026-11-06
Branch: main

## Scope completed
- Unit 1: என்னுயிர் என்பேன்
- Unit 2: மாமழை போற்றுதும்
- Existing `questions.md` files were retained; no question extraction overwrite was performed.
- Created `answers.md`, `quiz.md`, and `quiz.json` for both units.
- Created subject-level master: `tamil/book_back_questions/quiz.json`.

## Repository source inventory
- Unit 1 PDF page files present: `page_013.pdf` through `page_032.pdf`; source reference in questions.md points to textbook page 27 and repository contains `page_027.pdf`.
- Unit 2 PDF page files present: `page_033.pdf` through `page_068.pdf`; source reference in questions.md points to pages 54–59 and repository contains `page_054.pdf` through `page_059.pdf`.
- The PDF binary page contents could not be opened/extracted by the available GitHub file reader in this run. Therefore page-by-page visual/text comparison is NOT certified.

## Answer source review
- Unit 1: six one-mark/objective candidates included, sourced to the direct Unit 1 answer page at https://www.kalvitips.com/2025/06/11th-tamil-book-back-answers-unit-1-guide-tamilnadu-school-books.html.
- Unit 2: five objective candidates are now included. The previously withheld soil-fertility item is added with answer “இவை மூன்றும்”, sourced to https://www.brainkart.in/article/Questions-and-Answers_12017/. This is an answer-source match; page-content comparison remains pending.
- Unit 2 question 2 (“மண்ணுக்கு வளம் சேர்ப்பன”) has been added as `TN11-TAM-U02-Q002`, answer index 3 (“இவை மூன்றும்”). It is included in unit and master quiz, with page-content comparison still pending.

## Quiz QA
| File | Records | Duplicate IDs | Invalid option sets | Invalid correct indexes | Missing source URLs |
|---|---:|---:|---:|---:|---:|
| Unit 1 quiz.json | 6 | 0 | 0 | 0 | 0 |
| Unit 2 quiz.json | 5 | 0 | 0 | 0 | 0 |
| Tamil master quiz.json | 11 | 0 | 0 | 0 | 0 |

- Every published item has exactly four distinct options.
- Every `correctOptionIndex` is an integer from 0 to 3.
- Master quiz is the ordered flattening of Unit 1 and Unit 2 quiz records.
- `quiz.md` includes the Unit 2 soil-fertility item.
- Long-answer questions were not answered; placeholder guidance is preserved in each `answers.md`.

## Edition / validity status
`CURRENT_VALIDITY_UNVERIFIED`. Repository page PDFs exist, but their page contents and the current official edition imprint/title pages were not visually verified in this run. Third-party guide websites are answer references, not official SCERT sources.

## Next required action
Open/extract the repository PDF pages for Unit 1 page 27 and Unit 2 pages 54–59, verify every published question and its option wording against those pages, resolve Unit 2 question 2, then update the verification status and master QA.


## Follow-up update — Unit 2 item added
- Added `TN11-TAM-U02-Q002` with four options and `correctOptionIndex: 3` to the Unit 2 quiz.
- Updated Unit 2 `quiz.md`, `answers.md`, and subject Master Quiz; the Master Quiz now contains 11 records.
- The answer is supported by the BrainKart guide URL, but remains `PAGE_CONTENT_COMPARISON_PENDING`; it is not labelled official textbook-page verified.

## Unit 3–4 source consistency check (2026-11-06)
- Actual repository paths are `tamil/03_unit_3/` and `tamil/04_unit_4/`; the alternate slugs supplied in the task are not present.
- Existing `questions.md` files were inspected and retained.
- Unit 3 supplied quiz data conflicts with existing `questions.md` on matching question 3 and sandhi question 4 (repository asks `முழவோசை`; supplied JSON asks `இனிதென`).
- Unit 4 supplied quiz data conflicts with existing `questions.md` on matching question 2; supplied questions 3–5 do not match the existing repository objective section, which currently has only four objective questions and different items.
- Therefore no Unit 3/4 quiz files were generated from mismatched supplied data. Resolve the source-version discrepancy against the relevant textbook PDF pages before writing quiz records. Existing questions.md files were not overwritten.
