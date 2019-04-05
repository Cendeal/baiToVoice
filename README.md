# baiToVoice Package
>基于百度语音合成开发的，可以更加简单的使用百度语音合成的，生成你需要的语音mp3文件或者二进制数据

#### 功能

官网的有限制文本转换的最大值为1024字节，bai的功能主要是完成了大文本的分割以及合并，所以不用担心文本的大小，使用即可，另外也数据的方式有两种呈现，第一种是保存MP3文件的到本地，另一种就是返回的是二进制数据，可以供网络直接传输使用。还有这里默认提供了作者的appId,appKey及secretKey给那些非开发人员使用的，不用去申请一个开发账号之类的繁琐步骤，快速体验一下百度语音合成的有趣。

#### 使用

##### 1.安装

```
pip install baiToVoice
```

##### 2.文本转MP3语音文件

```
from baiToVoice import BaiVoice
import os
# 这里使用的是作者自己的appId,appKey及secretKey，建议正式开发不要使用默认的，请调用
# BaiVoice(appId, appKey,secretKey)
bai_voice = BaiVoice()
# 保存MP3文件
bai_voice.translate_output_mp3_file('''
风雨
唐代：李商隐
凄凉宝剑篇，羁泊欲穷年。
黄叶仍风雨，青楼自管弦。
新知遭薄俗，旧好隔良缘。
心断新丰酒，销愁斗几千。
''','fengyu.mp3')
os.system('fengyu.mp3')
```

##### 3.文本返回音频二进制数据

```
# text是文本内容
bai_voice.translate_to_content_bytes(text)
```

##### 4.修改合成语音的声音风格

```
bai_voice.change_voice_style(可选参数):
spd:设置语速，取值范围是0-9。
pit: 设置语调，取值范围是0-9。
vol:设置音量，取值范围是0-15。
per:发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫。
```

##### 5.项目地址

[baiToVoice](https://github.com/Cendeal/baiToVoice)