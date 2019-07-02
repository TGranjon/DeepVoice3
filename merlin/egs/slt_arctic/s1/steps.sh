#!/bin/bash

./03_train_duration_model.sh conf/duration_slt_arctic_full.conf
./04_train_acoustic_model.sh conf/acoustic_slt_arctic_full.conf
./05_run_merlin.sh conf/test_dur_synth_slt_arctic_full.conf conf/test_synth_slt_arctic_full.conf
