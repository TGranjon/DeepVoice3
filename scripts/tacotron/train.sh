#!/bin/bash

cd ../../tacotron/

# python train.py --data-root=<emplacement des données pré-traitées> --checkpoint-dir=<emplacement où sauvegarder les checkpoints> 
# Version en anglais.
python train.py --data-root=/lium/raid01_b/tgranjon/tacotron/data --checkpoint-dir=/lium/raid01_b/tgranjon/tacotron/checkpoints

# Version en français (_ne fonctionne pas pour l'instant_)
#python train.py --data-root=/lium/raid01_b/tgranjon/tacotron/data/fr --checkpoint-dir=/lium/raid01_b/tgranjon/tacotron/checkpoints/fr

cd ../scripts/tacotron
