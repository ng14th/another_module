# -*- coding: utf-8 -*-
import os
import sys
from pathlib import Path
try:
    from sub_module import core  # noqa
except ModuleNotFoundError:
    current_path = Path(os.getcwd())
    print(current_path)
    sys.path.append(str(current_path.parents[1]))
    from sub_module import core  # noqa


core.datetime_now
print("Đây là commit từ module chính")
print("Datetime now", core.datetime_now)
