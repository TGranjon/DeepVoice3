#!/bin/bash

# Lance l'apprenstissage en partant d'un checkpoint spécifié.
# python <script train.py> <preset> <emplacement des données pré-traitées> <emplacement où sauvegarder les checkpoints> <emplacement où sauvegarder les logs> <emplacement du checkpoint duquel partir>
python ../../deepvoice3_by_tg/train.py --preset=../../deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/logs --restore-parts=/lium/raid01_b/tgranjon/dv3/checkpoints/checkpoint_step000570000.pth
