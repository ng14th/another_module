# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
try:
    from sub_module import core  # noqa
except ModuleNotFoundError:
    current_path = Path(os.getcwd())
    sys.path.append(str(current_path.parents[1]))
    from sub_module import core  # noqa
