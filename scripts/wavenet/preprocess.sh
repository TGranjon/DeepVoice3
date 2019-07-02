#!/bin/bash

# Lance le pré-traitement des données.

cd ../../wavenet_vocoder

# python preprocess.py <nom du corpus> <adresse du fichier CSV> <Adresse où sauvegarder les données> --preset=<preset>
python preprocess.py synpaflex /lium/raid01_b/tgranjon/synpaflex/full /lium/raid01_b/tgranjon/wavenet/data --preset=presets/synpaflex_gaussian.json

cd ../scripts/wavenet
