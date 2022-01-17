#!/bin/bash

wget http://drugdesign.unistra.fr/LIT-PCBA/Files/full_data.tgz -O lit-pcba.tgz
mkdir -p lit-pcba/
tar -xvf lit-pcba.tgz -C lit-pcba
rm lit-pcba.tgz