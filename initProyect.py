import argparse
import os
DESCRIPTION ="""
create template for proyects
run:
\n\tpython initProyect.py <Proyect name> [Options]
use -h/--help for more options 
"""
def farguments():
  parser = argparse.ArgumentParser(description=DESCRIPTION)
  parser.add_argument("proyectName")
  parser.add_argument("-s","--size",type=str,default="medium",help="scale of proyect (default: medium)  small,medium,big.")
  parser.add_argument("-l","--programmingLanguage",type=str,default="python",help="programming language for init files")
  parser.add_argument("-a","--author",type=str,default="jero98772",help="name of who did it")
  return parser.parse_args()
def createFile(name,content):
  with open(name, 'w') as file:
    file.write(content)
    file.close()
class genTemplate():
  def __init__(self,proyectName,size,programmingLanguage,author=""):
    self.name=proyectName
    self.language=programmingLanguage
    self.extencion=""
    self.user=author
    self.size=size
  def programmingLanguages():
    """
    return programming language extencion ,run with, installing depencies and chose setup file
    """
    if self.language=="python":
      self.extencion=".py"
      self.runOnTerminal="python "+str(name)+self.extencion
      if this.size=="small":
        self.mainFile=f"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#{self.name} - by {self.user}
def main():
  pass;'''some code here'''
if __name__=='__main__':
  main() self.size
        """
    return languageTags
  def readmeTemplate(name,preparations="\n",user=""):
    return f"""
# {name}

### features 
### Screenshots
### Installing
**Download repositories**

  git clone https://github.com/{user}/{name}.git

**Run:**  
  
  {self.runOnTerminal}

### Made for:
#### Ethical purpose
#### Non-ethical purpose
"""
  def smallProyect(self):
    os.mkdir(name)
    os.mkdir(name+"/misc")
    createFile("readme.md",readmeTemplate(name,user="jero98772"))
    createFile(name+self.extencion,content)
#def installDepenciesTemplate():
#def mediumProyect():
#def bigProyect():
#add mi lib
  def generate(self):
    if self.size=="small":
      smallProyect()
def main():
  arguments=farguments()
  template=genTemplate(arguments.proyectName,arguments.author,arguments.programmingLanguage)
  if arguments.size == "small":
    smallProyect(name)
  print(arguments.proyectName)
main()
