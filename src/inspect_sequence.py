from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

sequence_path = Path("data/raw/CASIA-B/GaitDatasetB-silh/001/nm-01/090")

frames = sorted(sequence_path.glob("*.png"))

print(f"Number of frames: {len(frames)}")

if not frames:
    raise FileNotFoundError(f"No PNG frames found in {sequence_path}")

# Selected few frames spread across the sequence
indices = [0, len(frames) // 4, len(frames) // 2,
           3 * len(frames) // 4, len(frames) - 1]

selected_frames = [frames[i] for i in indices]

fig, axes = plt.subplots(1, len(selected_frames), figsize=(12, 3))

for ax, frame_path in zip(axes, selected_frames):
    image = Image.open(frame_path)

    ax.imshow(image, cmap="gray")
    ax.set_title(frame_path.name)
    ax.axis("off")

plt.tight_layout()

plt.savefig(
    "results/figures/subject001_sequence.png",
    dpi=150,
    bbox_inches="tight"
)

plt.show()