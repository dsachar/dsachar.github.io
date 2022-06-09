#! /bin/sh


for file in *.pdf; do
    [ -f "$file" ] || break
    filename="${file%.*}"
    echo "$file -> ${filename}.svg"
    pdf2svg $file "${filename}.svg"
done