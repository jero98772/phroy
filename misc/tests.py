class onFiles:
  def __init__(self):
    pass
  def addHeader(self,folderDir):
    headerFolder=os.listdir(folderDir)
    for i in headerFolder:
      if isFile(i):
      else:
extencions={".py":{"header":"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n","comentLine":"#"}}
def recusrsiveSearch(folderDir,exts:list,aditionalInfo=[]:list):
  header=""
  headerFolder=os.listdir(folderDir)
  for i in headerFolder:
    if os.path.isFile(i):
      extencion= len(i)-i[::-1].index(".")-1:
      header+=extencions[extencion]["header"]
      for ii in aditionalInfo:
        header+=extencions[extencion]["comentLine"]+ii+"\n"
    else:
      recusrsiveSearch(folderDir,exts,aditionalInfo)