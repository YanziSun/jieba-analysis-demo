#!/usr/bin/env python
# coding=utf-8

from jpype import *
import sys
import os
reload(sys)

sys.setdefaultencoding('utf-8')


def init():
    #jarpath = os.path.join(os.path.abspath('.'),'jieba-analysis-1.0.2.jar')
    jarpath = os.path.join(os.path.abspath('.'),'jieba-analysis-1.0.3-mdf-1.0.1.jar')
    startJVM(getDefaultJVMPath(), "-ea","-Djava.class.path=%s" % jarpath)

def loaddict():
    WordDictionary = JClass('com.huaban.analysis.jieba.WordDictionary')
    instance=WordDictionary.getInstance()
    Paths=JClass('java.nio.file.Paths')
    Pt=JPackage('java').nio.file
    Paths=Pt.Paths
    instance.init(java.nio.file.Paths.get("./userdict",""))

def process(text,flag):
    JiebaSegmenter = JClass('com.huaban.analysis.jieba.JiebaSegmenter')
    SegMode = JClass('com.huaban.analysis.jieba.JiebaSegmenter$SegMode')
    #loaddict()
    segmenter = JiebaSegmenter(); 
    if flag==1:
        return segmenter.process(text,SegMode.SEARCH);
    else:
        return segmenter.process(text,SegMode.INDEX);
    
def cut_index(text):
    if not text.strip():
        return
    tokens=process(text,0)
    for t in tokens:
        strt=str(t)
        i=strt.index(",")
        j=strt[1:i]
        if j:
            yield j

def cut_search(text):
    if not text.strip():
        return
    tokens=process(text,1)
    for t in tokens:
        strt=str(t)
        i=strt.index(",")
        j=strt[1:i]
        if j:
            yield j

def shutdown():
    shutdownJVM()

def all(text):
    init()
    cut(text)
    shutdown()

if __name__ == '__main__':
    init()
    shutdown()
