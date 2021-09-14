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
if __name__=='__main__':
  main()