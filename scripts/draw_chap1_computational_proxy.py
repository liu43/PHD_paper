from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.image as mpimg
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "figures" / "chap1_computational_proxy.pdf"
OUT_PNG = ROOT / "figures" / "chap1_computational_proxy.png"

PANELS = [
    ROOT / "figures" / "chap1_comp_sharp.png",
    ROOT / "figures" / "chap1_comp_kwok.png",
    ROOT / "figures" / "chap1_comp_jiang.png",
]


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 11,
            "font.family": "DejaVu Serif",
        }
    )


def main() -> None:
    fig, axes = plt.subplots(1, 3, figsize=(11.0, 3.6), constrained_layout=True)

    for ax, path in zip(axes, PANELS):
        image = mpimg.imread(path)
        ax.imshow(image)
        ax.axis("off")

    fig.savefig(OUT_PDF, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(OUT_PNG, dpi=220, bbox_inches="tight", pad_inches=0.02)


if __name__ == "__main__":
    setup_style()
    main()
