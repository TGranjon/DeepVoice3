#!/bin/bash
#SBATCH --mem 20G
#SBATCH --job-name Synthese-All
#SBATCH --time 01:30:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user=thomas.granjon.etu@univ-lemans.fr

cd ~/deepvoice3_by_tg

time python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/full_text --preset=presets/deepvoice3_synpaflex.json
echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/tiers/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/tiers_text --preset=presets/deepvoice3_synpaflex.json
echo -------------------------------------------------
time python synthesis.py /lium/raid01_b/tgranjon/dv3/demi/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/demi_text --preset=presets/deepvoice3_synpaflex.json
echo -------------------------------------------------
time python synthesis.py /lium/raid01_b/tgranjon/dv3/emotional/checkpoints/0/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/0_text --preset=presets/deepvoice3_synpaflex.json
echo -------------------------------------------------
time python synthesis.py /lium/raid01_b/tgranjon/dv3/emotional/checkpoints/1/average.pth tests/test_fr/corpus_phonemes.txt /lium/raid01_b/tgranjon/dv3/synthesis/1_phone --preset=presets/deepvoice3_synpaflex.json
#echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/wavenet_full --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth
#echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/tiers/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/wavenet_tiers --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth
#echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/demi/checkpoints/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/wavenet_demi --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth
#echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/emotional/checkpoints/0/average.pth tests/test_fr/corpus_text.txt /lium/raid01_b/tgranjon/dv3/synthesis/wavenet_0 --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth
#echo -------------------------------------------------
#time python synthesis.py /lium/raid01_b/tgranjon/dv3/emotional/checkpoints/1/average.pth tests/test_fr/corpus_phonemes.txt /lium/raid01_b/tgranjon/dv3/synthesis/wavenet_1 --preset=presets/deepvoice3_synpaflex.json --checkpoint-wavenet=/lium/raid01_b/tgranjon/wavenet/checkpoints/checkpoint_step000248556.pth

cd ~/scripts/dv3
