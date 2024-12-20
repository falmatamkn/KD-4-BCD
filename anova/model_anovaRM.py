import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.anova import AnovaRM
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Create the dataframe
data = {
    'Model': ['TM', 'SM_scratch', 'SM'] * 12,
    'Dataset': ['PBCNT', 'PBCNT', 'PBCNT', 'BCD', 'BCD', 'BCD', 'WDBC', 'WDBC', 'WDBC'] * 4,
    'Oversampling': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes',
                     'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No'] * 2,
    'AccuracyType': ['Training', 'Training', 'Training', 'Training', 'Training', 'Training', 
                     'Training', 'Training', 'Training', 'Training', 'Training', 'Training', 
                     'Training', 'Training', 'Training', 'Training', 'Training', 'Training',
                     'Validation', 'Validation', 'Validation', 'Validation', 'Validation', 'Validation',
                     'Validation', 'Validation', 'Validation', 'Validation', 'Validation', 'Validation',
                     'Validation', 'Validation', 'Validation', 'Validation', 'Validation', 'Validation'] * 1,
    'Value': [1, 0.96, 1, 0.99, 0.93, 0.96, 1, 0.8, 0.96,
              1, 0.59, 1, 0.98, 0.92, 0.96, 1, 0.8, 0.95,
              0.89, 0.95, 1, 0.96, 0.95, 0.96, 0.97, 0.88, 0.97,
              0.9, 0.55, 0.95, 0.96, 0.95, 0.97, 0.94, 0.86, 0.97]
}

df = pd.DataFrame(data)

# Perform Repeated Measures ANOVA
aovrm = AnovaRM(df, 'Value', 'Dataset', within=['Model', 'Oversampling', 'AccuracyType'])
res = aovrm.fit()

print("Repeated Measures ANOVA Results:")
print(res.summary())

# Perform post-hoc tests
print("\nPost-hoc Tukey HSD test for Model:")
tukey = pairwise_tukeyhsd(df['Value'], df['Model'])
print(tukey)

# Visualize results
plt.figure(figsize=(12, 6))
sns.boxplot(x='Model', y='Value', hue='AccuracyType', data=df)
plt.title('Model Performance Comparison')
plt.savefig('model_comparison.png')
plt.close()

plt.figure(figsize=(12, 6))
sns.boxplot(x='Dataset', y='Value', hue='Model', data=df)
plt.title('Dataset Performance Comparison')
plt.savefig('dataset_comparison.png')
plt.close()

# Calculate mean accuracies
print("\nMean Accuracies:")
for model in df['Model'].unique():
    mean_acc = df[df['Model'] == model]['Value'].mean()
    print(f"{model}: {mean_acc:.4f}")

# Interaction plot
plt.figure(figsize=(12, 6))
for model in df['Model'].unique():
    model_data = df[df['Model'] == model]
    sns.lineplot(x='AccuracyType', y='Value', data=model_data, marker='o', label=model)
plt.title('Model-AccuracyType Interaction')
plt.xlabel('Accuracy Type')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('model_accuracytype_interaction.png')
plt.close()

print("\nAnalysis complete. Check the generated plots for visual representations.")
