"""
Model training and evaluation utilities.
"""

import os
from typing import Tuple, Dict
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
from dotenv import load_dotenv


class ModelEvaluator:
    """Evaluate model performance."""
    
    def __init__(self):
        """Initialize evaluator."""
        load_dotenv()
        self.metrics = {}
    
    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray,
                y_pred_proba: np.ndarray = None) -> Dict[str, float]:
        """
        Calculate comprehensive metrics.
        
        Parameters
        ----------
        y_true : np.ndarray
            True labels
        y_pred : np.ndarray
            Predicted labels
        y_pred_proba : np.ndarray, optional
            Predicted probabilities for probabilistic metrics
            
        Returns
        -------
        metrics : dict
            Dictionary of metrics
        """
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, zero_division=0),
            'recall': recall_score(y_true, y_pred, zero_division=0),
            'f1': f1_score(y_true, y_pred, zero_division=0),
        }
        
        if y_pred_proba is not None:
            metrics['auc_roc'] = roc_auc_score(y_true, y_pred_proba)
        
        self.metrics = metrics
        return metrics
    
    def print_report(self, metrics: Dict[str, float] = None):
        """
        Print formatted metrics report.
        
        Parameters
        ----------
        metrics : dict, optional
            Metrics to print. If None, uses last evaluated metrics.
        """
        if metrics is None:
            metrics = self.metrics
        
        print("\n" + "="*50)
        print("MODEL EVALUATION REPORT")
        print("="*50)
        for metric_name, value in metrics.items():
            print(f"  {metric_name:.<40} {value:.4f}")
        print("="*50 + "\n")


class ModelSaver:
    """Save and load models."""
    
    def __init__(self, save_path: str = None):
        """
        Initialize saver.
        
        Parameters
        ----------
        save_path : str, optional
            Directory to save models. If None, uses MODEL_SAVE_PATH from .env
        """
        load_dotenv()
        self.save_path = save_path or os.getenv('MODEL_SAVE_PATH', './results/models/')
        os.makedirs(self.save_path, exist_ok=True)
    
    def save_model(self, model, name: str = 'model.pkl') -> str:
        """
        Save model to disk.
        
        Parameters
        ----------
        model : object
            Model to save (should be pickle-compatible)
        name : str
            Filename for the model
            
        Returns
        -------
        filepath : str
            Path where model was saved
        """
        filepath = os.path.join(self.save_path, name)
        joblib.dump(model, filepath)
        print(f"Model saved to: {filepath}")
        return filepath
    
    def load_model(self, name: str = 'model.pkl'):
        """
        Load model from disk.
        
        Parameters
        ----------
        name : str
            Filename of the model
            
        Returns
        -------
        model : object
            Loaded model
        """
        filepath = os.path.join(self.save_path, name)
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Model not found: {filepath}")
        
        model = joblib.load(filepath)
        print(f"Model loaded from: {filepath}")
        return model
