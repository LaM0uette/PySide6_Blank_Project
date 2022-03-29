import json
import os


class Config:

    ### FICHIER CONFIG ###
    with open(f"{os.path.dirname(__file__)}\config.json", "r", encoding="utf-8") as fichier:
        cfg = json.load(fichier)

    ### infos ###
    nom = cfg["nom"]
    description = cfg["description"]
    version = cfg["version"]
    auteur = cfg["auteur"]

    ### config ###
    theme = cfg["config"]["theme"]
    font = cfg["config"]["font"]
    widht = cfg["config"]["widht"]
    height = cfg["config"]["height"]
    opacity = cfg["config"]["opacity"]
    cur = cfg["config"]["cur"]

    ### var ###
    debug = cfg["var"]["debug"]
    resize = cfg["var"]["resize"]
    auto_close = cfg["var"]["auto_close"]
    toolbox_pin = cfg["var"]["toolbox_pin"]