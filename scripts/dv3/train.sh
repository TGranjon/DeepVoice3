#!/bin/bash

# Lance l'entraînement.

cd ../../deepvoice3_by_tg/

# python train.py --preset=<preset> --data-root=<emplacement des données pré-traitées> --checkpoint-dir=<où sauvegarder les checkpoints> --log-event-path=<où sauvegarder les logs> 
python train.py --preset=presets/deepvoice3_synpaflex.json --data-root=/lium/raid01_b/tgranjon/dv3/old/data/ --checkpoint-dir=/lium/raid01_b/tgranjon/dv3/old/checkpoints --log-event-path=/lium/raid01_b/tgranjon/dv3/old/logs

cd ../scripts/dv3/
