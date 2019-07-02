#!/bin/bash
#SBATCH --mem 50G
#SBATCH -c 2
#SBATCH --job-name Preprocess-DV3
#SBATCH --time 02:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

cd ~/deepvoice3_by_tg/

python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/dv3/old/data --preset=presets/deepvoice3_synpaflex.json
#python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/dv3/data --preset=presets/deepvoice3_synpaflex.json
#python preprocess.py ljspeech /lium/corpus/synthese/LJSpeech-1.1/ /lium/raid01_b/tgranjon/tacotron/data --preset=presets/deepvoice3_ljspeech.json

cd ~/scripts/dv3/
