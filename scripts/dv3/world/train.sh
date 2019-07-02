#!/bin/bash
#SBATCH -c2
#SBATCH --mem 40G
#SBATCH -p gpu
#SBATCH --job-name train-DV3-World
#SBATCH --gres gpu:1
#SBATCH --time 08-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

python ~/deepvoice3_by_tg/train.py --preset=../../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/world/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/world/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/world/logs
