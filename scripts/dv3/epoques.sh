#!/bin/bash

cd ~/deepvoice3_by_tg

for file in /lium/raid01_b/tgranjon/test/checkpoints/*.pth
do
	echo $file
	python synthesis_cop.py "$file" tests/test_fr/learn.txt /lium/raid01_b/tgranjon/test/synthesis --preset=presets/deepvoice3_test.json

done
cd ~/scripts/dv3
