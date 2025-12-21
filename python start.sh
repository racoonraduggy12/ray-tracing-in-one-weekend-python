#!/bin/bash
cd "$( dirname "${BASH_SOURCE[0]}" )"
source venv/bin/activate
which python
echo python venv started, install modules to your hearts content
echo path is:
pwd
python raytracing-weekend.py > outputimage.ppm
