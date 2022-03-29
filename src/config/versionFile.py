import pyinstaller_versionfile

from src.config.config import Config


pyinstaller_versionfile.create_versionfile(
    output_file="versionfile.txt",
    version=Config.version,
    company_name=Config.auteur,
    file_description=Config.description,
    internal_name=Config.nom,
    legal_copyright="© My Imaginary Company. All rights reserved.",
    original_filename=Config.nom,
    product_name=Config.nom
)
