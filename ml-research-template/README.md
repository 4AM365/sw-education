# ML Research Project Template

A reproducible, publication-ready template for machine learning research projects.

## Project Structure

```
ml-research-template/
├── README.md                      # Project documentation
├── RESEARCH.md                    # Research findings and results
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
├── config/
│   └── config.yaml               # Project configuration
├── data/
│   ├── raw/                      # Original, immutable data
│   ├── processed/                # Cleaned, processed data
│   └── external/                 # External datasets
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_data_preparation.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_training.ipynb
│   ├── 05_evaluation_analysis.ipynb
│   └── 06_results_publication.ipynb
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py             # Data loading utilities
│   ├── features/
│   │   ├── __init__.py
│   │   └── engineering.py        # Feature engineering
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py              # Training logic
│   │   └── evaluate.py           # Evaluation metrics
│   └── utils/
│       ├── __init__.py
│       └── helpers.py            # Utility functions
├── results/
│   ├── models/                   # Trained models
│   ├── figures/                  # Publication-quality figures
│   └── reports/                  # Analysis reports
└── tests/
    ├── __init__.py
    └── test_pipeline.py          # Unit tests
```

## Key Features

- **Reproducible**: All random seeds set, dependencies pinned
- **Modular**: Reusable components in `src/`
- **Documented**: Clear notebooks for each stage
- **Publication-Ready**: Templates for figures and reports
- **Version Controlled**: Proper .gitignore for large files
- **Environment Management**: .env for credentials and config

## Environment Variables

Create a `.env` file with:

```
# Data
DATA_PATH=./data/raw
PROCESSED_DATA_PATH=./data/processed

# Model
MODEL_SEED=42
TEST_SIZE=0.2
VALIDATION_SIZE=0.1

# External APIs (if needed)
WANDB_API_KEY=your_key_here
MLFLOW_TRACKING_URI=http://localhost:5000

# Output
RESULTS_PATH=./results
FIGURES_PATH=./results/figures
```

## Notebooks Workflow

1. **01_exploratory_analysis.ipynb** - Data exploration and visualization
2. **02_data_preparation.ipynb** - Cleaning and preprocessing
3. **03_feature_engineering.ipynb** - Feature creation and selection
4. **04_model_training.ipynb** - Model development and hyperparameter tuning
5. **05_evaluation_analysis.ipynb** - Model evaluation and ablation studies
6. **06_results_publication.ipynb** - Generate publication figures and tables

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Create environment
cp .env.example .env
# Edit .env with your values

# Run first notebook
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

## Publishing Research

See `RESEARCH.md` for:
- How to structure your findings
- Guidelines for creating publication-ready figures
- Best practices for reproducibility
- Citation and attribution guidelines
