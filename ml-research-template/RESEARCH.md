# ML Research Publication Guide

## Structure of a Research Project

### 1. Problem Definition & Motivation
- **What**: Clear problem statement
- **Why**: Motivation and significance
- **How**: Proposed approach overview
- **Expected Impact**: Potential contributions

### 2. Literature Review
Synthesize existing work:
- State-of-the-art methods
- Gaps your research addresses
- Novel contributions
- Positioning relative to prior work

### 3. Methodology
Include:
- Dataset description (source, size, statistics, splits)
- Preprocessing steps and justification
- Feature engineering approach
- Model architecture and hyperparameters
- Training procedure (loss, optimizer, epochs)
- Evaluation metrics and validation strategy

### 4. Results & Analysis

#### Main Results Table
Include:
- Model name/configuration
- Performance metrics (accuracy, F1, AUC, etc.)
- Comparison to baselines
- Statistical significance tests
- Confidence intervals

#### Ablation Studies
- Remove components one-at-a-time
- Show contribution of each component
- Support design decisions

#### Error Analysis
- What does the model get wrong?
- Common failure modes
- Examples of edge cases

### 5. Figures & Visualization Guidelines

**Publication-Quality Figures:**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# Save as PDF for publication
fig.savefig('figure.pdf', dpi=300, bbox_inches='tight')
```

**Essential Figures:**
1. **Data Distribution** - Show class balance, feature distributions
2. **Model Architecture** - Diagram of your approach
3. **Training Curves** - Loss and metrics over epochs
4. **Confusion Matrix** - Classification performance breakdown
5. **Feature Importance** - Top features contributing to predictions
6. **Comparison Plot** - Your model vs baselines
7. **Learning Curves** - Performance vs training set size
8. **Failure Examples** - Worst predictions with analysis

### 6. Tables for Papers

**Model Performance Table:**
```
| Model | Accuracy | F1 | AUC | Params | Training Time |
|-------|----------|-----|-----|--------|--------------|
| Baseline | 85.2 | 0.81 | 0.88 | 1M | 2h |
| Proposed | 91.4* | 0.89 | 0.93 | 2.5M | 3h |
```

*Note: * indicates statistical significance p < 0.05

### 7. Reproducibility Checklist

- [ ] Random seeds fixed in all places
- [ ] Dependencies in requirements.txt with pinned versions
- [ ] .env.example provided with all needed variables
- [ ] Data loading script documented
- [ ] Preprocessing steps fully reproducible
- [ ] Model checkpoints saved
- [ ] Evaluation metrics calculated consistently
- [ ] Hardware specs documented (GPU model, RAM, etc.)
- [ ] Training time and compute requirements noted

### 8. Code & Documentation

**For researchers/developers to use your work:**

```python
"""
Docstring format for publication quality:

Parameters
----------
X : array-like of shape (n_samples, n_features)
    Input features
y : array-like of shape (n_samples,)
    Target labels

Returns
-------
predictions : array-like of shape (n_samples,)
    Model predictions
confidence : array-like of shape (n_samples,)
    Prediction confidence scores

Examples
--------
>>> from src.models import MyModel
>>> model = MyModel()
>>> predictions = model.predict(X_test)
"""
```

### 9. Citation Format

For your published research:

**BibTeX:**
```bibtex
@article{YourName2026,
  title={Your Research Title},
  author={Your Name and Collaborators},
  journal={Journal Name},
  year={2026},
  volume={XX},
  pages={XX--XX}
}
```

### 10. GitHub/GitLab Considerations

**README should include:**
- Quick start command
- Data download instructions
- Results reproduction guide
- Citation format
- Contact/questions section

**Do NOT commit:**
- Large datasets (use .gitignore)
- Model checkpoints (> 100MB)
- Raw outputs (results are generated)
- API keys (.env files)

### 11. Data Documentation

Create a data dictionary:

```
feature_name, type, description, null_count, unique_values
age, int, Age in years, 0, 85
income, float, Annual income in USD, 42, 5000
class, categorical, Target variable, 0, 2
```

### 12. Experimental Setup

Document in code:

```python
# Experiment Configuration
CONFIG = {
    'seed': 42,
    'train_size': 0.7,
    'val_size': 0.15,
    'test_size': 0.15,
    'model': 'xgboost',
    'hyperparams': {
        'n_estimators': 200,
        'max_depth': 7,
        'learning_rate': 0.05
    }
}
```

## Notebook Cell Organization

Each research notebook should follow:

1. **Setup** - Imports, config, seed setting
2. **Data Loading** - Load and validate
3. **Exploration** - EDA and visualization
4. **Processing** - Prep and feature engineering
5. **Modeling** - Build and train
6. **Evaluation** - Metrics and analysis
7. **Save Results** - Checkpoint and export

## Publication Checklist

- [ ] All figures are high-resolution (300+ DPI)
- [ ] Tables are formatted consistently
- [ ] Results are statistically significant (p < 0.05)
- [ ] Confidence intervals reported for all metrics
- [ ] Ablation studies included
- [ ] Error analysis provided
- [ ] Comparison to 3+ baselines
- [ ] Code is reproducible on fresh environment
- [ ] All assumptions stated
- [ ] Limitations discussed
- [ ] Future work outlined
