import pathlib, os
from pathlib import Path

librewolf1 = os.getenv("HOME") + "/.librewolf/7nojjl8s.default-release/favicons.sqlite"
isFile = os.path.isfile(librewolf1)
if isFile == True:
    os.remove(librewolf1)
librewolf2 = os.getenv("HOME") + "/.librewolf/7nojjl8s.default-release/favicons.sqlite-wal"
isFile = os.path.isfile(librewolf2)
if isFile == True:
    os.remove(librewolf2)
