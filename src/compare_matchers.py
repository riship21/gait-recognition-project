from pathlib import Path
import csv
import numpy as np

from gei import generate_gei
from baseline_identification import (
    BASE_PATH,
    VIEW,
    GALLERY_SEQUENCES,
    PROBE_SEQUENCES,
    get_subjects,
    build_gallery,
    gei_to_feature
)


def euclidean_match(probe_feature, gallery_features):
    distances = np.linalg.norm(
        gallery_features - probe_feature,
        axis=1
    )

    best_index = np.argmin(distances)

    return best_index, float(distances[best_index])


def cosine_match(probe_feature, gallery_features):
    probe_norm = np.linalg.norm(probe_feature)

    gallery_norms = np.linalg.norm(
        gallery_features,
        axis=1
    )

    similarities = (
        gallery_features @ probe_feature
    ) / (gallery_norms * probe_norm + 1e-10)

    best_index = np.argmax(similarities)

    return best_index, float(similarities[best_index])


def run_comparison():

    subjects = get_subjects()

    print(f"Subjects used: {len(subjects)}")

    (
        gallery_features,
        gallery_subjects,
        gallery_sequences
    ) = build_gallery(subjects)

    euclidean_correct = 0
    cosine_correct = 0
    total = 0

    results = []

    print("\nEvaluating probes with both matchers...")

    for subject in subjects:

        for sequence in PROBE_SEQUENCES:

            sequence_path = (
                BASE_PATH
                / subject
                / sequence
                / VIEW
            )

            gei, _ = generate_gei(sequence_path)

            probe_feature = gei_to_feature(gei)

            # Euclidean
            euclidean_index, euclidean_distance = euclidean_match(
                probe_feature,
                gallery_features
            )

            euclidean_prediction = gallery_subjects[
                euclidean_index
            ]

            # Cosine
            cosine_index, cosine_similarity = cosine_match(
                probe_feature,
                gallery_features
            )

            cosine_prediction = gallery_subjects[
                cosine_index
            ]

            euclidean_is_correct = (
                euclidean_prediction == subject
            )

            cosine_is_correct = (
                cosine_prediction == subject
            )

            if euclidean_is_correct:
                euclidean_correct += 1

            if cosine_is_correct:
                cosine_correct += 1

            total += 1

            results.append({
                "true_subject": subject,
                "probe_sequence": sequence,

                "euclidean_prediction":
                    euclidean_prediction,

                "euclidean_distance":
                    round(euclidean_distance, 4),

                "euclidean_correct":
                    euclidean_is_correct,

                "cosine_prediction":
                    cosine_prediction,

                "cosine_similarity":
                    round(cosine_similarity, 4),

                "cosine_correct":
                    cosine_is_correct
            })

    euclidean_accuracy = (
        euclidean_correct / total
    ) * 100

    cosine_accuracy = (
        cosine_correct / total
    ) * 100

    print("\nMatcher Comparison")
    print("------------------")

    print(
        f"Euclidean: "
        f"{euclidean_correct}/{total} "
        f"({euclidean_accuracy:.2f}%)"
    )

    print(
        f"Cosine:    "
        f"{cosine_correct}/{total} "
        f"({cosine_accuracy:.2f}%)"
    )

    save_results(results)

    if cosine_accuracy > euclidean_accuracy:
        print("\nCosine similarity performed better.")

    elif euclidean_accuracy > cosine_accuracy:
        print("\nEuclidean distance performed better.")

    else:
        print("\nBoth matchers achieved the same accuracy.")


def save_results(results):

    output_path = Path(
        "results/tables/matcher_comparison.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "true_subject",
        "probe_sequence",
        "euclidean_prediction",
        "euclidean_distance",
        "euclidean_correct",
        "cosine_prediction",
        "cosine_similarity",
        "cosine_correct"
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

    print(
        f"\nResults saved to: {output_path}"
    )


if __name__ == "__main__":
    run_comparison()