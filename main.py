import pathlib, os
from pathlib import Path

librewolf_instance = "7nojjl8s.default-release"
firefox_instance = "7ktl4nut.default-release"

librewolf1 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance +  "/favicons.sqlite"
isFile = os.path.isfile(librewolf1)
if isFile == True:
    os.remove(librewolf1)
librewolf2 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance + "/favicons.sqlite-wal"
isFile = os.path.isfile(librewolf2)
if isFile == True:
    os.remove(librewolf2)

firefox1 = os.getenv("HOME") + "/.mozilla/firefox/" + firefox_instance +  "/favicons.sqlite"
isFile = os.path.isfile(firefox1)
if isFile == True:
    os.remove(firefox1)
firefox2 = os.getenv("HOME") + "/.mozilla/firefox/" + firefox_instance + "/favicons.sqlite-wal"
isFile = os.path.isfile(firefox2)
if isFile == True:
    os.remove(firefox2)

brave1 = os.getenv("HOME") + ".config/BraveSoftware/Default/Favicons"
isFile = os.path.isfile(brave1)
if isFile == True:
    os.remove(brave1)
brave2 = os.getenv("HOME") + ".config/BraveSoftware/Default/Favicons-journal"
isFile = os.path.isfile(brave2)
if isFile == True:
    os.remove(brave2)
