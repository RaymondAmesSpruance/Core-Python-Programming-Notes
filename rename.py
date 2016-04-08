# coding=utf-8

import sys  
import os  

def name():
    now_dir=os.getcwd();  
    files=os.listdir(now_dir) 
    inpath = 'Python核心编程第二、三章图片笔记'
    hahapath='CorePythonProgramming_PhotoNotesGallery_for_Charpter_1_&_2_'
    uipath = unicode(inpath , "utf8")
    count=1
    for file in files:
        os.rename(file,hahapath+str(count)+'.jpg') 
        count=count+1		
  
if __name__ == '__main__':  
    name()