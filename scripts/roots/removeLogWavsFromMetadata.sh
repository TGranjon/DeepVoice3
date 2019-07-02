#!/bin/bash
#cd "../../data/SynPaFlex-1.1/wavs"
while read line
do 
    #echo -e $line
    wavname=$(echo -e $line | cut -f 1 -d "|") 
    duration=$(soxi -D "/lium/corpus/synthese/SynPaFlex-1.1/wavs/$wavname" | cut -f 1 -d ".")
    if (($duration < 11)); then
        echo $line >> synpaflex-metadata-10s.csv
    else
        echo $duration
    fi
#    exit
done < $1
