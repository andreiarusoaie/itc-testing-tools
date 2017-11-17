#!/bin/bash

for i in csv-data/* ; do
  if [ -d "$i" ]; then
     if [ "$(basename $i)" != "clangcorealpha" ]; then
	 wc -l csv-data/$(basename "$i")/temp/*csv
     fi
  fi
done
