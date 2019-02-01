#!/usr/bin/env bash

if [ "$(hostname)" == "r1n2.esss.dk" ]; then
    module load gcc/5.4.0  hdf5/1.10.2_gcc540
    git pull
fi
pipenv run ./x.py