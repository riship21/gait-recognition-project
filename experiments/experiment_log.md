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