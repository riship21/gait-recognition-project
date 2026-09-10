from pathlib import Path
import matplotlib.pyplot as plt

from gei import generate_gei


base_path = Path(
    "data/raw/CASIA-B/GaitDatasetB-silh/001"
)

sequences = [
    "nm-01",
    "nm-02",
    "nm-03",
    "nm-04",
    "nm-05",
    "nm-06"
]

view = "090"

fig, axes = plt.subplots(2, 3, figsize=(10, 7))

for ax, sequence in zip(axes.flat, sequences):

    sequence_path = base_path / sequence / view

    gei, num_frames = generate_gei(sequence_path)

    ax.imshow(gei, cmap="gray")
    ax.set_title(f"{sequence}\n{num_frames} frames")
    ax.axis("off")

plt.suptitle("Subject 001 - Normal Walking GEIs - 090°")
plt.tight_layout()

plt.savefig(
    "results/figures/subject001_all_normal_geis.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()