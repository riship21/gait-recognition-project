from pathlib import Path
import matplotlib.pyplot as plt

from gei import generate_gei


base_path = Path(
    "data/raw/CASIA-B/GaitDatasetB-silh"
)

subjects = [
    "001",
    "002",
    "003",
    "004",
    "005",
    "006"
]

sequence = "nm-01"
view = "090"

fig, axes = plt.subplots(2, 3, figsize=(10, 7))

for ax, subject in zip(axes.flat, subjects):

    sequence_path = base_path / subject / sequence / view

    gei, num_frames = generate_gei(sequence_path)

    ax.imshow(gei, cmap="gray")
    ax.set_title(f"Subject {subject}\n{num_frames} frames")
    ax.axis("off")

plt.suptitle("Different Subjects - nm-01 - 090°")
plt.tight_layout()

plt.savefig(
    "results/figures/different_subjects_gei_comparison.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()