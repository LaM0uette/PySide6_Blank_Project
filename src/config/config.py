import configparser

from . import vrb


### FICHIER CONFIG ______________
cfg = configparser.ConfigParser()
cfg.read(vrb.INI_CONFIG, encoding="utf-8")

### infos _______________
nom = cfg["infos"]["nom"]
description = cfg["infos"]["description"]
version = float(cfg["infos"]["version"])
auteur = cfg["infos"]["auteur"]

### config ________________________
theme = cfg["config"]["theme"]
font = cfg["config"]["font"]
widht = int(cfg["config"]["widht"])
height = int(cfg["config"]["height"])
opacity = float(cfg["config"]["opacity"])
cur = cfg["config"]["cur"]

### var _____________________
auto_reload = cfg["var"]["autoreload"].lower() == "true"
auto_close = cfg["var"]["autoClose"].lower() == "true"
resize = cfg["var"]["resize"].lower() == "true"
