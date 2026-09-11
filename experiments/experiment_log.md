## Experiment 1 - CASIA-B Sequence Inspection

### Goal
Inspect a real CASIA-B silhouette sequence and confirm that the dataset
is suitable for the gait recognition baseline.

### Sample
- Subject: 001
- Condition: nm-01
- View: 090°
- Frames: 56

### Observation
The sequence contains clear silhouette images showing different stages
of the subject's walking motion.

The subject also changes position across the image as they walk.
Therefore, the silhouettes should be cropped, resized, and aligned
before generating a Gait Energy Image (GEI).

### Next Step
Develop a simple preprocessing method to normalize the silhouette
frames before creating the first GEI.


## Experiment 2 - Silhouette Preprocessing

### Goal
Normalize silhouette frames before generating a Gait Energy Image (GEI).

### Method
Each silhouette frame was:
- cropped using the foreground bounding box
- resized while preserving aspect ratio
- centered on a fixed 128 x 128 canvas

### Observation
The original CASIA-B silhouettes show the subject moving across the frame.
After preprocessing, the subject appears more consistently centered and scaled.

### Conclusion
Preprocessing is necessary before averaging frames into a GEI.

### Next Step
Generate the first GEI from the preprocessed silhouette sequence.


## Experiment 3 - Initial GEI Generation

### Goal
Generated a Gait Energy Image (GEI) from a CASIA-B walking sequence.

### Sample
- Subject: 001
- Condition: nm-01
- View: 090°
- Frames used: 56

### Method
Each silhouette frame was cropped, resized, and centered on a 128 x 128 canvas. The processed frames were then averaged pixel wise to create the GEI.

### Result
A 128 x 128 GEI was successfully generated from all 56 frames.

### Observation
More stable body regions, such as the torso, appear brighter. Moving regions, especially the arms and legs, appear more spread out because their positions change throughout the walking sequence.

### Next Step
Generate GEIs for multiple walking sequences and compare whether samples from the same subject produce similar gait representations.


## Experiment 4 - Compare GEIs across same-subject walking sequences

### Observation

The six GEIs from Subject 001 are visually similar even though the
walking sequences contain different numbers of frames.

The main body shape remains consistent across the sequences, while
small differences appear around the arms and legs due to natural
variation in the walking motion.

This suggests that GEI captures relatively consistent gait information
for the same subject.

### Next Step

Generate GEIs from different subjects and compare them to determine
whether there is enough inter-class variation for identification.


## Experiment 5 - Compare GEIs across different-subject walking sequences

### Observation

The GEIs from different subjects show visible differences in body shape
and walking motion, which suggests useful inter-class variation.

Most sequences contained approximately 47 to 68 frames. Subject 005,
however, contained only 16 frames and produced a noticeably different
and less stable GEI. This suggests that sequence length may affect the
quality of the GEI representation and should be considered during
evaluation.

### Next Step

Inspect the unusually short Subject 005 sequence and then quantitatively
compare same-subject and different-subject GEIs using distance scores.


## Experiment 6 - Dataset Quality Audit

### Goal

Determine whether the unusually short sequences observed for Subject 005
also occur for other subjects.

### Method

Frame counts were calculated for all six normal walking sequences
(nm-01 through nm-06) at the 090° view for all 124 subjects.

### Result

A total of 744 sequences were checked.

- Median frame count: 60
- Minimum frame count: 3
- Maximum frame count: 86

The only sequences containing fewer than 30 frames belonged to
Subject 005:

- nm-01: 16 frames
- nm-02: 11 frames
- nm-03: 6 frames
- nm-04: 9 frames
- nm-06: 3 frames

### Conclusion

Subject 005 is a clear frame-count outlier in the 090° normal walking
data. For the main Project 1 baseline, Subject 005 will be excluded so
that unreliable GEIs from extremely short sequences do not affect the
evaluation.

### Next Step

Quantitatively compare same-subject and different-subject GEIs using
distance scores.


## Experiment 7 - Quantitative GEI Distance Comparison

### Goal

Verify that GEIs from the same subject are numerically more similar
than GEIs from different subjects.

### Method

Euclidean distance was calculated between:

- Subject 001 nm-01 and Subject 001 nm-02
- Subject 001 nm-01 and Subject 002 nm-01

### Result

- Same-subject distance: 4.2740
- Different-subject distance: 9.4212

The same-subject GEIs had a smaller Euclidean distance than the different-subject GEIs.

### Conclusion

This supports the use of Euclidean distance as a simple matching method for the baseline gait identification system.

### Next Step

Build the full gallery/probe identification system and evaluate it across the CASIA-B subjects.


## Experiment 8 - Baseline Gait Identification

### Goal
Evaluate a complete closed-set gait identification system using GEIs.

### Setup
- Dataset: CASIA-B
- View: 090°
- Condition: normal walking
- Subjects used: 123
- Excluded subject: 005
- Gallery: nm-01 through nm-04
- Probe: nm-05 and nm-06
- Representation: GEI
- Matcher: Euclidean distance
- Metric: Rank-1 identification accuracy

### Result
- Correct identifications: 236 / 246
- Rank-1 accuracy: 95.93%
- nm-05 accuracy: 95.12%
- nm-06 accuracy: 96.75%

### Conclusion
The GEI-based baseline performs well under controlled normal-walking conditions.
The result shows that the representation and simple distance-based matcher are sufficient for a functional baseline biometric system.

### Next Step
Inspect the incorrect matches and perform one small baseline comparison or improvement before finalizing Project 1.