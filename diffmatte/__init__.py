import os
from pathlib import Path

from diffmatte.modeling.meta_arch.difmatte import DifMatte

__all__ = [
    'DifMatte',
    'CONFIGS_PATH',
]

CONFIGS_PATH = Path(os.path.abspath(__file__)).parents[0] / 'configs'
