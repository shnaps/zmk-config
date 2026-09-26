"""Tidy raw behavior labels in the parsed keymap yaml.

keymap-drawer leaves behaviors it does not know as raw '&name' strings.
Layer names come from each layer's display-name in the keymap.
Re-run this after every parse.
"""
import io
import sys

LABELS = {
    "'&studio_unlock'": "{t: Studio, s: unlock}",
    "'&bootloader'": "BOOT",
    "'&caps_word'": "Caps Word",
}

path = sys.argv[1] if len(sys.argv) > 1 else "draw/garden36.yaml"
s = io.open(path, encoding="utf-8").read()

for old, new in LABELS.items():
    s = s.replace(old, new)

io.open(path, "w", encoding="utf-8", newline="\n").write(s)
print("polished %s" % path)
