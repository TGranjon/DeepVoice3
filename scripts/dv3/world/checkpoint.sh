#!/bin/bash
#SBATCH -c4
#SBATCH --mem 80G
#SBATCH -p gpu
#SBATCH --gres gpu:1
#SBATCH --time 04-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

python ~/deepvoice3_by_tg/train.py --preset=../../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/world/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/world/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/world/logs --restore-parts=/lium/raid01_b/tgranjon/dv3/world/checkpoints/checkpoint_step000440000.pth
