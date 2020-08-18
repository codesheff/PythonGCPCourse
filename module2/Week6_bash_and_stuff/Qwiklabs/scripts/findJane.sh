#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3 )

for file in ${files}
do
  echo Processing ${file}
  if [ -e ../${file} ]
  then
    echo ..${file} is found 
    echo ..${file} >> oldFiles.txt
  fi
done