# Python - Flask Examples - Application Configuration
Configuration elements of the Flask Examples project.

## Overview
This application uses an environment file (`.env` in root directory) from which to pull various configuration elements (such as DB config, secret keys, etc.). This information should not be synced with version control as some or all of its contents could lead to security compromises and bad habbits (don't save secrets in plain text in public!). Additionally, this project utilizes the `python-dotenv` module to access the environment file. The application pulls this information in through the `config.py` file to give the Flask application the information necessary to start.  The following sections contain inforamtion regarding the `.env` file and how configuration (including logging) is done throughout the application.

### Environment File
Using `python-dotenv` the application reads in the `.env` file to set needed environment variables (secret keys, etc.). This file is intentionally not synced with source control as it is intended to hold secrets and other variables that change from deployment-to-deployment (I.e. product v development). Therefore, everytime this project is pulled (for the first time that is) to a machine a `.env` file must be created before the application will run successfully. The environment file shall be placed in the root of the project directory: `~/workspace/python-flask-examples/.env`. The contents of the environment file, explanations, and an example that may be copied can be found in the `flask-python-examples/Documents/Examples/` directory.

__Notes:__
* The env file shouldn't be saved to source control!
* An env file is required before the app will run
* Copy the example for a quick start
* Don't re-use secrets that are self generated (I.e. SECRET_KEY)

### Configuration deployment
The application begins by calling `app_start.py` which imports the application (`~/app`). The `__init__.py` file is run which imports the `Config` from `config.py` (which is in the root of the project). Importing the `Config` class then initializes the `config.py` file which:

* Loads the `.env` file via `python-dotenv`
* Checks for and subsequently creates the log directory (if it doesn't already exist)
* Sets the environment variables within the configuration class

The variables that are set through the config class are subsequently consumed by the Flask application (loaded via the `create_app` function inside `~/app/__init__.py`).