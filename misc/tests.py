class onFiles:
  def __init__(self):
    pass
  def addHeader(self,folderDir):
    headerFolder=os.listdir(folderDir)
    for i in headerFolder:
      if isFile(i):pass
      #else:
extencions={".py":{"header":"#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n","comentLine":"#"}}
def recusrsiveSearch(folderDir,exts:list,proyectName="",ownerName=""):
  header=""
  headerFolder=os.listdir(folderDir)
  for i in headerFolder:
    if os.path.isFile(i):
      extencion= len(i)-i[::-1].index(".")-1
      header+=extencions[extencion]["header"]
      if proyectName!="" and ownerName!="":
        header+=extencions[extencion]["comentLine"]+proyectName+" - by "+ownerName+"\n"
      elif proyectName=="" and ownerName!="":
        header+=extencions[extencion]["comentLine"]+"by "+ownerName+"\n"
      elif proyectName!="" and ownerName=="":
        header+=extencions[extencion]["comentLine"]+"--"+proyectName+"--\n"
      else:
        pass
    else:
      recusrsiveSearch(folderDir,exts,proyectName,ownerName)
#recusrsiveSearch(folderDir,exts,"cul","jero98772")#to test