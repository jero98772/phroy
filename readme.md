# phory

		     ρρρρρρρ   
		   ρρ    ρρρρ  
		  ρρ       ρρρ 
		  ρρ       ρρρ 
		  ρρ        ρρ 
		  ρρ        ρρ 
		  ρρ       ρρ  
		  ρρρ     ρρ   
		  ρρ ρρρρρ     
		  ρρ           
		  ρρ           
		 ρρρ           
		 ρρρ           

is a python project initializer, which organizes the initial structure and content of the project in different ways according to the required work and impact of the project, this is called project size, for cli.

		positional arguments:
	  proyectName

	options:
	  -h, --help            show this help message and exit
	  -t TYPE, --type TYPE  scale of proyect (default: medium) main,small,medium,big,flaskBig,flask,goweb.
	  -a [AUTHOR], --author [AUTHOR]
	                        name of who did it
	  -l [PROGRAMMINGLANGUAGE], --programmingLanguage [PROGRAMMINGLANGUAGE]
	                        programming language for init files(defualt: python)
	  -np [NUMBEROFPROBLEMS], --numberofproblems [NUMBEROFPROBLEMS]
	                        select amount of problem in the contest
	  -u URL, --url URL     link of contest

### Examples

build file structure of python flask

	python phroy.py <name> -s flask -a <author> -l python

build my file system

	python phroy.py <name> -s flaskBig -a <author> -l python


build file structure of go web code

	python phroy.py <name> -s goweb -a <author> -l go

prepare for a contest

	python phroy.py <teamname> -t cp -np <number of problems> -u <contest link>

prepare for a contest with my team

	python phroy.py appendice.cpp -t cp -np 20 -u https://codeforces.com/contest/1760

### Screenshots

![tree](https://raw.githubusercontent.com/jero98772/phroy/main/misc/screenshots/tree.png?token=ACZB27P5ELU2V2G3DR7KEUDBIIIPY)

![data](https://raw.githubusercontent.com/jero98772/phroy/main/misc/screenshots/data.png?token=ACZB27P5ELU2V2G3DR7KEUDBIIIPY)

![competitiveprograming](https://raw.githubusercontent.com/jero98772/phroy/main/misc/screenshots/competitiveprograming.png?token=ACZB27P5ELU2V2G3DR7KEUDBIIIPY)

### Installing
**Download repositories**

    git clone https://github.com/jero98772/phory.git

**Run:**  

	python phory.py <proyectName>

### Made for:

create python proyects for github repository automatically, to save time
