#!/bin/bash

cd ~/deepvoice3_by_tg

#python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/checkpoint_step$1.pth tests/test_fr/roman.txt /lium/raid01_b/tgranjon/dv3/synthesis --preset=presets/deepvoice3_synpaflex.json --checkpoint_wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step$1.pth
python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/average.pth tests/test_fr/roman.txt /lium/raid01_b/tgranjon/dv3/synthesis --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step$1.pth

cd ~/scripts/dv3
