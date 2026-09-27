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
    "'&lang_switch'": "{t: LANG, s: EN/RU}",
}

path = sys.argv[1] if len(sys.argv) > 1 else "draw/garden36.yaml"
s = io.open(path, encoding="utf-8").read()

for old, new in LABELS.items():
    s = s.replace(old, new)

# The Ru layer sends QWERTY keycodes that Windows' Russian layout turns into
# Cyrillic. Draw the letters it types, not the keycode names.
RU = "й ц у к е н г ш щ з ф ы в а п р о л д ж я ч с м и т ь б ю".split()
start = s.index("  Ru:\n") + len("  Ru:\n")
lines = s[start:].split("\n")
for i, letter in enumerate(RU):
    assert lines[i].startswith("  - "), lines[i]
    lines[i] = "  - " + letter
assert lines[len(RU)] == "  - /", lines[len(RU)]
lines[len(RU)] = "  - {t: ., s: ','}"
s = s[:start] + "\n".join(lines)

RU_COMBOS = {"'['": "х", "']'": "ъ", "''''": "э", "'`'": "ё"}
for key, letter in RU_COMBOS.items():
    s = s.replace("  k: %s\n  l: [Ru]" % key, "  k: %s\n  l: [Ru]" % letter)

io.open(path, "w", encoding="utf-8", newline="\n").write(s)
print("polished %s" % path)
