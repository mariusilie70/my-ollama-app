#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt
python app/gui.py
