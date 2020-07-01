<h1><img src="images/hbnb img.png" alt="logo python" width="650" height="300"><br/><b>0x00. AirBnB clone - The console</b></h1>

[![contribuitors](https://img.shields.io/github/contributors/cbarros7/AirBnB_clone?style=plastic)](https://github.com/cbarros7/AirBnB_clone/graphs/contributors)
[![lisence](https://img.shields.io/github/license/cbarros7/AirBnB_clone?style=plastic)](https://github.com/cbarros7/AirBnB_clone/blob/master/LICENSE)
[![plattaforms](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1?color=%23EF7F1A&style=plastic)](https://www.powershellgallery.com/packages/DNS.1.1.1.1/0.0.7)
[![python versiion](https://img.shields.io/pypi/pyversions/3?color=%23EF7F1A&style=plastic)](https://www.python.org/download/releases/3.0/)

[![Twitter Jose](https://img.shields.io/twitter/follow/joseAVallejo12?label=JoseVallejo&style=social)](https://twitter.com/JoseAVallejo12)
[![Twitter Carlos](https://img.shields.io/twitter/follow/cbarros27?label=CarlosBarros&style=social)](https://twitter.com/cbarros27)

## **Background Context**
## **First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## **What’s a command interpreter?**
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## **Resources**
Read or watch: [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw), [packages](https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q), [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g), [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q), [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g), [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg), [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

### **Requirements Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").-MyClass.my_function.__doc__)')

### **Requirements Python Unit Tests**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
