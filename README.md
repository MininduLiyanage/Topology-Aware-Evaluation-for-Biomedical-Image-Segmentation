# Topology-Aware-Evaluation-for-Biomedical-Image-Segmentation
This repository contains the 2D topology-aware evaluation framework introduced in our paper:

Beyond Overlap: Topology-Aware Evaluation for Biomedical Image Segmentation
Accepted at ICIIS 2025

The code in this repository focuses on 2D retinal vessel segmentation evaluation, where we analyze continuity and topology preservation beyond conventional pixel-wise metrics.

## What is Included in This Repository

✔ 2D retinal vessel evaluation on the DRIVE dataset

✔ Implementation of:
  - Betti number and clDice-based connectivity analysis
  - Chamfer distance for spatial discontinuity analysis
    
✔ Evaluation of three segmentation frameworks:
  - M2U-Net
  - DRIU
  - ERFNet
    
✔ Comparison of  Pixel-wise metrics with  Continuity and Topology-aware metrics

✔ Scripts for metric computation, comparison, and visualization

This repository supports the 2D experimental results and tables reported in the paper.

## 3D Evaluation

The 3D topology-aware and continuity evaluation for mandibular canal segmentation (CBCT volumes) is implemented in a separate repository, due to its dependence on volumetric processing pipelines and dataset-specific preprocessing.
