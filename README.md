# Vision-Based Gait Recognition

## Author

Rishi Patel  
COSC 594 - Biometrics  
University of Tennessee

## Project 1 - Baseline Biometric System

This project develops a baseline biometric gait recognition system.

The goal is to identify individuals based on their walking patterns using vision-based gait representations.

## Research Question

Can individuals be correctly identified from normal walking sequences using Gait Energy Images (GEIs) as a baseline gait representation?

## Biometric Modality

Gait (behavioral biometric)

## Recognition Task

Closed-set identification.

The system compares a probe gait sample against enrolled gallery samples and predicts the identity of the closest match.

## Dataset

The project uses the CASIA-B gait dataset.

For the Project 1 baseline:

- View: 090 degrees
- Condition: normal walking
- Gallery sequences: nm-01, nm-02, nm-03, nm-04
- Probe sequences: nm-05, nm-06
- Subjects used: 123

Subject 005 was excluded from the main evaluation because several of its
normal walking sequences contained unusually few frames.

The CASIA-B dataset itself is not included in this repository.

Dataset setup instructions are listed under `data/README.md` 

## Baseline Representation

The baseline uses Gait Energy Images (GEIs).

A GEI is created by averaging the preprocessed silhouette frames from a walking sequence into a single image.

GEI was selected because it is simple, interpretable, computationally inexpensive, and provides a useful baseline for comparison with more advanced gait representations in later projects.

## Baseline Pipeline

Walking Sequence → Silhouette Sequence → Preprocessing → Gait Energy Image (GEI) → Feature Vector
→ Gallery / Probe Matching → Euclidean Distance → Identity Prediction → Rank-1 Evaluation

## Preprocessing

Each silhouette frame is:

1. Cropped using its foreground bounding box
2. Resized while preserving aspect ratio
3. Centered on a 128 x 128 canvas

This reduces variation caused by the subject moving across the original video frame.

## Feature Representation

Each 128 x 128 GEI is flattened into a 16,384-dimensional feature vector.

The feature values are normalized before matching.

## Matching

The final baseline uses nearest-neighbor matching with Euclidean distance.

For each probe sample, the system compares its GEI feature vector against all gallery samples and selects the subject with the smallest distance.

## Evaluation

The primary evaluation metric is Rank-1 identification accuracy.

### Final Baseline Results

- Correct identifications: 236 / 246
- Rank-1 accuracy: 95.93%
- nm-05 accuracy: 95.12%
- nm-06 accuracy: 96.75%

## Matcher Comparison

Two matching approaches were compared using the same dataset,
preprocessing, representation, and gallery split.

Euclidean distance performed slightly better and was kept as the final
baseline matcher.

## Relevance

Gait recognition is useful because individuals can potentially be identified
from their walking behavior at a distance without requiring direct contact
with a biometric sensor.

## Experiments

The development and evolution of the baseline system is documented in:

`experiments/experiment_log.md`

The experiments include dataset inspection, preprocessing, GEI generation, same-subject and different-subject comparisons, dataset quality analysis, distance comparison, baseline identification, error analysis, and matcher comparison.

## Limitations
The Project 1 baseline intentionally focuses on a controlled configuration:

One viewing angle: 090°
Normal walking sequences only
Simple GEI representation
Simple distance-based matching

These limitations provide directions for future investigation in Projects 2 and 3.

## AI Assistance

ChatGPT (OpenAI) was used as a supporting tool during this project.

AI assistance was mainly used for:

- Improving grammar and flow in the written documentation
- Reviewing and improving parts of the Python code
- Helping debug implementation issues
- Discussing project organization and possible approaches

The project decisions, experimentation, implementation, evaluation, and final results were all completed and reviewed by the author.