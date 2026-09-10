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