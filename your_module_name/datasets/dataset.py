"""Dataset class to be extended by dataset-specific classes."""
from pathlib import Path
import argparse
import os

from text_recognizer import util


class Dataset:
    """Simple class for datasets."""
    """
    Allows you to download and store your datasets
    """