from pathlib import Path
import csv
import numpy as np

from gei import generate_gei


BASE_PATH = Path(
    "data/raw/CASIA-B/GaitDatasetB-silh"
)

VIEW = "090"

GALLERY_SEQUENCES = [
    "nm-01",
    "nm-02",
    "nm-03",
    "nm-04"
]

PROBE_SEQUENCES = [
    "nm-05",
    "nm-06"
]

# Subject 005 was identified as a sequence-length outlier
EXCLUDED_SUBJECTS = {"005"}


def gei_to_feature(gei):
    """
    Convert a GEI into a normalized 1D feature vector.
    """
    return gei.astype(np.float32).flatten() / 255.0


def get_subjects():
    """
    Return valid CASIA-B subject IDs.
    """
    subjects = []

    for subject_path in sorted(BASE_PATH.iterdir()):

        if not subject_path.is_dir():
            continue

        subject = subject_path.name

        if not subject.isdigit():
            continue

        if subject in EXCLUDED_SUBJECTS:
            continue

        subjects.append(subject)

    return subjects


def build_gallery(subjects):
    """
    Generate gallery GEIs and feature vectors.
    """
    gallery_features = []
    gallery_subjects = []
    gallery_sequences = []

    print("Building gallery...")

    for subject in subjects:

        for sequence in GALLERY_SEQUENCES:

            sequence_path = (
                BASE_PATH
                / subject
                / sequence
                / VIEW
            )

            gei, _ = generate_gei(sequence_path)

            feature = gei_to_feature(gei)

            gallery_features.append(feature)
            gallery_subjects.append(subject)
            gallery_sequences.append(sequence)

    gallery_features = np.array(
        gallery_features,
        dtype=np.float32
    )

    print(
        f"Gallery contains {len(gallery_features)} samples "
        f"from {len(subjects)} subjects."
    )

    return (
        gallery_features,
        gallery_subjects,
        gallery_sequences
    )


def identify_probe(
    probe_feature,
    gallery_features,
    gallery_subjects,
    gallery_sequences
):
    """
    Find the gallery GEI with the smallest Euclidean distance.
    """

    distances = np.linalg.norm(
        gallery_features - probe_feature,
        axis=1
    )

    best_index = np.argmin(distances)

    return (
        gallery_subjects[best_index],
        gallery_sequences[best_index],
        float(distances[best_index])
    )


def run_evaluation():
    subjects = get_subjects()

    print(f"Subjects used: {len(subjects)}")

    (
        gallery_features,
        gallery_subjects,
        gallery_sequences
    ) = build_gallery(subjects)

    results = []

    correct = 0
    total = 0

    sequence_correct = {
        "nm-05": 0,
        "nm-06": 0
    }

    sequence_total = {
        "nm-05": 0,
        "nm-06": 0
    }

    print("\nEvaluating probes...")

    for subject in subjects:

        for sequence in PROBE_SEQUENCES:

            sequence_path = (
                BASE_PATH
                / subject
                / sequence
                / VIEW
            )

            gei, num_frames = generate_gei(sequence_path)

            probe_feature = gei_to_feature(gei)

            (
                predicted_subject,
                matched_sequence,
                distance
            ) = identify_probe(
                probe_feature,
                gallery_features,
                gallery_subjects,
                gallery_sequences
            )

            is_correct = predicted_subject == subject

            total += 1
            sequence_total[sequence] += 1

            if is_correct:
                correct += 1
                sequence_correct[sequence] += 1

            results.append({
                "true_subject": subject,
                "probe_sequence": sequence,
                "frames": num_frames,
                "predicted_subject": predicted_subject,
                "matched_gallery_sequence": matched_sequence,
                "distance": round(distance, 4),
                "correct": is_correct
            })

    accuracy = correct / total

    print("\nBaseline Results")
    print("----------------")
    print(f"Correct: {correct}")
    print(f"Total probes: {total}")
    print(f"Rank-1 Accuracy: {accuracy * 100:.2f}%")

    for sequence in PROBE_SEQUENCES:

        seq_accuracy = (
            sequence_correct[sequence]
            / sequence_total[sequence]
        )

        print(
            f"{sequence} Accuracy: "
            f"{seq_accuracy * 100:.2f}%"
        )

    save_results(results)

    return accuracy


def save_results(results):

    output_path = Path(
        "results/tables/baseline_predictions.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "true_subject",
        "probe_sequence",
        "frames",
        "predicted_subject",
        "matched_gallery_sequence",
        "distance",
        "correct"
    ]

    with output_path.open(
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    run_evaluation()