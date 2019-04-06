from setuptools import setup, find_packages

from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here.replace('\\','/'),"README.md"),encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='baiToVoice',
    version='1.2.2',
    author="Cendeal",
    author_email="1798062051@qq.com",
    description="基于百度语音合成开发的，可以更加简单的使用百度语音合成的，生成你需要的语音mp3文件或者二进制数据",
    long_description=long_description,
    long_description_content_type= "text/markdown",
    url="https://github.com/Cendeal/baiToVoice",
    keywords='baidu-aip 语音合成 百度语音 baiToVoice',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=['requests']
)