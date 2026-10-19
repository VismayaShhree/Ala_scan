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

`ala_scan_app.py` does the same thing in a small window with buttons, no coding needed. You only set it up once.

### Step 1. Install Python (once)

1. Go to [python.org/downloads](https://www.python.org/downloads/) and download the latest Python 3.
2. Run the installer.
   - **Windows:** tick **"Add python.exe to PATH"** on the first screen, then click Install.
   - **Mac:** click through the installer with the default options.

### Step 2. Download this project (once)

1. At the top of this page, click the green **Code** button → **Download ZIP**.
2. Unzip it. You get a folder called `Ala_scan-main`.

### Step 3. Open a terminal in that folder

- **Mac:** open the **Terminal** app. Type `cd ` (with a space), drag the `Ala_scan-main` folder into the Terminal window, and press Enter.
- **Windows:** open the `Ala_scan-main` folder, click the address bar at the top, type `cmd`, and press Enter.

### Step 4. Install the required packages (once)

Copy this line into the terminal and press Enter:

| Mac | Windows |
|---|---|
| `pip3 install -r requirements.txt` | `pip install -r requirements.txt` |

### Step 5. Start the app

| Mac | Windows |
|---|---|
| `python3 ala_scan_app.py` | `python ala_scan_app.py` |

A window opens.

### Step 6. Make your figure

1. **Sequence:** type your peptide in one-letter codes, e.g. `VQAAQAGDTKPIEV`.
2. **Peptide name:** e.g. `PN3`. This becomes the title and file name.
3. **Don't swap:** residues to leave as they are. Default is `G, I`. Clear the box to scan every residue.
4. **Original row label:** `WT` by default. You can type `Native` instead.
5. Click **Make figure** to see a preview.
6. Click **Save figure**, choose where to save, and pick TIFF or PNG. The image is saved at 600 dpi.

**Next time** you only need Steps 3 and 5.

### If something goes wrong

| Message | Fix |
|---|---|
| `python: command not found` (Mac) | Use `python3` instead of `python` |
| `'python' is not recognized` (Windows) | Reinstall Python and tick "Add python.exe to PATH" |
| `No module named 'matplotlib'` or `'PIL'` | Run Step 4 again |
| `No module named 'tkinter'` | Install Python from python.org (some other installs leave this part out) |
| `No such file or directory` | You're not in the project folder. Repeat Step 3 |

## Citation

If you use this notebook, please cite the archived code:

> Lokesh, Dhanashree (2026). Ala_scan: alanine-scan visualisation notebook. Zenodo. https://doi.org/10.5281/zenodo.23483270

The associated article is in preparation.

## License

MIT. See [LICENSE](LICENSE).
