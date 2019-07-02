#!/bin/bash

cd ~/deepvoice3_by_tg

python synthesis.py /lium/raid01_b/tgranjon/dv3/world/checkpoints/checkpoint_step$1.pth ~/deepvoice3_by_tg/tests/test_fr/text_fr.txt /lium/raid01_b/tgranjon/dv3/world/synthesis --preset=presets/deepvoice_synpaflex.json


cd ~/scripts/dv3
