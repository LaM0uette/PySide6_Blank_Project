import datetime
import os


### VARIABLES
GUID = str(os.getenv("USERNAME"))
DATE_NOW = datetime.datetime.now()
DATE_NOW_FORMAT = datetime.datetime.now().strftime("%d_%m_%Y")


### DOSSIERS
DO_CUR = "src/assets/cursor/"
DO_DATA = "src/build/palettes/data/"
DO_IMG = "src/assets/img/"
DO_THEME = "src/build/themes/"
DO_SCRIPT = "src/scripts/"


### FICHIERS
INI_CONFIG = "src/config/config.ini"
JS_FONT = f"{DO_DATA}font.json"
