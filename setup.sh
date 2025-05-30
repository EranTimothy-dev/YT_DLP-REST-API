#!/bin/bash

set -e # exit on error

VENV_DIR = ".venv"

echo "Setting up FastAPI project"
echo "Checking for virtual environment"

if [ ! -d "$VENV_DIR"]; then
    echo "Creating virtual environment"
    if [ $OSTYPE == "msys" || $OSTYPE == "cygwin" ]; then
        python -m venv $VENV_DIR
        echo "created windows virtual environment"
    else
        python3 -m venv $VENV_DIR
        echo "created linux virtual environment"
    fi
else
    echo "Virtual environment exists"
fi

echo "Activating virtual environment"
if [$OSTYPE == "msys" || $OSTYPE == "cygwin" ]; then
    source $VENV_DIR/Scripts/activate
    echo "Activated windows virtual environment"
else
    source $VENV_DIR/bin/activate
    echo "Activated linux virtual environment"
fi

echo "Installing package in editable mode"
pip install -e .

if [ -f "requirements.txt" ]; then
    if [$OSTYPE == "msys" || $OSTYPE == "cygwin" ]; then
        echo "Installing requirements"
        pip install -r requirements.txt
    else
        pip3 install -r requirements.txt
    fi
else
    echo "No requirements file found"
fi

echo "Setup complete! you can now lauch the python server"


