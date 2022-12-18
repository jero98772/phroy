#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#phory - by jero98772
from tools.tools import farguments,generatorBase,medium,bigProyect,flaskWebProyect,flaskWebBigProyect,goweb,competitivePrograming
def main():
  arguments=farguments()
  if arguments.type == "main":
    g=generatorBase(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "medium":
    g=medium(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "big":
    g=bigProyect(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "flask":
    g=flaskWebProyect(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "flaskBig":
    g=flaskWebBigProyect(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "goweb":
    g=goweb(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.type == "cp":
    g=competitivePrograming(arguments.proyectName,arguments.url)
    g.structureFiles(arguments.numberofproblems)
  print("proyect "+arguments.proyectName+" was create successfully")
if __name__=='__main__':
  main()