[![GitHub issues](https://img.shields.io/github/issues/xioperez01/AirBnB_clone?style=plastic)](https://github.com/xioperez01/AirBnB_clone/issues)
[![GitHub forks](https://img.shields.io/github/forks/xioperez01/AirBnB_clone?color=orange&style=plastic)](https://github.com/xioperez01/AirBnB_clone/network)
[![GitHub stars](https://img.shields.io/github/stars/xioperez01/AirBnB_clone?color=violet&style=plastic)](https://github.com/xioperez01/AirBnB_clone/stargazers)
# AirBnB_clone #
**A command interpreter to manage your AirBnB objects.**

This **AirBnB** clone consists of creating a shell to manage AirBnB objects.
As a command interpreter take the Shell example, but limited to a specific case. In this case, you want to be able to manage the project objects:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…)
* Update attributes of an object
* Destroy an object
## Directory content ##
| Directory Name | Description |
| ------------- |:-------------:|
| models | It contains everything corresponding to the creation and operation of the console |
| test | Contains the test cases with which the operation of the console was evaluated |
| web_static | Contains those corresponding to the creation of the web interface |
## How does it work? ##
### How to install it? :question: ###
To have this repository and its content, you must execute the following on your terminal:
~~~
$ git clone https://github.com/xioperez01/AirBnB_clone.git
$cd AirBnB_Clone
~~~
### How to use it? :question: ###
You can use it in interactive mode:
~~~
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
~~~
Or you can use it in non-interactive mode:
~~~
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
~~~
### Examples ###
* Execution:
~~~
$ ./console.py
*****************************
*                           *
*       Welcome :)          *
*                           *
*****************************

(hbnb) 
~~~
* Somme commands:
~~~
*****************************
*                           *
*       Welcome :)          *
*                           *
*****************************

(hbnb) help quit
Quit command to exit the program

(hbnb) create User
032c2cc0-9e74-4caf-8d48-13f7a304cf81
(hbnb)
~~~

**Now you know how to use it, have a happy coding :)**