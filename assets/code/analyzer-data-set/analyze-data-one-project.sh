#!/bin/bash

# Chemins vers les dossiers contenant les scripts Python
folders=("../search-consumers" "../search-producers" "../search-microservices")

output_directories=()

for folder in "${folders[@]}"
do
    echo "Recherche de scripts Python dans le dossier : $folder"
    
    if [ -d "$folder" ]; then
        for script in "$folder"/*.py
        do
            echo "Exécution de $script ..."
            python3 "$script" -p $1
        done
    fi
done

python3 analyze-project-data.py $1

rm -rf ./outputs