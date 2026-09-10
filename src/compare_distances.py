from pathlib import Path
import numpy as np

from gei import generate_gei


base_path = Path(
    "data/raw/CASIA-B/GaitDatasetB-silh"
)


def gei_feature(subject, sequence, view="090"):
    sequence_path = base_path / subject / sequence / view

    gei, _ = generate_gei(sequence_path)

    # Normalize pixel values and flatten into a feature vector
    return gei.flatten() / 255.0


def euclidean_distance(feature1, feature2):
    return np.linalg.norm(feature1 - feature2)


# Same subject, different walking sequences
subject001_nm01 = gei_feature("001", "nm-01")
subject001_nm02 = gei_feature("001", "nm-02")

same_subject_distance = euclidean_distance(
    subject001_nm01,
    subject001_nm02
)


# Different subjects, same walking condition
subject002_nm01 = gei_feature("002", "nm-01")

different_subject_distance = euclidean_distance(
    subject001_nm01,
    subject002_nm01
)


print("Same-subject comparison:")
print(f"001 nm-01 vs 001 nm-02: {same_subject_distance:.4f}")

print()

print("Different-subject comparison:")
print(f"001 nm-01 vs 002 nm-01: {different_subject_distance:.4f}")

print()

if same_subject_distance < different_subject_distance:
    print("Result: Same-subject GEIs are closer, as expected.")
else:
    print("Result: Unexpected result. Further investigation is needed.")