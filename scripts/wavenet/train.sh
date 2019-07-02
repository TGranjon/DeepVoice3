#!/bin/bash
#SBATCH -c2
#SBATCH --mem 80G
#SBATCH -p gpu
#SBATCH --job-name train-WaveNet
#SBATCH --gres gpu:2
#SBATCH --time 10-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

cd ~/wavenet_vocoder
python train.py --data-root=/lium/raid01_b/tgranjon/wavenet/data --preset=presets/synpaflex_mixture.json --checkpoint-dir=/lium/raid01_b/tgranjon/wavenet/checkpoints --log-event-path=/lium/raid01_b/tgranjon/wavenet/logs --checkpoint=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000060000.pth
cd ~/scripts/wavenet
