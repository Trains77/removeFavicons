import pathlib, os
from pathlib import Path

librewolf_instance = "7nojjl8s.default-release"

librewolf1 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance +  "/favicons.sqlite"
isFile = os.path.isfile(librewolf1)
if isFile == True:
    os.remove(librewolf1)
librewolf2 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance + "/favicons.sqlite-wal"
isFile = os.path.isfile(librewolf2)
if isFile == True:
    os.remove(librewolf2)
