#!/bin/bash

# Setup virtual environment
python3 -m venv venv

# Activate virtual environment
venv/bin/activate

# install dependencies
pip install -r requirements.txt