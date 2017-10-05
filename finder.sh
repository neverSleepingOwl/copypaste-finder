#!/bin/bash +x 

CURDIR=$(pwd)
cd $1
find . -type f | grep -o -P '\.(\/\w+)*\w+\.py' | xargs cat | "$CURDIR/finder.py"
