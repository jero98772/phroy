from tools.tools import farguments,generatorBase

def main():
  arguments=farguments()
  if arguments.size == "small":
    g=generatorBase(arguments.proyectName,arguments.author,arguments.programmingLanguage)
    g.programingLangueFile()
    g.structureFiles()
  if arguments.size == "medium":
    print("medium")
if __name__=='__main__':
  main()