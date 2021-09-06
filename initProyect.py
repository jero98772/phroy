import argparse
import os
DESCRIPTION ="""
create template for proyects
run:
\tinitProyect.py <Proyect name> [Options]
use -h/--help for more options 
"""
def farguments():
  parser = argparse.ArgumentParser(description=DESCRIPTION)
  parser.add_argument('-h')
  parser.add_argument('--help')
  parser.add_argument('-s',type=str)
  parser.add_argument('-size',type=str)
  return parser.parse_args()

def readmeTemplate(name,):
	return f"""
# {name}

### features 
### Screenshots
### Installing
Download repo

	git clone https://github.com/jero98772/{name}.git

### Made for:
#### Ethical purpose
#### Non-ethical purpose
"""
def createFile(name,content):
  with open(name, 'w') as file:
    file.write(content)
    file.close()
def smallProyect(name):
  os.mkdir(name)
  os.mkdir(name+"/misc")
  createFile("readme.md",README)
  createFile("readme.md",content)
#def mediumProyect():
#def bigProyect():
#add mi lib
def help():
  return """
Usage:

python initProyect.py <Proyect name> [Options]
\t-s\tSize of proyect (default: medium) ")\n\t\t[1]small,\n\t\t[2]medium,\n\t\t[3]big.
"""
def main():
  arguments=farguments()
  proyectSize=sys.argv[1]
main()