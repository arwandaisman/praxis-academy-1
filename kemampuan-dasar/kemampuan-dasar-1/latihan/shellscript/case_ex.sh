#!/bin/bash

echo "Enter your lucky number"
read n
case $n in
10)
echo echo "You got 1st prize" ;;
55)
echo "You got 2nd prize" ;;
675)
echo "You got 3rd prize" ;;
*)
echo "Sorry, try for the next time" ;;
esac