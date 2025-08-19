# Arsenolipid-MS-process

A Python-only pipeline for processing mass spectrometry (mzML) data related to arsenolipids: from I/O, binning-based feature table, alignment & ML, to a searchable documentation site published via **GitHub Pages**.

## Quick Start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Put your *.mzML into data/raw/
# Prepare data/labels.csv with two columns: sample,label

# 1) Export TIC/BPC and binned peak tables
python -c "from src.io import export_tic_bpc; import glob; [export_tic_bpc(f) for f in glob.glob('data/raw/*.mzML')]"
python -c "from src.preprocessing import bin_peaks; import glob; [bin_peaks(f) for f in glob.glob('data/raw/*.mzML')]"

# 2) Merge features & train a simple classifier
python -c "from src.align import merge_binned_tables; merge_binned_tables()"
python -c "from src.ml import train_classify; train_classify()"

# 3) Export docs assets and preview the site locally
python -c "from src.report import export_summary_json; export_summary_json()"
mkdocs serve
```

## Publish to GitHub Pages
Push to `main` and GitHub Actions will build and deploy the site automatically.

## Repo Layout
```
Arsenolipid-MS-process/
├─ data/
│  ├─ raw/         # drop mzML here
│  ├─ interim/     # binned/temporary tables
│  └─ processed/   # final tables/plots/models
├─ notebooks/
├─ src/            # pipeline source code
├─ docs/           # mkdocs site content
├─ .github/workflows/gh-pages.yml  # CI for Pages
├─ requirements.txt
├─ mkdocs.yml
└─ README.md
```
