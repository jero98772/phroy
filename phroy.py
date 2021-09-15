
#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#phory - by jero98772
from tools.tools import farguments,generatorBase,medium,bigProyect,flaskWebProyect
def main():
  arguments=farguments()
  if arguments.size == "small":
    g=generatorBase(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.size == "medium":
    g=medium(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.size == "big":
    g=bigProyect(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.size == "flaskBig":
    g=flaskWebProyect(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  print("proyect "+arguments.proyectName+" was create successfully")
if __name__=='__main__':
  main()