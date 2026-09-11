 # CASIA-B Dataset Setup

The CASIA-B gait dataset is used for Project 1.

The dataset itself is not included in this repository.

## Local Dataset Location

Place the extracted silhouette dataset at:

data/raw/CASIA-B/GaitDatasetB-silh/

The expected structure is:

CASIA-B/
└── GaitDatasetB-silh/
    ├── 001/
    │   ├── nm-01/
    │   │   ├── 000/
    │   │   ├── 018/
    │   │   ├── 036/
    │   │   ├── 054/
    │   │   ├── 072/
    │   │   ├── 090/
    │   │   ├── 108/
    │   │   ├── 126/
    │   │   ├── 144/
    │   │   ├── 162/
    │   │   └── 180/
    │   ├── nm-02/
    │   ├── nm-03/
    │   ├── nm-04/
    │   ├── nm-05/
    │   ├── nm-06/
    │   ├── bg-01/
    │   ├── bg-02/
    │   ├── cl-01/
    │   └── cl-02/
    ├── 002/
    └── ...

## Project 1 Subset

The baseline experiment uses:

- View: 090 degrees
- Condition: normal walking
- Gallery sequences:
  - nm-01
  - nm-02
  - nm-03
  - nm-04
- Probe sequences:
  - nm-05
  - nm-06

Subject 005 is excluded from the main baseline evaluation because several of
its normal walking sequences contain unusually few frames.

## Notes

The dataset is stored locally under `data/raw/` and is ignored by Git.

The repository contains the code, experiment logs, results, and documentation needed to reproduce the baseline once the dataset is placed in the expected location.