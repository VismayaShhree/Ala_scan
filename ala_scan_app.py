"""
Alanine scan figure - desktop app

Type a peptide sequence, click "Make figure", then "Save figure".
Saves a 600 dpi TIFF (or PNG).

Run:  python ala_scan_app.py
Needs: Python 3.10+, matplotlib, pillow (tkinter comes with most Python installs)
"""

import io
import tkinter as tk
from tkinter import filedialog, messagebox

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from PIL import Image, ImageTk

AMINO_ACID_CATEGORIES = {
    "polar":     ["N", "C", "Q", "S", "T", "Y"],
    "non-polar": ["A", "V", "L", "I", "M", "F", "P", "G", "W"],
    "anionic":   ["D", "E"],
    "cationic":  ["R", "H", "K"],
}

COLOR_MAP = {
    "polar":     "#9467bd",   # purple
    "non-polar": "#ff7f0e",   # orange
    "anionic":   "#d62728",   # red
    "cationic":  "#2ca02c",   # green
}

DPI = 600


def get_category(aa):
    for category, residues in AMINO_ACID_CATEGORIES.items():
        if aa.upper() in residues:
            return category
    raise ValueError(f"Unknown amino acid letter: {aa}")


def alanine_scan(sequence, skip_residues=("G", "I"), original_label="WT"):
    """Return [(sequence, label), ...]. Lowercase 'a' marks the swapped residue."""
    sequence = sequence.strip().upper()
    for aa in sequence:
        get_category(aa)  # raises on unknown letters
    skip = {r.upper() for r in skip_residues} | {"A"}

    rows = [(sequence, original_label)]
    for i, aa in enumerate(sequence):
        if aa in skip:
            continue
        new = list(sequence)
        new[i] = "a"
        rows.append(("".join(new), f"{aa}{i + 1}A"))
    return rows


def make_figure(rows, title="", show_labels=True):
    n_rows = len(rows)
    n_cols = len(rows[0][0])

    fig, ax = plt.subplots(figsize=(n_cols * 0.9 + 3, n_rows * 0.9 + 1))

    for r, (seq, label) in enumerate(rows):
        y = n_rows - r
        for c, aa in enumerate(seq):
            x = c + 1
            ax.add_patch(plt.Circle((x, y), 0.45,
                                    facecolor=COLOR_MAP[get_category(aa)],
                                    edgecolor="none"))
            ax.text(x, y, aa.upper(),
                    color="black" if aa == "a" else "white",
                    ha="center", va="center", fontsize=18, weight="bold")
        if show_labels and label:
            ax.text(0.3, y, label, ha="right", va="center",
                    fontsize=14, weight="bold")

    ax.legend(handles=[Patch(facecolor=col, edgecolor="none", label=name)
                       for name, col in COLOR_MAP.items()],
              loc="center left", bbox_to_anchor=(1, 0.5),
              frameon=False, fontsize=12)

    if title:
        ax.set_title(title, fontsize=24, weight="bold", color="green")

    ax.set_xlim(-0.8 if show_labels else 0.4, n_cols + 0.6)
    ax.set_ylim(0.4, n_rows + 0.6)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig


class App:
    def __init__(self, root):
        self.root = root
        self.fig = None
        self.preview = None
        root.title("Alanine Scan")

        form = tk.Frame(root)
        form.pack(padx=12, pady=8)

        tk.Label(form, text="Sequence:").grid(row=0, column=0, sticky="e")
        self.seq_entry = tk.Entry(form, width=40)
        self.seq_entry.grid(row=0, column=1, pady=2)

        tk.Label(form, text="Peptide name:").grid(row=1, column=0, sticky="e")
        self.name_entry = tk.Entry(form, width=40)
        self.name_entry.grid(row=1, column=1, pady=2)

        tk.Label(form, text="Don't swap:").grid(row=2, column=0, sticky="e")
        self.skip_entry = tk.Entry(form, width=40)
        self.skip_entry.insert(0, "G, I")
        self.skip_entry.grid(row=2, column=1, pady=2)

        tk.Label(form, text="Original row label:").grid(row=3, column=0, sticky="e")
        self.wt_entry = tk.Entry(form, width=40)
        self.wt_entry.insert(0, "WT")
        self.wt_entry.grid(row=3, column=1, pady=2)

        self.labels_var = tk.BooleanVar(value=True)
        tk.Checkbutton(form, text="Show row labels (WT, D2A, ...)",
                       variable=self.labels_var).grid(row=4, column=1, sticky="w")

        buttons = tk.Frame(root)
        buttons.pack(pady=4)
        tk.Button(buttons, text="Make figure", command=self.make).pack(side="left", padx=4)
        tk.Button(buttons, text="Save figure", command=self.save).pack(side="left", padx=4)

        self.canvas = tk.Canvas(root, width=700, height=450, bg="white")
        self.canvas.pack(padx=12, pady=8)

    def make(self):
        seq = self.seq_entry.get().strip()
        if not seq:
            messagebox.showwarning("Missing sequence", "Please type a peptide sequence.")
            return
        skip = [s.strip() for s in self.skip_entry.get().replace(",", " ").split() if s.strip()]
        try:
            rows = alanine_scan(seq, skip, self.wt_entry.get().strip())
        except ValueError as e:
            messagebox.showerror("Sequence error", str(e))
            return

        if self.fig is not None:
            plt.close(self.fig)
        self.fig = make_figure(rows, self.name_entry.get().strip(), self.labels_var.get())

        buf = io.BytesIO()
        self.fig.savefig(buf, format="png", dpi=100, bbox_inches="tight")
        buf.seek(0)
        img = Image.open(buf)
        img.thumbnail((700, 450), Image.LANCZOS)
        self.preview = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(350, 225, anchor="center", image=self.preview)

    def save(self):
        if self.fig is None:
            messagebox.showwarning("No figure", "Click 'Make figure' first.")
            return
        name = self.name_entry.get().strip() or "ala_scan"
        path = filedialog.asksaveasfilename(
            defaultextension=".tif",
            initialfile=f"{name}_ala_scan.tif",
            filetypes=[("TIFF image", "*.tif"), ("PNG image", "*.png")],
            title="Save figure",
        )
        if path:
            self.fig.savefig(path, dpi=DPI, bbox_inches="tight")
            messagebox.showinfo("Saved", f"Saved at {DPI} dpi:\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
