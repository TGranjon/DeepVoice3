#!/bin/bash
#SBATCH -c2
#SBATCH --mem 100G
#SBATCH -p gpu
#SBATCH --job-name train-Tacotron-Fr
#SBATCH --gres gpu:4
#SBATCH --time 06-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

#python ~/tacotron_pytorch/train.py --data-root=/lium/raid01_b/tgranjon/tacotron/data --checkpoint-dir=/lium/raid01_b/tgranjon/tacotron/checkpoints
python ~/tacotron_pytorch/train.py --data-root=/lium/raid01_b/tgranjon/tacotron/data/fr --checkpoint-dir=/lium/raid01_b/tgranjon/tacotron/checkpoints/fr
