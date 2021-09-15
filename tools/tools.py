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
  parser.add_argument("-s","--size",type=str,default="medium",help="scale of proyect (default: medium)  small,medium,big,flaskBig.")
  parser.add_argument("-a","--author",type=str,default="me",help="name of who did it")
  parser.add_argument("-l","--programmingLanguage",type=str,default="python",help="programming language for init files(defualt: python,only suported now)")
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
    self.readmeTemplate = f"""# {name}
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
      self.header=f"""#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#{self.name} - by {self.author}"""
      self.mainFile=self.header+f"""
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
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
class medium(generatorBase):
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/tools")
    os.mkdir(self.name+"/misc")
    os.mkdir(self.name+"/misc/screenshots")
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/misc/todos.org","* TODO´S")
    createFile(self.name+"/tools/tools"+self.extencion,self.header)
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
class bigProyect(generatorBase):
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/core")
    os.mkdir(self.name+"/data")
    os.mkdir(self.name+"/docs")
    os.mkdir(self.name+"/core/tools")
    createFile(self.name+"/docs/todos.org","* TODO´S")
    createFile(self.name+"/docs/Notes.org","* Notes")    
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/core/tools/__init__"+self.extencion,self.header)
    createFile(self.name+"/core/tools/tools"+self.extencion,self.header)
    createFile(self.name+"/core/main"+self.extencion,self.header)    
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
class flaskWebProyect(generatorBase):
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/core")
    os.mkdir(self.name+"/data")
    os.mkdir(self.name+"/docs")
    os.mkdir(self.name+"/core/tools")
    os.mkdir(self.name+"/core/templates")
    os.mkdir(self.name+"/core/static")
    os.mkdir(self.name+"/core/static/js")
    os.mkdir(self.name+"/core/static/css")
    os.mkdir(self.name+"/core/static/img")
    createFile(self.name+"/docs/todos.org","* TODO´S")
    createFile(self.name+"/docs/Notes.org","* Notes")
    createFile(self.name+"/core/templates/index.html",self.indexFile)
    createFile(self.name+"/core/templates/template.html",self.templateFile)
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/core/tools/__init__"+self.extencion,self.header)
    createFile(self.name+"/core/tools/tools"+self.extencion,self.header)
    createFile(self.name+"/core/main"+self.extencion,self.mainFile)    
    createFile(self.name+"/"+self.name+self.extencion,self.runFile)
  def programingLangueFile(self):
    self.indexFile ="""
{% extends  'template.html'%}
{% block content %} 
   
{% endblock  %}
"""
    self.templateFile =f"<h1>{self.name}</h1>"+"""
<hr>
{% block content %}

{% endblock %}
"""
    if self.pl == "python":
      self.header=f"""#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#{self.name} - by {self.author}
"""
      self.mainFile=self.header+f"""
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
class webpage():
  @app.route()
  def index():
    return render_template("index.html")
      """
      self.runFile=self.header+f"""
from core.main import webpage
from core.main import app
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
"""
      self.extencion=".py"
    else:
      print(self.pl+" no prescribed code was found to generate a project in that language. add it if you like.")
