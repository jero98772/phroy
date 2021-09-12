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
  parser.add_argument("-a","--author",type=str,default="me",help="name of who did it")
  parser.add_argument("-l","--programmingLanguage",type=str,default="python",help="programming language for init files")
  return parser.parse_args()
def createFile(name,content):
  with open(name, 'w') as file:
    file.write(content)
    file.close()
class generatorBase:
  def __init__(self,name,author,programingLangue):
    self.name=name
    self.author=author
    self.pl=programingLangue
    self.readmeTemplate = f"""
# {name}

### features 
### Screenshots
### Installing
**Download repositories**

    git clone https://github.com/{author}/{name}.git

**Run:**  

### Made for:
#### Ethical purpose
#### Non-ethical purpose
"""
  def programingLangueFile(self):
    if self.pl == "python":
      self.mainFile=f"""#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#{self.name} - by {self.author}
def main():
  pass;'''some code here'''
if __name__=='__main__':
  main()
"""
      self.extencion=".py"
    if self.pl == "java":
      self.mainFile=f"//{self.name} - by {self.author}\n"+f"class {self.name} "+"{\n    public static void main(String[] args) {\n        System.out.println();\n     }\n}"
      self.extencion=".java"
    else:
      print(self.pl+" no prescribed code was found to generate a project in that language. add it if you like.")
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/misc")
    createFile(self.name+"/""readme.md",self.readmeTemplate)
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
