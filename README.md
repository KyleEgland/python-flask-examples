# Python - Flask Examples
Collection of examples pertaining to Flask

## Synopsis
I've consumed quite a few tutorials while creating projects and therefore have created numerous Flask repositories all over the place (in version control, local machines, etc.). This project is meant to be a culmination of those efforts that may be reviewed and updated as I evolve as a programmer. This project has been built upon the work of many other brilliant and hardworking people who's efforts have been given credit in the `Credits` section. Additionally, this project is a representation of my capability to assimilate all these ideas into one project and demonstrate my own learning capability.

## Objectives

* Create a Flask Application that may serve as an example of best-practices, design patterns, and modularity which utilizes current technology and principles.
    * Secure API for front-end user interaction with app provided data
    * Single-page CRUD application, consuming internal API
    * Single-page application consuming a third-party API

## Getting Started
I am accepting contributions to this project, however, please feel free to copy it as you see fit in order to further your own learning.  Please find below some brief instruction on how to get this repository, start an environment, and run your own development server.

__Prerequisites:__
* Git ([git site](https://git-scm.com/))
* Python 3 ([Python](https://www.python.org/))
* virtualenv Python module (`$ python -m pip install virtualenv`)

1. Clone the [repository](https://github.com/KyleEgland/python-flask-examples.git)

`user@machine:~/workspace$ git clone https://github.com/KyleEgland/python-flask-examples.git`

2. Create the project virtualenv

`user@machine:~/workspace/python-flask-examples$ python -m virtualenv env`

_Note: This action will create a Python virtual environment in the current working directory. Ensure, when issuing this commnad, that the current working directory is the one in which the project resides - [virtualenv docs](https://virtualenv.pypa.io/en/latest/)._

3. Activate the virtual environment and install required Python modules

_Linux_

`user@machine:~/workspace/python-flask-examples$ source ./env/bin/activate`

_Windows_

`C:\Users\user\workspace\python-flask-examples> . .\env\Scripts\activate`

_Install dependencies (all systems)_

`(env) user@machine:~/workspace/python-flask-examples$ python -m pip install -r requirements.txt`

4. Create the environment file (see documentation) and run application

`(env) user@machine:~/workspace/python-flask-examples$ python -m flask run`

_End application with `ctrl + c`_

## Other Technologies
This section is meant to talk briefly about the technologies (aside from Python and, subsequently, Flask) used to create this project.  Most (if not all) third party libraries have been included here because I didn't want to pull cross-site.

__Bootstrap__ creates the styling seen within the application.  Bootstrap has additional dependencies of Popper-js and jQuery (both bundled in the `~/app/static/bootstrap` directory). Everything kept within this project was working at the time of creation, however, that doesn't mean it is the latest - please ensure (should you choose to use this code) that you check for any known vulnerabilities in these packages (I'm looking at you jQuery...).

__Fontawesome__ provides iconography for the project.

## Credits
There are, generally, a lot of online resources that I use to accomplish my coding tasks.  Should you find anything is the repository useful, please patronize these additional resources or, at the very least, credit them in your own work if you clone/fork this for your own purposes.

* [Using jQuery to Update a Page Without Refresh (Part 1 of 2)](https://youtu.be/Kcka5WBMktw) by [Pretty Printed](https://prettyprinted.com/)
* [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by [Miguel Grinbert](https://blog.miguelgrinberg.com/index)
* [Reset CSS Stylesheet](http://html5doctor.com/html-5-reset-stylesheet/)
* [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/download/)
* [Popper.js](https://popper.js.org/)
    * _Bootstrap dependency_
* [Fontawesome](https://fontawesome.com/)
