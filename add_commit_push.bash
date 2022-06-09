#!/bin/bash

INFO=$(date +%Y%m%d)

#git status
#echo;echo
git add *
git commit -m $INFO && echo commit_succese
git push
echo;echo
git status

exit 0
