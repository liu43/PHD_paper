from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle


ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "figures" / "chap2_residue_path.pdf"
OUT_PNG = ROOT / "figures" / "chap2_residue_path.png"


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 12,
            "mathtext.fontset": "stix",
            "font.family": "DejaVu Serif",
            "axes.linewidth": 1.2,
        }
    )


def add_arrow(ax, start, end, color, lw=1.4, ms=20):
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            mutation_scale=ms,
            shrinkA=0,
            shrinkB=0,
        ),
    )


def main() -> None:
    fig, ax = plt.subplots(figsize=(8.2, 5.0))
    ax.set_aspect("equal")
    ax.axis("off")

    a = 4.8
    eps = 1.0
    big_r = 4.8
    small_r = 1.0

    blue = "#3b6ec2"
    green = "#1fa463"
    axis = "#222222"
    purple = "#7b3fb3"

    # axes
    ax.plot([-5.8, 6.2], [0, 0], color=axis, lw=1.2)
    ax.plot([0, 0], [-2.0, 5.7], color=axis, lw=1.0, alpha=0.6)
    add_arrow(ax, (5.9, 0), (6.25, 0), axis, lw=1.2, ms=18)
    add_arrow(ax, (0, 5.35), (0, 5.75), axis, lw=1.2, ms=18)

    # contour pieces
    ax.add_patch(Arc((0, 0), 2 * big_r, 2 * big_r, theta1=0, theta2=180, color=blue, lw=3.0))
    ax.add_patch(Arc((0, 0), 2 * small_r, 2 * small_r, theta1=0, theta2=180, color=blue, lw=3.0))
    ax.plot([-a, -eps], [0, 0], color=green, lw=3.0)
    ax.plot([eps, a], [0, 0], color=green, lw=3.0)

    # singular point
    ax.add_patch(Circle((0, 0), 0.12, color=purple, zorder=5))

    # arrows along L2: from right to left over upper semicircle
    add_arrow(ax, (3.35, 3.4), (2.95, 3.95), blue, lw=2.0, ms=22)
    add_arrow(ax, (-3.35, 3.4), (-2.95, 3.95), blue, lw=2.0, ms=22)

    # arrows along L1: from left to right over upper small semicircle
    add_arrow(ax, (-0.45, 0.55), (0.02, 0.98), blue, lw=1.9, ms=18)

    # arrows along real axis segments
    add_arrow(ax, (-3.0, -0.55), (-2.3, 0.0), green, lw=1.8, ms=18)
    add_arrow(ax, (2.3, 0.0), (3.0, -0.55), green, lw=1.8, ms=18)

    ax.set_xlim(-6.3, 6.6)
    ax.set_ylim(-2.05, 6.0)

    fig.tight_layout(pad=0.1)
    fig.savefig(OUT_PDF, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(OUT_PNG, dpi=220, bbox_inches="tight", pad_inches=0.02)


if __name__ == "__main__":
    setup_style()
    main()
