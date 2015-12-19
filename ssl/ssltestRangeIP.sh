#! /bin/bash

while read line
do
	/PATH_TO_SCANNER/SCANNER $line > FOLDER/SCANNER_$line
done < rangeIP.txt
