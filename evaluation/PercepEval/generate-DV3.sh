#!/bin/bash

OUTDIR=./tests/DeepVoice3/
rm -rf $OUTDIR
python ./generator.py -o $OUTDIR -j ./input/DV3.json -t ./input/DV3.tpl -c input/completed.tpl -i input/index.tpl -e input/export.tpl -s ./input/dv3_sysA.csv SysA ./input/dv3_sysB.csv SysB -n
ret=$?
if [ $ret == 0 ]; then
	mkdir $OUTDIR/static
	cp -rf ./input/static/* $OUTDIR/static
fi
