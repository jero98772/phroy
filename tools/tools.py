import argparse
import os
from datetime import datetime
DESCRIPTION="""
create template for proyects
run:
\n\tpython initProyect.py <Proyect name> [Options]
use -h/--help for more options\n
Description:
type -t:\n
\t[option]:\t description
\t[main]:\t only main function in code
\t[medium]:\t a larger file structure for big scripts and functions
\t[big]:\t a larger file structure for production code

ProgrammingLanguage -l:\n
\t[option]:\t description
\t[main]:\t go,java,c++,python
\t[medium]:\t python
\t[big]:\t 
"""
def readtxtstr(name):
  """
  readtxtstr(name) , return txt content as string
  """
  content = ""
  with open(name, 'r') as file:
    for i in file.readlines():
      content += str(i)
  return content
def formatFile(name,author,code):
    """
    format templete file 
    """
    try:
      return code.format(name=name,author=author)
    except:
      code=code.replace("{name}",name)
      code=code.replace("{author}",author)
      return code
def formatFileCp(code,name,date,link=""):
    """
    format templete file for competitive programing
    """
    try:
      return code.format(name=name,date=date,link=link)
    except:
      code=code.replace("{date}",date)
      code=code.replace("{link}",link)
      code=code.replace("{name}",name)
      return code
def farguments():
  """
  configure arguments
  """
  parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=DESCRIPTION)
  parser.add_argument("proyectName")
  parser.add_argument("-t","--type",type=str,default="medium",help="scale of proyect (default: medium)  main,small,medium,big,flaskBig,flask,goweb.")
  parser.add_argument("-a","--author",nargs='?',type=str,default="me",help="name of who did it")
  parser.add_argument("-l","--programmingLanguage",nargs='?',type=str,default="python",help="programming language for init files(defualt: python)")
  parser.add_argument("-np","--numberofproblems",nargs='?',type=str,default="1",help="select amount of problem in the contest")
  parser.add_argument("-u","--url",type=str,default="",help="link of contest")

  return parser.parse_args()

def createFile(name,content):
  """
  create empty file
  """
  with open(name, 'w') as file:
    file.write(content)
    file.close()

class templatesNames:
  """
  variables of templates
  """
  def __init__(self):
    self.htmlJingaTemplate="templates/htmlJingaTemplate.html"
    self.htmlJingaIndex="templates/htmlJingaIndex.html"
    self.readmeMd="templates/readme.md"
    self.pythonMain="templates/pythonMain.py"
    self.javaMain="templates/javaMain.java"
    self.goMain="templates/goMain.go"
    self.goWeb="templates/goWeb.go"
    self.cppMain="templates/cppMain.cpp"
class generatorBase(templatesNames):
  def __init__(self,name,author,programingLangue):
    templatesNames.__init__(self)
    self.name=name
    self.author=author
    self.pl=programingLangue
    self.readmeTemplate=formatFile(self.name,self.author,readtxtstr(self.readmeMd))
  def programingLangueFile(self):
    if self.pl == "python" or self.pl=="py":
      self.header="#!/usr/bin/env python\n# -*- coding: utf-8 -*- \n#{name} - by {author}"
      self.mainFile=formatFile(self.name,self.author,readtxtstr(self.pythonMain))
      self.extencion=".py"
    if self.pl == "java":
      self.header=f"//{self.name} - by {self.author}\n"
      self.mainFile=formatFile(self.name,self.author,readtxtstr(self.javaMain))
      self.extencion=".java"
    if self.pl == "go":
      self.header=f"//{self.name} - by {self.author}\n"
      self.mainFile=formatFile(self.name,self.author,readtxtstr(self.goMain))
      self.extencion=".go"
    if self.pl == "cpp" or self.pl == "c++" :
      self.header=f"//{self.name} - by {self.author}\n"
      self.mainFile=formatFile(self.name,self.author,readtxtstr(self.cppMain))
      self.extencion=".cpp"
    else:
      print(self.pl+" no prescribed code was found to generate a project in that language. add it if you like.")
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/misc")
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
class flaskBase(generatorBase):
    def programingLangueFile(self):
      self.indexFile =readtxtstr(self.htmlJingaIndex)
      self.extencion=".py"
      self.templateFile =formatFile(self.name,self.author,readtxtstr(self.htmlJingaTemplate))
      self.header=f"#!/usr/bin/env python\n# -*- coding: utf-8 -*- \n#{self.name} - by {self.author}"
      self.mainFile=self.header+f"""
from flask import Flask, render_template, request, flash, redirect ,session
app = Flask(__name__)
class webpage():
  @app.route("/")
  def index():
    return render_template("index.html")
      """
      self.runFile=self.header+f"""
from core.main import webpage
from core.main import app
if __name__ == "__main__":
  app.run(debug=True,host="127.0.0.1",port=5000)
"""

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
class flaskWebBigProyect(flaskBase):
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
class flaskWebProyect(flaskBase):
  def structureFiles(self):
    os.mkdir(self.name)
    os.mkdir(self.name+"/tools")
    os.mkdir(self.name+"/templates")
    os.mkdir(self.name+"/static")
    os.mkdir(self.name+"/static/js")
    os.mkdir(self.name+"/static/css")
    os.mkdir(self.name+"/static/img")
    createFile(self.name+"/templates/index.html",self.indexFile)
    createFile(self.name+"/templates/template.html",self.templateFile)
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/tools/__init__"+self.extencion,self.header)
    createFile(self.name+"/tools/tools"+self.extencion,self.header)
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile+self.runFile[-77:])
class goweb(medium):
  """
  create file structure for web proyects in go, with html file, go files for tools and backend and others
  """
  def structureFiles(self):
    self.mainFile=formatFile(self.name,self.author,readtxtstr(self.goWeb))
    os.mkdir(self.name)
    os.mkdir(self.name+"/tools")
    os.mkdir(self.name+"/misc")
    os.mkdir(self.name+"/templates")
    os.mkdir(self.name+"/misc/screenshots")
    createFile(self.name+"/readme.md",self.readmeTemplate)
    createFile(self.name+"/misc/todos.org","* TODO´S")
    createFile(self.name+"/tools/tools"+self.extencion,self.header)
    createFile(self.name+"/templates/index.html",f"<!--{self.name} by {self.author}-->")
    createFile(self.name+"/"+self.name+self.extencion,self.mainFile)
class competitivePrograming():
    def __init__(self,name,link="",templatesPath="templates/competitivePrograming/"):
      self.ext=name[name.find("."):]
      self.name=name[:name.find(".")]
      self.alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      self.date=datetime.today().strftime("%d-%m-%Y")
      self.content=formatFileCp(readtxtstr(templatesPath+name),self.name,self.date,link=link)
    def structureFiles(self,numberproblems):
      folder=self.name+self.date
      os.mkdir(folder)
      for i in range(int(numberproblems)):
        createFile(folder+"/"+self.alphabet[i]+self.ext,self.content)

