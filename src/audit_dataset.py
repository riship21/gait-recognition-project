from pathlib import Path
import csv
import statistics


base_path = Path(
    "data/raw/CASIA-B/GaitDatasetB-silh"
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

rows = []

for subject_path in sorted(base_path.iterdir()):

    if not subject_path.is_dir():
        continue

    subject = subject_path.name

    for sequence in sequences:
        sequence_path = subject_path / sequence / view

        if sequence_path.exists():
            frame_count = len(list(sequence_path.glob("*.png")))
        else:
            frame_count = 0

        rows.append({
            "subject": subject,
            "sequence": sequence,
            "view": view,
            "frame_count": frame_count
        })


# Save all counts
output_path = Path("results/tables/frame_counts_090.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["subject", "sequence", "view", "frame_count"]
    )
    writer.writeheader()
    writer.writerows(rows)


counts = [row["frame_count"] for row in rows if row["frame_count"] > 0]

median_count = statistics.median(counts)

print(f"Total sequences checked: {len(rows)}")
print(f"Minimum frame count: {min(counts)}")
print(f"Maximum frame count: {max(counts)}")
print(f"Median frame count: {median_count}")

print("\nSequences with less than half the median number of frames:")

for row in rows:
    if row["frame_count"] < median_count / 2:
        print(
            f"Subject {row['subject']} | "
            f"{row['sequence']} | "
            f"{row['frame_count']} frames"
        )