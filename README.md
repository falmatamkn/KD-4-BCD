# KD-4-BCD
This project contains code (in Jupyter Notebook format) for Breast Cancer Detection (BCD) using Knowledge Distillation (KD) technique.

## Datasets: 
1. Primary breast cancer vs Normal breast tissue (PBCNT) (https://www.kaggle.com/datasets/rhostam/primary-breast-cancer-vs-normal-breast-tissue) [1].
2. Wisconsin Breast Cancer Database (BCD) (https://www.kaggle.com/datasets/roustekbio/breast-cancer-csv) [2,3].
3. Breast Cancer Wisconsin (Diagnostic) Data Set (WDBCD) (https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) [4].

## Folders
1. *ANOVA:* The folder contains the code for calculating the Analysis of Variation for the 3 databases on the validation and the training accuracy. We used the 3x2x2 factorial design to test the Teacher model (TM), the Student Model (SM) with KD, and SM_scratch which is an SM without KD technique. There is an Excel file with the data we obtained.
2. *BCD:* This folder contains two Jupyter Notebooks, BCD-KD, and BCD-KD-O that train on the BCD dataset. The BCD-KD-O code uses oversampling to increase the dataset's size, while BCD-KD does not.
3. *PBCNT:* This folder contains two Jupyter Notebooks, SM2-PBCNT, and SM2-PBCNT-O that train on the PBCNT dataset. The SM2-PBCNT-O code uses oversampling to increase the dataset's size, while SM2-PBCNT does not.
4. *WDBC:* The uploaded folder contains code for testing Breast Cancer Wisconsin (Diagnostic) Data Set with oversampling and without it, WDBC-KD and WDBC-KD-O, respectively. There is a third code (WDBC-KD-10-FOLD) that uses 10-fold validation without oversampling.

## References
1. Matamala N, Vargas MT, González-Cámpora R, Miñambres R et al. Tumor microRNA expression profiling identifies circulating microRNAs for early breast cancer detection. Clin Chem 2015 Aug; 61(8):1098-106. PMID: 26056355
2. Wolberg, W. H., \& Mangasarian, O. L. (1990). Multisurface method of pattern separation for medical diagnosis applied to breast cytology. In *Proceedings of the National Academy of Sciences*, *87*, 9193--9196.
3. Zhang, J. (1992). Selecting typical instances in instance-based learning. In *Proceedings of the Ninth International Machine Learning Conference* (pp. 470--479). Aberdeen, Scotland: Morgan Kaufmann.
4. K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34
