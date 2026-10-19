# Ala_scan

A Jupyter notebook that draws an alanine-scan figure for a peptide.

Type in a peptide sequence and the notebook swaps each residue for alanine, one position at a time. Every variant is drawn as a row of circles coloured by amino acid class, with each row labelled by its substitution (for example D8A). The figure is saved as a 600 dpi TIFF, ready for a paper.

![Example alanine-scan figure](ala_scan.png)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VismayaShhree/Ala_scan/blob/main/Alanin_sca.ipynb)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23483270.svg)](https://doi.org/10.5281/zenodo.23483270)

## Run it in your browser

Click the **Open in Colab** badge above. You only need a Google account.

1. In the first code cell, type your sequence and a name for the peptide.
2. Choose **Runtime → Run all**.
3. The last cell downloads the figure to your computer.

## Settings

All settings are in the first code cell.

| Setting | What it does | Default |
|---|---|---|
| `original_sequence` | Your peptide, one-letter codes | `"VQAAQAGDTKPIEV"` |
| `peptide_name` | Figure title and file name | `"PN3"` |
| `skip_residues` | Residues not swapped to alanine | `["G", "I"]` |
| `show_title` | Show the peptide name above the figure | `True` |
| `original_label` | Label for the original row, e.g. `"WT"` or `"Native"` | `"WT"` |
| `show_labels` | Show row labels such as WT, D8A | `True` |
| `file_format` | `"tif"` or `"png"` | `"tif"` |
| `dpi` | Image resolution | `600` |

Glycine and isoleucine are skipped by default because swapping them to alanine usually changes little. Set `skip_residues = []` to scan every residue. Residues that are already alanine are always skipped.

## Colour scheme

| Class | Residues | Colour |
|---|---|---|
| Polar | N, C, Q, S, T, Y | Purple |
| Non-polar | A, V, L, I, M, F, P, G, W | Orange |
| Anionic | D, E | Red |
| Cationic | R, H, K | Green |

## Run it on your computer

You need Python 3.10 or newer.

```bash
git clone https://github.com/VismayaShhree/Ala_scan.git
cd Ala_scan
pip install -r requirements.txt
jupyter notebook Alanin_sca.ipynb
```

## Desktop app (optional)

`ala_scan_app.py` does the same thing with a small window: type the sequence, click **Make figure**, then **Save figure**. It needs Python on your computer.

```bash
pip install -r requirements.txt
python ala_scan_app.py
```

## Citation

If you use this notebook, please cite the archived code:

> Lokesh, Dhanashree. (2026). Ala_scan: alanine-scan visualisation notebook. Zenodo. https://doi.org/10.5281/zenodo.23483270

The associated article is in preparation.

## License

MIT. See [LICENSE](LICENSE).
