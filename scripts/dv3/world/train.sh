#!/bin/bash

# Lance l'entraînement.

cd ../../../deepvoice3_world

# python train.py --preset=<preset> --data-root=<emplacement des données pré-traitées> --checkpoint-dir=<où sauvegarder les checkpoints> --log-event-path=<où sauvegarder les logs> 

python train.py --preset=deepvoice3_by_tg/presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/world/data --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/world/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/world/logs

cd ../scripts/dv3/world
