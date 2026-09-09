# Vision-Based Gait Recognition

## Project 1

This project develops a baseline biometric gait recognition system.

The goal is to identify individuals based on their walking patterns using
vision-based gait representations.

## Current Research Question

Can individuals be correctly identified from normal walking sequences
using Gait Energy Images (GEIs) as a baseline gait representation?

## Biometric Modality

Gait (behavioral biometric)

## Recognition Task

Closed-set identification.

The system compares a probe gait sample against enrolled gallery samples
and predicts the identity of the closest match.

## Candidate Representations

- Gait Energy Image (GEI)
- Silhouette sequences
- 2D skeleton / pose
- Other gait representations may be investigated in later projects

## Candidate Datasets

- CASIA-B
- GREW

The final Project 1 dataset is being selected based on accessibility, available representations, and suitability for a controlled baseline.

## Current Baseline Direction

The current plan is to use silhouette sequences and Gait Energy Images (GEIs) as a simple baseline representation.

GEI is being considered because it provides a compact and interpretable representation of a walking sequence and can later be compared with more advanced gait representations.

## Baseline Pipeline

Walking Sequence
→ Silhouette Sequence
→ Preprocessing
→ Gait Representation (GEI)
→ Gallery / Probe Setup
→ Matching
→ Identity Prediction
→ Evaluation

## Relevance

Gait recognition is useful because individuals can potentially be identified from their walking behavior at a distance without requiring
direct contact with a biometric sensor.