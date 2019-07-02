#!/bin/bash
#SBATCH --mem 45G
#SBATCH -p gpu
#SBATCH --gres gpu:1
#SBATCH -c 2
#SBATCH --job-name Preprocess-Wavenet
#SBATCH --time 02:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

cd ~/wavenet_vocoder
#python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/wavenet/data --preset=presets/synpaflex_gaussian.json
python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex /lium/raid01_b/tgranjon/wavenet/data --preset=presets/synpaflex_mixture.json
cd ~/scripts/wavenet
