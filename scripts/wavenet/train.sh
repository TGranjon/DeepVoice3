#!/bin/bash

# Lance l'entraînement.
# Note : il est possible de reprendre l'entraînement à partir d'un checkpoint en ajoutant l'option --checkpoint=<checkpoint>.

cd ../../wavenet_vocoder

# python train.py --data-root=<données pré-traitées> --preset=<preset> --checkpoint-dir=<Où sauvegarder les checkpoints> --log-event-path=<Où sauvegarder les logs>
python train.py --data-root=/lium/raid01_b/tgranjon/wavenet/data --preset=presets/synpaflex_mixture.json --checkpoint-dir=/lium/raid01_b/tgranjon/wavenet/checkpoints --log-event-path=/lium/raid01_b/tgranjon/wavenet/logs

cd ~/scripts/wavenet
