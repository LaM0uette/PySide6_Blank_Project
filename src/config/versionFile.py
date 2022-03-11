import pyinstaller_versionfile

from src.config import config


pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=config.version,
    company_name=config.auteur,
    file_description=config.description,
    internal_name=config.nom,
    legal_copyright="© My Imaginary Company. All rights reserved.",
    original_filename=config.nom,
    product_name=config.nom
)
