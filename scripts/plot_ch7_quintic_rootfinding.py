from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_PDF = ROOT / "figures" / "chap6_quintic_rootfinding.pdf"
OUT_PNG = ROOT / "figures" / "chap6_quintic_rootfinding.png"


def setup_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 11,
            "mathtext.fontset": "stix",
            "font.family": "DejaVu Serif",
            "axes.linewidth": 1.0,
        }
    )


def poly(z: np.ndarray) -> np.ndarray:
    return z**5 - z - 1


def dpoly(z: np.ndarray) -> np.ndarray:
    return 5 * z**4 - 1


def newton_path(z0: complex, steps: int = 12) -> np.ndarray:
    path = [complex(z0)]
    z = complex(z0)
    for _ in range(steps):
        dz = dpoly(z)
        if abs(dz) < 1e-12:
            break
        z = z - poly(z) / dz
        path.append(z)
        if abs(poly(z)) < 1e-12:
            break
    return np.array(path, dtype=np.complex128)


def closest_root_index(z: complex, roots: np.ndarray) -> int:
    return int(np.argmin(np.abs(roots - z)))


def main() -> None:
    roots = np.roots([1, 0, 0, 0, -1, -1])

    x = np.linspace(-1.45, 1.45, 520)
    y = np.linspace(-1.45, 1.45, 520)
    xx, yy = np.meshgrid(x, y)
    zz = xx + 1j * yy
    vals = np.log10(np.abs(poly(zz)) + 1e-8)

    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.9), constrained_layout=True)

    ax0 = axes[0]
    im = ax0.contourf(xx, yy, vals, levels=32, cmap="cividis")
    ax0.contour(xx, yy, vals, levels=np.linspace(-2.0, 0.8, 8), colors="white", linewidths=0.45, alpha=0.55)
    ax0.scatter(roots.real, roots.imag, s=42, facecolors="none", edgecolors="white", linewidths=1.4, zorder=4)
    ax0.scatter(roots.real, roots.imag, s=18, color="#d94841", zorder=5)
    ax0.set_aspect("equal")
    ax0.set_xlim(-1.45, 1.45)
    ax0.set_ylim(-1.45, 1.45)
    ax0.set_xlabel(r"$\mathrm{Re}(z)$")
    ax0.set_ylabel(r"$\mathrm{Im}(z)$")
    ax0.text(0.03, 0.97, "(a)", transform=ax0.transAxes, ha="left", va="top")

    cbar = fig.colorbar(im, ax=ax0, fraction=0.048, pad=0.02)
    cbar.set_label(r"$\log_{10}|p(z)|$")

    ax1 = axes[1]
    seed_radii = [1.25, 0.9, 0.55]
    seed_angles = np.deg2rad(np.arange(0, 360, 30))
    seeds = []
    for radius in seed_radii:
        for angle in seed_angles:
            seeds.append(radius * np.exp(1j * angle))
    colors = ["#d94841", "#2f7fc1", "#3aa56d", "#8f63c7", "#c8891f"]

    for seed in seeds:
        path = newton_path(seed, steps=14)
        root_id = closest_root_index(path[-1], roots)
        ax1.plot(path.real, path.imag, color=colors[root_id], linewidth=1.0, alpha=0.78)
        ax1.scatter(path.real[0], path.imag[0], s=8, color=colors[root_id], alpha=0.55)

    ax1.scatter(roots.real, roots.imag, s=52, facecolors="white", edgecolors="#222222", linewidths=0.8, zorder=4)
    ax1.scatter(roots.real, roots.imag, s=18, color="#222222", zorder=5)
    ax1.set_aspect("equal")
    ax1.set_xlim(-1.45, 1.45)
    ax1.set_ylim(-1.45, 1.45)
    ax1.set_xlabel(r"$\mathrm{Re}(z)$")
    ax1.set_ylabel(r"$\mathrm{Im}(z)$")
    ax1.text(0.03, 0.97, "(b)", transform=ax1.transAxes, ha="left", va="top")

    for ax in axes:
        ax.axhline(0.0, color="#444444", linewidth=0.5, alpha=0.35)
        ax.axvline(0.0, color="#444444", linewidth=0.5, alpha=0.35)

    fig.savefig(OUT_PDF, bbox_inches="tight", pad_inches=0.02)
    fig.savefig(OUT_PNG, dpi=220, bbox_inches="tight", pad_inches=0.02)


if __name__ == "__main__":
    setup_style()
    main()
