"""
Initialization file.
"""

import os 
from .config import WDIR
from . import utils

for directory in ['logs', 'results', 'data', 'tensorboard']:
    if directory not in os.listdir(WDIR):
        os.mkdir(WDIR + directory)

__all__ = ['artificial', 'household', 'keras_utils', 'utils', 'config', 'models', 'user', 'user_models', 'models']