# -*- coding: utf-8 -*-

"""
    python setup.py py2app
"""

import os
import shutil
import subprocess
import sys
import traceback
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

    if os.path.exists(dest):
        shutil.rmtree(dest)

    shutil.move(src, dest)
    subprocess.Popen(["open", "-R", dest])



PY_2APP = "py2app" # don't change it
YEAR = datetime.now().year
AUTHOR = "AUTHOR NAME"
COMPANY = "COMPANY_NAME"
APP_NAME = "APP_NAME"
BUNDLE_ID = f"com.ANY_NAME.{APP_NAME}"
APP_VER = "APP_VER"
ICON_PATH = "ICON_PATH"
MAIN_FILES = ["FILENAME.py"]

# include folder with .jpg and .svg files
folder_name = "FOLDER_NAME"
extensions = (".FILE_EXTENSION", ".FILE_EXTENSION",)
FOLDER_EXT_FILES = [
    os.path.join(folder_name, i)
    for i in os.listdir(folder_name)
    if i.endswith(extensions)
    ]

# include folder with any file
folder_name = "FOLDER_NAME"
FOLDER_ANY_FILES = [
    os.path.join(folder_name, i)
    for i in os.listdir(folder_name)
    ]

# EXAMPLE
DATA_FILES = [
    "SINGLE_FILE.ext",
    "FOLDER/SINGLE_FILE.ext", # SINGLE FILE WITH FOLDER
    ("FOLDER_NAME", FOLDER_EXT_FILES), # MULTIPLE FILES WITH EXTENSIONS AND FOLDER 
    ("FOLDER_NAME", FOLDER_ANY_FILES) # MULTIPLE FILES WITH FOLDER
    ]

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

    #you can run this file
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
