# Knowledge-Distillation-Based Breast Cancer Classifier for LMICs

This repository contains the Python scripts and notebooks used to conduct the experiments described in the paper:

**"Development of a Knowledge-Distillation-Based Breast Cancer Classifier for LMICs: Comparison with Pruning and Quantization."**

The project evaluates several lightweight machine-learning techniques—including Knowledge Distillation (KD), Pruning, Post-Training Quantization (PTQ), Quantization-Aware Training (QAT), and cross-dataset generalization—on three breast cancer datasets (WDBC, BCDD, PBCNT).  
Each folder corresponds to a specific set of experiments reported in the paper.

---

## 📁 Folder Structure

### `KD/`
Contains Python scripts for training the Teacher Model (TM), Student Model (SM), and Student-from-Scratch (SM_Scratch) using the Knowledge Distillation (KD) framework.  
Includes the KD loss formulation, distiller class, and training/evaluation procedures described in Section 6.2.

### `Prune/`
Contains code for applying magnitude-based pruning to the Teacher Model.  
Reproduces the experiments in Section 6.4, including:
- pruning configuration  
- fine-tuning  
- evaluation  
- deployability tests  

### `PTQ/`
Includes scripts for:
- Weight-only Post-Training Quantization (TM_PTQ)  
- Full-integer PTQ (TM_PTQ_INT)

Reproduces results in Section 6.5, covering accuracy, file-size reduction, and Raspberry Pi deployability.

### `QAT/`
Contains Python code for Quantization-Aware Training (TM_QAT).  
Implements custom quantizers, layer annotation, fake quantization, and TFLite conversion as described in Section 6.6.

### `Cross Dataset/`
Scripts for the cross-dataset generalization experiment in Section 6.2.4  
(models trained on WDBC and tested on BCDD).

### `tflite_visualization.ipynb`
Notebook for analyzing TFLite model structure (operators, buffers, metadata).  
Used to interpret file-size differences between TM_PTQ and TM_PTQ_INT.

---

## 📄 Note
This repository contains only the experimental code.  
Datasets must be downloaded separately from their original sources (as referenced in the manuscript).

---

## 📚 Citation

If you use this repository, please cite the following paper:

