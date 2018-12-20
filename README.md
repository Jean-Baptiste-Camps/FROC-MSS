# FROC-MSS: Old French and Old Occitan Medieval Manuscripts HTR Data and Models

This repository contains:

- training and evaluation data from allographetic transcriptions of various
Old French and Old Occitan manuscripts, in various states of correctness, in Kraken
training format;
- 

If you plan of using this data or the provided model for a publication, please
cite it, as:


## Data format

Unicode NFD normalisation.

[3.5532] alphabet mismatch {'U', '/', '>', '&', '\uf127', ';', '<', 'P', 'K', '̈', '⸿', 'ͧ'}
[1057.9168] alphabet mismatch {'ͧ', 'V', 'U', '?', '<', '>', 'K', ';', 'P', '̈', "'", '/', '&', '\uf127', '̧', '⸿'} 
[795.2094] alphabet mismatch {'K', '>', '/', '&', 'y', 'P', '<', 'ͦ', '̈', 'U', '̧', 'ꝓ', ';', '⸿', 'ͧ', '\uf127'} 

alphabet mismatch {'/', '&', 'w', 'P', '̧', '\uf127', "'", 'y', '>', 'x', 'ͧ', '⸿', ']', '<', ';', 'U', '̈', '?', 'K', 'ȷ'} 

## Models

## List of manuscripts

## Cite this repository


Kraken: skipping files with no transcript when training

Finding png without gt:
for i in */*/*.png; do
    if [ ! -f "${i%.png}.gt.txt" ]; then
        echo "file not found"
    fi
done

The reverse:
for i in */*/*.gt.txt; do
    if [ ! -f "${i%.gt.txt}.png" ]; then
        echo "file not found"
    fi
done




