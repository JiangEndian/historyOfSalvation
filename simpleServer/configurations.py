#!/usr/bin/env python3

from MyPython3 import *
import base64
import hashlib
import hmac
import requests
import time
import uuid
from urllib import parse

dictList = []

global restudy_info
restudy_info = {}
global my_dict_alt1
my_dict_alt1 = {}
global my_dict_alt2
my_dict_alt2 = {}
global my_dict_alt3
my_dict_alt3 = {}
global my_dict_alt4
my_dict_alt4 = {}
global my_dict_worshipAndBible
my_dict_worshipAndBible = {}
global file_dict
file_dict = {}
global MyConfigurations
MyConfigurations = {}

dictList.append(restudy_info)
dictList.append(my_dict_alt1)
dictList.append(my_dict_alt2)
dictList.append(my_dict_alt3)
dictList.append(my_dict_alt4)
dictList.append(my_dict_worshipAndBible)
dictList.append(file_dict)
dictList.append(MyConfigurations)

def updateTimeInfo(dictList=dictList):
    #统一的加上显示时间的
    nowHM = getnowtime('hm')
    intH = int(nowHM[:2])
    intM = int(nowHM[2:4])
    if intM == 0:
        remainHM = '{:02d}'.format(24-intH) + '00'
    else:
        remainHM = '{:02d}'.format(23-intH) + '{:02d}'.format(60-intM)
    for infoDict in dictList:
        infoDict['TIME'] = getnowtime('ymd') + ' '+nowHM
        infoDict['remainHM'] = remainHM


def readConfigurations(FileName):
    Configurations = {'InfoOfThisConfigurations':'This is a dictionary to story configurations.'}
    if os.path.exists(FileName):
        Configurations = loadffile(FileName)
    else:
        dump2file(FileName, Configurations)
    #print('Configurations:', Configurations)
    return Configurations

def updateConfigurations(FileName, Configurations, UpdateDictionary):
    Configurations = loadffile(FileName)
    #print('Configurations:', Configurations)
    #print('update:', UpdateDictionary)

    for Key in UpdateDictionary:
        Configurations[Key] = UpdateDictionary[Key]
    dump2file(FileName, Configurations)

#每两行加一行空格方便阅读
def addLineEvery2Lines(text):
    NewTextList = []
    AllLinesNumber = 0
    for Line in text.split('\n'):
        AllLinesNumber += 1
        NewTextList.append(Line)
        if AllLinesNumber % 2 == 0:
            NewTextList.append(' ')
    return '\n'.join(NewTextList)


class AccessToken:
    @staticmethod
    def _encode_text(text):
        encoded_text = parse.quote_plus(text)
        return encoded_text.replace('+', '%20').replace('*', '%2A').replace('%7E', '~')
    @staticmethod
    def _encode_dict(dic):
        keys = dic.keys()
        dic_sorted = [(key, dic[key]) for key in sorted(keys)]
        encoded_text = parse.urlencode(dic_sorted)
        return encoded_text.replace('+', '%20').replace('*', '%2A').replace('%7E', '~')
    @staticmethod
    def create_token(access_key_id, access_key_secret):
        parameters = {'AccessKeyId': access_key_id,
                      'Action': 'CreateToken',
                      'Format': 'JSON',
                      'RegionId': 'cn-shanghai',
                      'SignatureMethod': 'HMAC-SHA1',
                      'SignatureNonce': str(uuid.uuid1()),
                      'SignatureVersion': '1.0',
                      'Timestamp': time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                      'Version': '2019-02-28'}
        # 构造规范化的请求字符串
        query_string = AccessToken._encode_dict(parameters)
        print('规范化的请求字符串: %s' % query_string)
        # 构造待签名字符串
        string_to_sign = 'GET' + '&' + AccessToken._encode_text('/') + '&' + AccessToken._encode_text(query_string)
        print('待签名的字符串: %s' % string_to_sign)
        # 计算签名
        secreted_string = hmac.new(bytes(access_key_secret + '&', encoding='utf-8'),
                                   bytes(string_to_sign, encoding='utf-8'),
                                   hashlib.sha1).digest()
        signature = base64.b64encode(secreted_string)
        print('签名: %s' % signature)
        # 进行URL编码
        signature = AccessToken._encode_text(signature)
        print('URL编码后的签名: %s' % signature)
        # 调用服务
        full_url = 'http://nls-meta.cn-shanghai.aliyuncs.com/?Signature=%s&%s' % (signature, query_string)
        print('url: %s' % full_url)
        # 提交HTTP GET请求
        response = requests.get(full_url)
        if response.ok:
            root_obj = response.json()
            key = 'Token'
            if key in root_obj:
                token = root_obj[key]['Id']
                expire_time = root_obj[key]['ExpireTime']
                return token, expire_time
        print(response.text)
        return None, None
def getAliyunToken():
    access_key_id2 = 'EZ33JpGvHcmN'
    access_key_id1 = str('LTAI5tF244AK')
    access_key_id = access_key_id1 + access_key_id2
    access_key_secret = str('CFVFZD15582qycr') + 'vW8l74YsrDkoVh2'
    token, expire_time = AccessToken.create_token(access_key_id, access_key_secret)
    print('token: %s, expire time(s): %s' % (token, expire_time))
    return token

