#!/bin/bash

# Lance l'apprenstissage en partant d'un checkpoint spécifié.
# python train.py --preset=<preset> --data-root=<emplacement des données pré-traitées> --checkpoint-dir=<emplacement où sauvegarder les checkpoints> --log-event-path=<emplacement où sauvegarder les logs> <emplacement du checkpoint duquel partir>

cd ../../../deepvoice3_world/

python train.py --preset=deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/world/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/world/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/world/logs --restore-parts=/lium/raid01_b/tgranjon/dv3/world/checkpoints/checkpoint_step000440000.pth

cd ../scripts/dv3/world
