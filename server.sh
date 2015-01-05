#!/bin/bash

PYTHONDONTWRITEBYTECODE=" " \
python -m bottle --debug --reload mikan:app
