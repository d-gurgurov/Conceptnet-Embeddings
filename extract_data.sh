#!/bin/bash

declare -a lang_codes=("ae" "mt" "bg" "cs" "lb" "ro")

for lang_code in "${lang_codes[@]}"
do
    echo "Processing language code: $lang_code"

    python3 main.py --language "$lang_code" --output "cn_data" --glove 'no' --ppmi "yes" --ppmi_dim 50
done