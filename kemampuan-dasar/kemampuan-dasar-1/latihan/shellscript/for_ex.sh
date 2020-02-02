#!/bin/bash
for (( counter=10; counter>0; counter-=2 ))
do
echo -n "$counter "
done
printf "\n"