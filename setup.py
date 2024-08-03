# -*- coding: utf-8 -*-

"""
    python setup.py py2app
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime

from setuptools import setup


def remove_trash():
    trash = ("build", ".eggs", "dist")
    for i in trash:
        try:
            shutil.rmtree(i)
        except Exception as e:
            print(e)
            continue


def move_app_to_desktop(appname: str):
    desktop = os.path.expanduser("~/Desktop")

    dest = os.path.join(desktop, f"{appname}.app")
    src = os.path.join("dist", f"{appname}.app")

    try:
        if os.path.exists(dest):
            shutil.rmtree(dest)
    except Exception as e:
        print(e)

    try:
        shutil.move(src, dest)
    except Exception as e:
        print(e)

    try:
        subprocess.Popen(["open", "-R", dest])
    except Exception as e:
        print(e)


YEAR = datetime.now().year # CURRENT YEAR
AUTHOR = "AUTHOR NAME"  # "Evgeny Loshkarev"
SHORT_AUTHOR_NAME = "SHORT_AUTHOR_NAME" # "Evlosh"
COMPANY = "COMPANY_NAME" # "MIUZ Diamonds" or ""
APP_NAME = "APP_NAME"
APP_VER = "APP_VER" # "1.0.0"
ICON_PATH = "ICON_PATH" # "icon/icon.icns" or "icon.icns"
MAIN_FILES = ["FILENAME.py"] # SINGLE OR MULTIPLE PYTHON FILES

BUNDLE_ID = f"com.{SHORT_AUTHOR_NAME}.{APP_NAME}" # DON'T CHANGE IT
PY_2APP = "py2app" # DON'T CHANGE IT


# CREATE FILES LIST WITH EXTENSIONS
folder_name = "FOLDER_NAME"
extensions = (".FILE_EXTENSION", ".FILE_EXTENSION",)
FOLDER_EXT_FILES = [
    os.path.join(folder_name, i)
    for i in os.listdir(folder_name)
    if i.endswith(extensions)
    ]

# CREATE FILES LIST
folder_name = "FOLDER_NAME"
FOLDER_ANY_FILES = [
    os.path.join(folder_name, i)
    for i in os.listdir(folder_name)
    ]

# IF YOU DON'T HAVE ADVANCED FILES
DATA_FILES = []

# IF YOU HAVE ADVANCED FILES
DATA_FILES = [
    "SINGLE_FILE.ext", # SINGLE FILE
    "FOLDER/SINGLE_FILE.ext", # SINGLE FILE WITH FOLDER
    ("FOLDER_NAME", FOLDER_EXT_FILES), # MULTIPLE FILES WITH EXTENSIONS AND FOLDER 
    ("FOLDER_NAME", FOLDER_ANY_FILES) # MULTIPLE FILES WITH FOLDER
    ]



# DON'T CHANGE IT

OPTIONS = {"iconfile": ICON_PATH,
           "plist": {"CFBundleName": APP_NAME,
                     "CFBundleShortVersionString": APP_VER,
                     "CFBundleVersion": APP_VER,
                     "CFBundleIdentifier": BUNDLE_ID,
                     "NSHumanReadableCopyright": (
                         f"Created by {AUTHOR}"
                         f"\nCopyright © {YEAR} {COMPANY}."
                         f"\nAll rights reserved.")}}


if __name__ == "__main__":

    sys.argv.append(PY_2APP)

    try:
        setup(
            app=MAIN_FILES,
            name=APP_NAME,
            data_files=DATA_FILES,
            options={PY_2APP: OPTIONS},
            setup_requires=[PY_2APP],
            )

        remove_trash()
        move_app_to_desktop()
        remove_trash()

    except Exception as e:
        print(e)
        remove_trash()
