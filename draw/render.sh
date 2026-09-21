#!/usr/bin/env sh
# Regenerate the keymap image from config/garden36.keymap.
# Requires uv (https://docs.astral.sh/uv/). PNG step needs Inkscape, optional.
set -e
cd "$(dirname "$0")/.."

uvx --from keymap-drawer keymap parse -z config/garden36.keymap -o draw/garden36.yaml
python draw/polish.py draw/garden36.yaml
uvx --from keymap-drawer keymap -c draw/config.yaml draw draw/garden36.yaml \
    --dts-layout boards/shields/garden36/garden36-layouts.dtsi \
    --layout-name physical_layout0 \
    -o draw/garden36.svg
echo "Wrote draw/garden36.svg"
