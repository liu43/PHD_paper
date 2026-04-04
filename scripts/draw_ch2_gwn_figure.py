from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Ellipse, Polygon


ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "figures" / "chap2_gwn_projection.pdf"
OUT_PNG = ROOT / "figures" / "chap2_gwn_projection.png"


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 12,
            "mathtext.fontset": "stix",
            "font.family": "DejaVu Serif",
            "axes.linewidth": 1.2,
        }
    )


def draw_left(ax) -> None:
    ax.set_aspect("equal")
    ax.axis("off")

    p = (0.0, 0.0)
    ci = (1.55, -0.55)
    cip1 = (1.45, 0.75)

    region = Polygon(
        [
            ci,
            cip1,
            (1.85, 1.18),
            (-0.10, 1.12),
            (-0.75, 0.20),
            (-0.45, -1.05),
            (1.05, -1.12),
        ],
        closed=True,
        facecolor="#efb394",
        edgecolor="black",
        linewidth=1.4,
        joinstyle="round",
    )
    ax.add_patch(region)

    ax.add_patch(Circle(p, 0.72, facecolor="none", edgecolor="#9a9a9a", linewidth=1.2))
    ax.plot(*p, "ko", ms=4)

    ax.plot([p[0], ci[0]], [p[1], ci[1]], color="black", lw=1.0)
    ax.plot([p[0], cip1[0]], [p[1], cip1[1]], color="black", lw=1.0)

    ax.annotate(
        "",
        xy=(1.48, 0.25),
        xytext=(1.52, -0.12),
        arrowprops=dict(arrowstyle="-|>", lw=1.2, color="black", shrinkA=0, shrinkB=0),
    )

    theta1 = -19
    theta2 = 28
    ax.add_patch(Arc(p, 0.86, 0.86, angle=0, theta1=theta1, theta2=theta2, linewidth=1.2))

    ax.set_xlim(-1.15, 2.45)
    ax.set_ylim(-1.35, 1.45)


def draw_right(ax) -> None:
    ax.set_aspect("equal")
    ax.axis("off")

    p = (-0.10, -0.78)
    vi = (-1.22, -0.55)
    vj = (-0.78, 1.00)
    vk = (0.16, 0.42)

    tri = Polygon(
        [vi, vj, vk],
        closed=True,
        facecolor="#efb394",
        edgecolor="black",
        linewidth=1.4,
        joinstyle="round",
    )
    ax.add_patch(tri)

    for vx, vy in (vi, vj, vk):
        ax.plot([p[0], vx], [p[1], vy], color="#5a5a5a", lw=1.0)

    sphere_center = (0.95, -0.05)
    ax.add_patch(Circle(sphere_center, 0.82, facecolor="none", edgecolor="#9a9a9a", linewidth=1.2))
    ax.add_patch(Ellipse(sphere_center, 1.64, 0.48, facecolor="none", edgecolor="#9a9a9a", linewidth=1.0))

    spherical_patch = Polygon(
        [(0.36, -0.18), (0.72, 0.50), (1.34, 0.23)],
        closed=True,
        facecolor="#efb394",
        edgecolor="black",
        linewidth=1.0,
        alpha=0.95,
    )
    ax.add_patch(spherical_patch)

    ax.plot(*p, "ko", ms=4)

    ax.set_xlim(-1.65, 1.95)
    ax.set_ylim(-1.25, 1.35)


def main() -> None:
    setup_style()
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.0))
    draw_left(axes[0])
    draw_right(axes[1])

    fig.tight_layout(pad=0.4, w_pad=1.0)
    fig.savefig(OUT_PDF, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(OUT_PNG, dpi=220, bbox_inches="tight", pad_inches=0.02)


if __name__ == "__main__":
    main()
