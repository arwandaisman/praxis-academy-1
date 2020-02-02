#!/bin/bash
file='../cmdline.txt'
while read line; do
echo $line
done < $file