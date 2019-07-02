#!/bin/bash
#SBATCH -c2
#SBATCH --mem 120G
#SBATCH -p gpu
#SBATCH --gres gpu:k40:1
#SBATCH --time 08-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

python ~/deepvoice3_pytorch/train.py --preset=../../deepvoice3_pytorch/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/logs --restore-parts=/lium/raid01_b/tgranjon/dv3/checkpoints/checkpoint_step000570000.pth
