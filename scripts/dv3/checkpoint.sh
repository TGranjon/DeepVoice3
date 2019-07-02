#!/bin/bash

# Lance l'apprenstissage en partant d'un checkpoint spécifié.
# python train.py --preset=<preset> --data-root=<emplacement des données pré-traitées> <emplacement où sauvegarder les checkpoints> <emplacement où sauvegarder les logs> <emplacement du checkpoint duquel partir>

cd ../../deepvoice3_by_tg

python train.py --preset=../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/logs --restore-parts=/lium/raid01_b/tgranjon/dv3/checkpoints/checkpoint_step000570000.pth

cd ../scripts/dv3
