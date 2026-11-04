import os, sys, json, time, requests, fitz, hashlib

batch_num = int(sys.argv[1]) if len(sys.argv) > 1 else 1

batches = {
    1: [
        {"key": "english_full", "subj_dir": "english", "vol": "full", "name": "General English", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_General%20English_Text.pdf"},
        {"key": "physics_tm_vol1", "subj_dir": "physics_tm", "vol": "vol1", "name": "Physics (Vol I)", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Physics_Vol-1_Tamil%20Medium_Text.pdf"},
        {"key": "physics_tm_vol2", "subj_dir": "physics_tm", "vol": "vol2", "name": "Physics (Vol II)", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Physics_Vol-2_Tamil%20Medium_Text.pdf"},
        {"key": "physics_em_vol1", "subj_dir": "physics_em", "vol": "vol1", "name": "Physics (Vol I)", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Physics%20Vol%201_English%20Medium_Text.pdf"},
        {"key": "physics_em_vol2", "subj_dir": "physics_em", "vol": "vol2", "name": "Physics (Vol II)", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Physics_Vol-2_English%20Medium_Text.pdf"},
        {"key": "chemistry_tm_vol1", "subj_dir": "chemistry_tm", "vol": "vol1", "name": "Chemistry (Vol I)", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Chemistry_Vol-1_Tamil%20Medium_Text.pdf"}
    ],
    2: [
        {"key": "chemistry_tm_vol2", "subj_dir": "chemistry_tm", "vol": "vol2", "name": "Chemistry (Vol II)", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th%20Chemistry_Vol-2%20TM_Text.pdf"},
        {"key": "chemistry_em_vol1", "subj_dir": "chemistry_em", "vol": "vol1", "name": "Chemistry (Vol I)", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Chemistry_Vol-1_English%20Medium_Text.pdf"},
        {"key": "chemistry_em_vol2", "subj_dir": "chemistry_em", "vol": "vol2", "name": "Chemistry (Vol II)", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Chemistry_Vol-2_English%20Medium_Text.pdf"},
        {"key": "botany_tm_full", "subj_dir": "botany_tm", "vol": "full", "name": "Botany", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Botany_TM_Text.pdf"},
        {"key": "botany_em_full", "subj_dir": "botany_em", "vol": "full", "name": "Botany", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Botany_EM_Text.pdf"},
        {"key": "zoology_tm_full", "subj_dir": "zoology_tm", "vol": "full", "name": "Zoology", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Zoology_TM_Text.pdf"}
    ],
    3: [
        {"key": "zoology_em_full", "subj_dir": "zoology_em", "vol": "full", "name": "Zoology", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Zoology_EM_Text.pdf"},
        {"key": "computer_science_tm_full", "subj_dir": "computer_science_tm", "vol": "full", "name": "Computer Science", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Computer%20Science_TM_Text.pdf"},
        {"key": "computer_science_em_full", "subj_dir": "computer_science_em", "vol": "full", "name": "Computer Science", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Computer%20Science_EM_Text.pdf"},
        {"key": "commerce_tm_full", "subj_dir": "commerce_tm", "vol": "full", "name": "Commerce", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Commerce_TM_Text.pdf"},
        {"key": "commerce_em_full", "subj_dir": "commerce_em", "vol": "full", "name": "Commerce", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Commerce_EM_Text.pdf"},
        {"key": "accountancy_tm_full", "subj_dir": "accountancy_tm", "vol": "full", "name": "Accountancy", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Accountancy_TM_Text.pdf"}
    ],
    4: [
        {"key": "accountancy_em_full", "subj_dir": "accountancy_em", "vol": "full", "name": "Accountancy", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Accountancy_EM_Text.pdf"},
        {"key": "economics_tm_full", "subj_dir": "economics_tm", "vol": "full", "name": "Economics", "med": "Tamil", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Economics_TM_Text.pdf"},
        {"key": "economics_em_full", "subj_dir": "economics_em", "vol": "full", "name": "Economics", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Economics_EM_Text.pdf"},
        {"key": "history_em_full", "subj_dir": "history_em", "vol": "full", "name": "History", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_History_EM_Text.pdf"},
        {"key": "geography_em_full", "subj_dir": "geography_em", "vol": "full", "name": "Geography", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Geography_EM_Text.pdf"},
        {"key": "political_science_em_full", "subj_dir": "political_science_em", "vol": "full", "name": "Political Science", "med": "English", "url": "https://d21mc000xink7q.cloudfront.net/scert/textbook/syllabuspdf/11th_Political%20Science%20EM_Text.pdf"}
    ]
}

current_batch = batches.get(batch_num, [])
print(f"=== Starting Class 11 Cloud Edition Update - Batch {batch_num} ({len(current_batch)} books) ===")

edition_name = "2026-27-scert-official"
summary_results = []

for b in current_batch:
    print(f"\n=======================================================")
    print(f"Processing: {b['name']} ({b['med']}) - Vol: {b['vol']}")
    print(f"URL: {b['url']}")
    
    temp_pdf = f"runner_temp_{b['key']}.pdf"
    print(f"Downloading master to {temp_pdf}...")
    resp = requests.get(b['url'], headers={'User-Agent': 'Mozilla/5.0'}, stream=True)
    resp.raise_for_status()
    with open(temp_pdf, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
                
    file_size_mb = os.path.getsize(temp_pdf) / (1024*1024)
    print(f"Downloaded master PDF: {file_size_mb:.2f} MB")
    
    doc = fitz.open(temp_pdf)
    total_pages = len(doc)
    p2_text = doc[1].get_text() if total_pages >= 2 else ""
    p2_lines = [l.strip() for l in p2_text.splitlines() if l.strip()]
    imprint_lines = [l for l in p2_lines if any(yr in l for yr in ['2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026', 'First', 'Revised', 'Reprint', 'பதிப்பு'])]
    print(f"Total pages: {total_pages}")
    print(f"Page 2 Imprint: {' | '.join(imprint_lines)}")
    
    if b['vol'] == 'full':
        ed_base = os.path.join(b['subj_dir'], "editions", edition_name)
    else:
        ed_base = os.path.join(b['subj_dir'], "editions", edition_name, b['vol'])
        
    pages_dir = os.path.join(ed_base, "pages")
    os.makedirs(pages_dir, exist_ok=True)
    
    print(f"Splitting {total_pages} pages into {pages_dir}...")
    manifest_entries = []
    page_files = []
    
    for p_idx in range(total_pages):
        single_doc = fitz.open()
        single_doc.insert_pdf(doc, from_page=p_idx, to_page=p_idx)
        p_filename = f"page_{p_idx + 1:03d}.pdf"
        p_path = os.path.join(pages_dir, p_filename)
        single_doc.save(p_path)
        single_doc.close()
        
        h = hashlib.sha256()
        with open(p_path, 'rb') as pf:
            h.update(pf.read())
        sha256 = h.hexdigest()
        
        page_files.append(f"./pages/{p_filename}")
        manifest_entries.append({
            "page_number": p_idx + 1,
            "filename": p_filename,
            "rel_path": f"pages/{p_filename}",
            "sha256": sha256,
            "size_bytes": os.path.getsize(p_path)
        })
        
        if (p_idx + 1) % 50 == 0 or (p_idx + 1) == total_pages:
            print(f"  Split progress: {p_idx + 1}/{total_pages}")
            
    doc.close()
    if os.path.exists(temp_pdf):
        os.remove(temp_pdf)
    print("Master PDF deleted from runner storage.")
    
    with open(os.path.join(ed_base, "pages.json"), "w", encoding="utf-8") as f:
        json.dump(page_files, f, indent=2)
        
    with open(os.path.join(ed_base, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump({
            "subject": b["name"],
            "medium": b["med"],
            "edition_name": edition_name,
            "volume": b["vol"],
            "total_pages": total_pages,
            "master_url": b["url"],
            "pages": manifest_entries
        }, f, indent=2)
        
    edition_meta = {
        "subject_name": b["name"],
        "medium": b["med"],
        "volume": b["vol"],
        "edition_name": edition_name,
        "source_url": b["url"],
        "download_date": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "total_pages": total_pages,
        "imprint_lines": imprint_lines,
        "runner_os": sys.platform
    }
    with open(os.path.join(ed_base, "edition.json"), "w", encoding="utf-8") as f:
        json.dump(edition_meta, f, indent=2)
        
    with open(os.path.join(ed_base, "edition.md"), "w", encoding="utf-8") as f:
        f.write(f"# Official SCERT Edition: {b['name']} ({b['med']})\n\n")
        f.write(f"- **Edition Tag**: `{edition_name}`\n")
        f.write(f"- **Volume**: `{b['vol']}`\n")
        f.write(f"- **Official URL**: {b['url']}\n")
        f.write(f"- **Download Timestamp**: {edition_meta['download_date']}\n")
        f.write(f"- **Total Page Count**: {total_pages}\n")
        f.write(f"- **Page 2 Imprint**:\n")
        for line in imprint_lines:
            f.write(f"  - {line}\n")
            
    summary_results.append({
        "key": b["key"],
        "name": b["name"],
        "medium": b["med"],
        "volume": b["vol"],
        "total_pages": total_pages,
        "edition_dir": ed_base
    })

os.makedirs("docs", exist_ok=True)
with open(f"docs/class_11_batch_{batch_num}_report.md", "w", encoding="utf-8") as f:
    f.write(f"# Class 11 Cloud Edition Update - Batch {batch_num} Report\n\n")
    f.write("| Subject | Medium | Volume | Total Pages | Edition Directory |\n")
    f.write("| :--- | :---: | :---: | :---: | :--- |\n")
    for s in summary_results:
        f.write(f"| {s['name']} | {s['medium']} | {s['volume']} | {s['total_pages']} | `{s['edition_dir']}` |\n")

print(f"\n=== Batch {batch_num} Processed Successfully! ===")
