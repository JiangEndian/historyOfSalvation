#!/bin/bash

rm ~/grace_voice_file/alt3_all_mp3/*

file_number='1001'
for one_mp3 in $(cat alt3_all_mp3_string);do
    cp ~/grace_voice_file/$one_mp3'.mp3' ~/grace_voice_file/alt3_all_mp3/$file_number'.mp3'
    ((file_number++))
    #echo $file_number
    #read
done

mv alt3_all_text_string ~/grace_voice_file/alt3_all_mp3/textbook.txt
mv alt3_all_mp3_string ~/grace_voice_file/alt3_all_mp3/

cd ~/grace_voice_file/alt3_all_mp3/  &&  zip -r -0 alt3_all_mp3.zip *.mp3 && rm *.mp3 && mv alt3_all_mp3.zip alt3_app_mp3.mp3 && zip -r -0 alt3_all.zip * 


