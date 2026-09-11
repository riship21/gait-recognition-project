import csv
from pathlib import Path


results_path = Path(
    "results/tables/baseline_predictions.csv"
)

incorrect = []

with results_path.open("r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["correct"] == "False":
            incorrect.append(row)


print(f"Total incorrect matches: {len(incorrect)}")
print()

for row in incorrect:
    print(
        f"True Subject: {row['true_subject']} | "
        f"Probe: {row['probe_sequence']} | "
        f"Predicted: {row['predicted_subject']} | "
        f"Matched Gallery: {row['matched_gallery_sequence']} | "
        f"Distance: {row['distance']}"
    )