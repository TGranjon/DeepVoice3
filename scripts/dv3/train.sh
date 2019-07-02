#!/bin/bash
#SBATCH -c2
#SBATCH --mem 80G
#SBATCH -p gpu
#SBATCH --job-name train
#SBATCH --gres gpu:1
#SBATCH --time 04-00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

cd ~/deepvoice3_by_tg/

#python train.py --preset=presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/tiers/data/ --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/tiers/checkpoints/ --log-event-path=/lium/raid01_b/tgranjon/dv3/tiers/logs/
#python train.py --preset=presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/demi/data/ --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/demi/checkpoints/ --log-event-path=/lium/raid01_b/tgranjon/dv3/demi/logs/
python train.py --preset=presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/old/data/ --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/old/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/old/logs

cd ~/scripts/dv3/
