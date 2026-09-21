"""Rename layers and tidy raw behavior labels in the parsed keymap yaml.

keymap-drawer emits lowercase devicetree node names and leaves behaviors it
does not know as raw '&name' strings. Re-run this after every parse.
"""
import io
import sys

LAYERS = {"default": "Base", "game": "Game", "num": "Num",
          "nav": "Nav", "fun": "Fun", "cmd": "Cmd"}

LABELS = {
    "'&studio_unlock'": "{t: Studio, s: unlock}",
    "'&bootloader'": "BOOT",
    "'&caps_word'": "Caps Word",
}

path = sys.argv[1] if len(sys.argv) > 1 else "draw/garden36.yaml"
s = io.open(path, encoding="utf-8").read()

for old, new in LAYERS.items():
    assert s.count("  %s:" % old) == 1, "layer %s not found" % old
    s = s.replace("  %s:" % old, "  %s:" % new)
    # &mo/&to/&tog targets are printed as the bare layer name
    s = s.replace("- %s\n" % old, "- %s\n" % new)
    s = s.replace("{t: %s," % old, "{t: %s," % new)

for old, new in LABELS.items():
    s = s.replace(old, new)

io.open(path, "w", encoding="utf-8", newline="\n").write(s)
print("polished %s" % path)
