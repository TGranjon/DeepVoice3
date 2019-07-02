#!/bin/bash
#SBATCH --mem 45G
#SBATCH -c 2
#SBATCH --job-name Preprocess-DV3-World
#SBATCH --time 02:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

python ~/deepvoice3_by_tg/preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/dv3/world/data --preset=../../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json
