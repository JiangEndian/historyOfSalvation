#!/usr/bin/env python3
import random
from aip import AipSpeech
from MyPython3 import *

""" 你的 APPID AK SK """
APP_ID = '15480868'
API_KEY = '2QT7r6p9H8PKCdzpL14mm2xD'
SECRET_KEY = 'LzGuG24eXu2qvsqiAQGGT9zhHHwkR8Iw'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#新库吧。换新库吧。同时，处理数据时，加上当时的时间秒数，来作为文件名，一个一个的处理，有错误时再看。读取的时候，就那样放一遍意思下，有就有，没就没。。。拉倒吧。。。
#得弄个自动切割的，来合成完整的一段话。。。嗯，先从bt开始吧，合成语音，附上去。
#1、判断文本字数并分割文本
#2、按文本提交得到数个result
#3、每个result都不为dict，才可一起写入

#分割文本为指定大小以内的文本列表
def texts2text_list(texts):
    texts_list = list(texts)
    numbers = 0
    text_list = []
    text_one = ''
    for char in texts_list:
        text_one = text_one + char
        numbers += 1
        if numbers >= 500:
            text_list.append(text_one)
            text_one = ''
            numbers = 0
    if text_one:
        text_list.append(text_one)
    return text_list

#转换一个文本到语音
def text2voice(text):
    result  = client.synthesis(text, 'zh', 1, {
    'vol': 15, #音量0-15
    'per':3, #发音人0女,1男,3情感男,4情感女
    'spd':7 #语速0-9
    })
    return result
#转换文本列表到语音列表
def voice2voice_list(text_list):
    voice_list = []
    for text in text_list:
        voice_list.append(text2voice(text))
    return voice_list
 
#转换语音列表为一个语音文件
def voice_list2voice_file(voice_list, file_name):
    for voice in voice_list:
        if isinstance(voice, dict):
            print('%s有错误，回车跳过此条转换继续。' % file_name)
            input()
            return 0
    with open(file_name, 'ab') as f: #二进制打开用于追加
        for voice in voice_list:
            f.write(voice)

#终极合成_任意长文本转到一个语音文件
def texts2voice_file(texts, file_name):
    text_list = texts2text_list(texts)
    voice_list = voice2voice_list(text_list)
    voice_list2voice_file(voice_list, file_name)
    

#texts2voice_file('测试任意长文本转至一个语音文件，这是以5个字符为分割的。。。', 'audio_baidu_api.mp3')
#行，挺好，虽然，挺怪怪的，5个字一停顿。。。但如果是500个应该不会那么怪了。。。

#cvlc_play_mp3('audio_baidu_api.mp3')


