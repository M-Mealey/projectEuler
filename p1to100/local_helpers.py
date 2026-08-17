"""
Adds the repo root to sys.path so problem files can `from local_helpers
import ...` regardless of whether they're run directly or loaded by
time_responses.py.
"""
import sys
from pathlib import Path

ROOT = str(Path(__file__).resolve().parent.parent)
if ROOT not in sys.path:
    sys.path.append(ROOT)

from helpers import *  # pylint: disable=wildcard-import,unused-wildcard-import
