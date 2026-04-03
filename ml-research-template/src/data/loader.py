"""
Data loading and preprocessing utilities.
"""

import os
from typing import Tuple
import pandas as pd
import numpy as np
from dotenv import load_dotenv


class DataLoader:
    """Load and validate datasets."""
    
    def __init__(self, data_path: str = None):
        """
        Initialize DataLoader.
        
        Parameters
        ----------
        data_path : str, optional
            Path to data directory. If None, uses DATA_PATH from .env
        """
        load_dotenv()
        self.data_path = data_path or os.getenv('DATA_PATH', './data/raw')
        
    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load data from CSV file.
        
        Parameters
        ----------
        filename : str
            Name of CSV file in data directory
            
        Returns
        -------
        df : pd.DataFrame
            Loaded dataset
        """
        filepath = os.path.join(self.data_path, filename)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Data file not found: {filepath}")
        
        df = pd.read_csv(filepath)
        print(f"Loaded {filename}: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    
    def validate_data(self, df: pd.DataFrame) -> dict:
        """
        Validate data quality.
        
        Parameters
        ----------
        df : pd.DataFrame
            Dataset to validate
            
        Returns
        -------
        report : dict
            Data quality report
        """
        report = {
            'n_rows': len(df),
            'n_cols': len(df.columns),
            'n_missing': df.isnull().sum().sum(),
            'n_duplicates': df.duplicated().sum(),
            'dtypes': df.dtypes.value_counts().to_dict()
        }
        return report


class DataPreprocessor:
    """Preprocess and clean data."""
    
    def __init__(self, random_state: int = 42):
        """
        Initialize preprocessor.
        
        Parameters
        ----------
        random_state : int
            Random seed for reproducibility
        """
        self.random_state = random_state
        self.scaler = None
        
    def handle_missing_values(self, df: pd.DataFrame, method: str = 'drop') -> pd.DataFrame:
        """
        Handle missing values.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input dataset
        method : str
            Method: 'drop', 'mean', 'median', 'forward_fill'
            
        Returns
        -------
        df_clean : pd.DataFrame
            Dataset with missing values handled
        """
        if method == 'drop':
            return df.dropna()
        elif method == 'mean':
            return df.fillna(df.mean())
        elif method == 'median':
            return df.fillna(df.median())
        elif method == 'forward_fill':
            return df.fillna(method='ffill')
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def remove_outliers(self, df: pd.DataFrame, method: str = 'iqr', 
                       columns: list = None) -> pd.DataFrame:
        """
        Remove outliers from numeric columns.
        
        Parameters
        ----------
        df : pd.DataFrame
            Input dataset
        method : str
            Method: 'iqr' or 'zscore'
        columns : list, optional
            Columns to check. If None, checks all numeric columns.
            
        Returns
        -------
        df_clean : pd.DataFrame
            Dataset without outliers
        """
        if columns is None:
            columns = df.select_dtypes(include=[np.number]).columns
        
        df_clean = df.copy()
        
        for col in columns:
            if method == 'iqr':
                Q1 = df_clean[col].quantile(0.25)
                Q3 = df_clean[col].quantile(0.75)
                IQR = Q3 - Q1
                mask = ~((df_clean[col] < (Q1 - 1.5 * IQR)) | (df_clean[col] > (Q3 + 1.5 * IQR)))
                df_clean = df_clean[mask]
            elif method == 'zscore':
                z_scores = np.abs((df_clean[col] - df_clean[col].mean()) / df_clean[col].std())
                df_clean = df_clean[z_scores <= 3]
        
        return df_clean
