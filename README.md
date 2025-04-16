# Domain Search

This project implements a pipeline using **HMMER** to search for known **PFAM domains** across protein sequences from various organisms in the **EukProt** database. The goal is to identify the presence of specific functional protein domains and compare their distribution across eukaryotic lineages.

## 🧬 Project Overview

- **PFAM Domains:** A curated list of PFAM HMMs were selected for domain-specific searches (e.g., PF03368, PF00636, PF00271, etc.).
- **HMMER:** Used to scan protein sequences from EukProt using the `hmmsearch` tool.
- **EukProt:** A reference database of predicted protein sequences from a broad sampling of eukaryotic diversity.
- **Output:** A matrix indicating the presence/absence of PFAMs across organisms, with additional logic for defining domain combinations (e.g., Dicer-like proteins).

## 🔍 Key Features

- **Automated `hmmsearch`** across EukProt datasets.
- **Custom logic for domain combinations**, such as:
  - "Dicer-like" proteins require either:
    - PF03368 + PF00636 + PF00271, **or**
    - PF00035 + PF00636 + PF00271.
- **Presence/absence matrix** generation for easy downstream visualization (e.g., heatmaps, bubble plots).
- **Flexible PFAM input**: Easily modify which PFAMs to search for.

## 📁 Folder Structure
```
project
pfam_pipeline_project/
├── src/                                
│   ├── __init__.py
│   ├── main.py                         
│   ├── pfam_pipeline.py                
│   ├── pfam_searcher.py                
│   └── utils.py                        
│
├── data/                               
├── pfam_models/                        
├── results/                            
├── output/                             
│
├── requirements.txt                    
├── README.md                           

```

## ⚙️ Requirements

- Python 3.7+
- HMMER 3.3+
- biopython, pandas, numpy, seaborn, matplotlib (for processing and visualization)

## 🚀 How to Run

1. **Prepare PFAM HMMs and Databases:**
   - Download from [Pfam database](https://www.ebi.ac.uk/interpro/entry/pfam/) and place in `pfam_models/`.
   - Download either the [196 database](https://figshare.com/articles/dataset/TCS_tar_gz/21586065?file=38256648) or the [full database](https://figshare.com/articles/dataset/EukProt_a_database_of_genome-scale_predicted_proteins_across_the_diversity_of_eukaryotic_life/12417881/3?file=34434377)

2. **Run `hmmsearch`**:
   - Install from [HMMER website](http://hmmer.org/)
   - Use the provided script to scan all EukProt proteins with your PFAM HMMs.

3. **Parse Results:**
   - Convert HMMER outputs into a binary matrix indicating domain presence.
   - Add custom logic for domain combinations.
   - Example:
     ```bash
     python scripts/parse_hmm_results.py
     ```

4. **Visualize:**
   - Create heatmaps or other plots to explore domain distributions.

## 📊 Example Use Case

Identify and compare Dicer-like proteins across Amoebozoa and Metazoa in the EukProt database by analyzing co-occurrence of specific PFAM domains.

## 📘 References

- [HMMER](http://hmmer.org/)
- [Pfam](http://pfam.xfam.org/)
- [EukProt](https://eukprot.github.io/)