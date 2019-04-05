# -*- coding: utf-8 -*-
from .speech import AipSpeech

"""
    baidu_ai_voice
    ~~~~
    这个主要依赖百度语音合成，可以将长的内容分块转换，合成语音MP3文件或者返回二进制语音内容，也可以切换不同的声音
"""


class BaiVoice:
    TEXT_MAX = 1023

    def __init__(self, appId='10890906', appKey='ZrniUsIZ7Y4ZaBrWv04Q7ax8',
                 secretKey='uKkOKxDZfK1KuTStszXcvmcAeYnggthb', lan='zh'):
        """
        这里使用的是Cendeal申请的appId,只用于测试或者非开发人员使用，建议如果你是使用于自己的应用，请自行到百度官网http://ai.baidu.com/tech/speech/tts申请属于自己的，一般调用次数是不限制的
        【注意这个默认的appId，appKey, secretKey是有可能会被删除的，也就是说会失效】
        :param appId: 
            百度云控制台中创建
        :type appId: str
        :param appKey: 
            百度云控制台中创建完毕应用后，系统分配给用户的
        :type appKey: str
        :param secretKey: 
            百度云控制台中创建完毕应用后，系统分配给用户的
        :type
        :param lan:
            语音合成语言默认zh
        :type lan: str
        """

        self.appId = appId
        self.appKey = appKey
        self.secretKey = secretKey
        self.lan = lan
        self.style = {'vol': 5, 'per': 0, 'pit': 5, 'spd': 5}
        self.client = AipSpeech(self.appId, self.appKey, self.secretKey)

    def change_voice_style(self, **kwargs):
        """
           该函数用于改变声音样式。
           :param spd:
               设置语速，取值范围是0-9。
           :type spd: string or integer
           :param pit:
               设置语调，取值范围是0-9。
           :type pit: string or integer
           :param vol:
               设置音量，取值范围是0-15。
           :type vol: string or integer
           :param per:
               发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫。
           :type per: string or integer
        """
        for k in self.style.keys():
            if k in kwargs:
                self.style[k] = kwargs[k]

    def translate_output_mp3_file(self, text, filename):
        # 输出mp3文件
        if filename.rfind('.mp3') < 0:
            filename += '.mp3'
        content = self.translate_to_content_bytes(text)
        if content is not None:
            with open(filename, 'wb') as w:
                w.write(content)
                return True
        return False

    def translate_to_content_bytes(self, text):
        res = b''
        count = len(text) // BaiVoice.TEXT_MAX + (1 if len(text) % BaiVoice.TEXT_MAX != 0 else 0)
        for i in range(0, count):
            content = text[i * BaiVoice.TEXT_MAX:BaiVoice.TEXT_MAX * i + (
                BaiVoice.TEXT_MAX if i < count - 1 else len(text) % BaiVoice.TEXT_MAX)]
            result = self.client.synthesis(content, self.lan, 1, self.style)
            if not isinstance(result, dict):
                res += result
            else:
                return None
        return res
