import os
import time

import psutil

from src.build import *
from src.config import *


if __name__ == "__main__":
    pg_run = False
    for proc in psutil.process_iter():
        pi = proc.as_dict(attrs=["pid", "name"])
        if pi["name"] == f"{config.nom}.exe":
            pg_run = True

    if config.auto_reload and not pg_run:
        os.startfile(os.path.abspath(f"{vrb.DO_SCRIPT}convert_ui.bat"))
        time.sleep(1)
        Fct().GEN_SVG()
        time.sleep(0.3)

    if not pg_run:
        from src.app import app
