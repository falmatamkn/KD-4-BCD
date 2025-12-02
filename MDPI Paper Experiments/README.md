# Lightweight Breast Cancer Detection Using Knowledge Distillation, Pruning, PTQ, and QAT

This repository contains all source code, experiments, and deployability evaluations used in the research study:

**“Development of a Knowledge-Distillation-Based Breast Cancer Classifier for LMICs: Comparison with Pruning and Quantization.”**

The project investigates lightweight deep learning techniques—Knowledge Distillation (KD), Pruning, Post-Training Quantization (PTQ), and Quantization-Aware Training (QAT)—to develop deployable breast cancer detection (BCD) models suitable for **resource-constrained environments** such as LMICs and embedded IoT devices.

This repository is organized into two major components:

1. **Model Python** — all model development code (training, compression, conversion).  
2. **Resource Usage Experiment** — Raspberry Pi 4B deployability tests (latency, CPU, memory, power, temperature).

Both are required to fully reproduce the results reported in the paper.

---

## 📁 Repository Structure
.
├── Model Python/
│ ├── KD/ # Knowledge Distillation training and evaluation
│ ├── Pruning/ # Magnitude-based pruning experiments
│ ├── PTQ/ # Post-Training Quantization (weight-only & integer-only)
│ └── QAT/ # Quantization-Aware Training experiments
│
└── Resource Usage Experiment/
├── KD/ # RPi deployability tests for SM_TFLite
├── Pruning/ # RPi deployability tests for TM_Prune
├── PTQ/ # RPi deployability tests for TM_PTQ & TM_PTQ_INT
└── QAT/ # RPi deployability tests for TM_QAT


---

# 📦 **Folder Descriptions**

## **📁 Model Python/**
This directory contains all **training and model-building code** used in the study.

### **KD/**
- Teacher Model (TM) and Student Model (SM) implementations  
- Distillation loss, temperature scaling, and α-weighting  
- Ablation study scripts  
- Cross-validation experiments  
- TFLite conversion of SM (SM_TFLite)

### **Pruning/**
- Magnitude-based pruning using `tfmot.sparsity.keras.prune_low_magnitude()`  
- Fine-tuning and evaluation scripts  
- Keras and TFLite versions of pruned models  

### **PTQ/**
- Weight-only quantization (`Optimize.DEFAULT`)  
- Integer-only quantization  
- Scripts for model conversion and accuracy evaluation  
- Visualization notebook for TFLite operator/buffer structure

### **QAT/**
- Quantization-Aware Training pipeline  
- Custom Keras quantizers + layer annotation  
- Fake quantization + TFLite export  
- Accuracy and file-size evaluation scripts

---

## **📁 Resource Usage Experiment/**
This directory contains **all Raspberry Pi 4B deployability experiments**, used to evaluate:

- Inference latency  
- CPU usage  
- Memory usage  
- Temperature  
- Power consumption  

### **Folder contents (each KD/Pruning/PTQ/QAT folder contains):**

#### **1. `*.ipynb`** — Full experiment notebook  
Runs the deployability pipeline:  
- Load model  
- Load dataset sample  
- Measure inference latency  
- Monitor CPU, RAM, temperature  
- Save results to `/results`

#### **2. `files/`**
- Keras (`.keras`, `.h5`) model files  
- TFLite (`.tflite`) optimized models  
- Intermediate files from compression/conversion

#### **3. `results/`**
Stores:
- Latency logs  
- Power measurements  
- CPU/memory traces  
- Temperature logs  
- Plots and figures  

#### **4. `evaluating_*.py`**
Python scripts that evaluate:
- Model load time  
- Tensor access time  
- Input preparation time  
- Single-sample inference latency  

#### **5. `sys_mon.py`**
Continuous system monitor logging:
- CPU %  
- RAM %  
- CPU temperature  

Outputs to a text file for graphing and analysis.

---

---

# 📚 **Citation**

If you use this repository, please cite:

@article{modu2025knowledge,
title = {Development of a Knowledge-Distillation-Based Breast Cancer Classifier for LMICs: Comparison with Pruning and Quantization},
author = {Modu, Falmata and Prasad, Rajesh and Aliyu, Farouq},
journal = {Electronics},
year = {2025},
volume = {1},
number = {0},
doi = {10.3390/electronics1010000},
note = {Submitted version}
}



---

# 📝 **Notes**

- Datasets are **not included** — download them from Kaggle (links in the paper).  
- All TFLite experiments use **CPU-only mode** with **XNNPACK** enabled.  
- The resource-usage tests replicate the conditions reported in Section 6 of the paper.

---
