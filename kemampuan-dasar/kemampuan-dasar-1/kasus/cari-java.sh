#!/bin/bash
find_file () {
    pencarian=$(find $1 -name "*.java")
    echo Ada file Java di direktori $pencarian.
}

find_file $1