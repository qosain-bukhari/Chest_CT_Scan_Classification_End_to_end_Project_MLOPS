import setuptools


__version__ = "0.0.1"

REPO_URL = "Chest_CT_Scan_Classification_End_to_end_Project_MLOPS"
AUTHOR = "qosain-bukhari"
SRC_REPO="Cnnclassificatier"
DESCRIPTION = "Chest CT Scan Classification using Deep Learning with MLOps practices"
AUTHOR_EMAIL = "bukhariqosain824@gmail.com"

setuptools.setup(
    name=REPO_URL,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=f"https://github.com/{AUTHOR}/{REPO_URL}",
    PROJECT_URL={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_URL}"
    },

    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)