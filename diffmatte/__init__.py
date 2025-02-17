import os
import sys
from pathlib import Path

from diffmatte.modeling.meta_arch.difmatte import DifMatte

__all__ = [
    'DifMatte',
    'CONFIGS_PATH',
]

DIFFMATTE_LOCATION = Path(os.path.abspath(__file__)).parents[0]

CONFIGS_PATH = DIFFMATTE_LOCATION / 'configs'

sys.path.insert(0, str(DIFFMATTE_LOCATION))
