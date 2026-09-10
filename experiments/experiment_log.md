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