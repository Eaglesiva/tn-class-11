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
- Unit 2: four confirmed objective candidates included, sourced to https://www.studentsguide360.com/11th-tamil-unit-2-book-back-answer/.
- Unit 2 question 2 (“மண்ணுக்கு வளம் சேர்ப்பவை”) is excluded from the published quiz and marked `REVIEW_REQUIRED_SOURCE_CONFLICT`: StudentsGuide360 gives “இவை மூன்றும்”, while BrainKart's guide page gives a different answer. Resolve only after checking the corresponding repository PDF page content.

## Quiz QA
| File | Records | Duplicate IDs | Invalid option sets | Invalid correct indexes | Missing source URLs |
|---|---:|---:|---:|---:|---:|
| Unit 1 quiz.json | 6 | 0 | 0 | 0 | 0 |
| Unit 2 quiz.json | 4 | 0 | 0 | 0 | 0 |
| Tamil master quiz.json | 10 | 0 | 0 | 0 | 0 |

- Every published item has exactly four distinct options.
- Every `correctOptionIndex` is an integer from 0 to 3.
- Master quiz is the ordered flattening of Unit 1 and Unit 2 quiz records.
- `quiz.md` omits the unresolved Unit 2 item.
- Long-answer questions were not answered; placeholder guidance is preserved in each `answers.md`.

## Edition / validity status
`CURRENT_VALIDITY_UNVERIFIED`. Repository page PDFs exist, but their page contents and the current official edition imprint/title pages were not visually verified in this run. Third-party guide websites are answer references, not official SCERT sources.

## Next required action
Open/extract the repository PDF pages for Unit 1 page 27 and Unit 2 pages 54–59, verify every published question and its option wording against those pages, resolve Unit 2 question 2, then update the verification status and master QA.
