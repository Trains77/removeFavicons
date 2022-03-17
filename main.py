import pathlib, os
from pathlib import Path

# Set these to the actual name of your Firefox or Librewolf profiles
librewolf_instance = "7nojjl8s.default-release"
firefox_instance = "7ktl4nut.default-release"

# Librewolf

librewolf1 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance +  "/favicons.sqlite"
isFile = os.path.isfile(librewolf1)
if isFile == True:
    os.remove(librewolf1)
librewolf2 = os.getenv("HOME") + "/.librewolf/" + librewolf_instance + "/favicons.sqlite-wal"
isFile = os.path.isfile(librewolf2)
if isFile == True:
    os.remove(librewolf2)

# Firefox

firefox1 = os.getenv("HOME") + "/.mozilla/firefox/" + firefox_instance +  "/favicons.sqlite"
isFile = os.path.isfile(firefox1)
if isFile == True:
    os.remove(firefox1)
firefox2 = os.getenv("HOME") + "/.mozilla/firefox/" + firefox_instance + "/favicons.sqlite-wal"
isFile = os.path.isfile(firefox2)
if isFile == True:
    os.remove(firefox2)

# Brave

brave1 = os.getenv("HOME") + "/.config/BraveSoftware/Default/Favicons"
isFile = os.path.isfile(brave1)
if isFile == True:
    os.remove(brave1)
brave2 = os.getenv("HOME") + "/.config/BraveSoftware/Default/Favicons-journal"
isFile = os.path.isfile(brave2)
if isFile == True:
    os.remove(brave2)

# Chrome
chrome1 = os.getenv("HOME") + "/.config/google-chrome/Default/Favicons"
isFile = os.path.isfile(chrome1)
if isFile == True:
    os.remove(chrome1)
chrome2 = os.getenv("HOME") + "/.config/google-chrome/Default/Favicons-journal"
isFile = os.path.isfile(chrome2)
if isFile == True:
    os.remove(chrome2)
os.system("clear")
