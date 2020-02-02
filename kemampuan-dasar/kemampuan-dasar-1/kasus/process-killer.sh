#!/bin/bash

#ps -ef | grep $1

if [ -z "$1" ]; then
    echo "You need to supply a search string..."
else
    processes=$(ps aux | grep $1 -i | awk '{print $2}')
    echo "Processes: "$processes
    while true; do
        read -ep "Hentikan semua proses '$1'? [y/N] " yesno
        case $yesno in
            [Yy]* )
                echo 'Killing processes...'
                for i in $processes; do kill $i; done
                echo "Processes Killed: " $processes
                break;;
            * )
                echo "Skipped killing processes..."
                break;;
        esac
    done
fi