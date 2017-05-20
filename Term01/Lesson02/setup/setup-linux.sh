#!/bin/bash

mkdir -p ~/project/nd889

mkdir -p ~/project/nd889/download

# https://www.continuum.io/downloads
cd ~/project/nd889/download
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh

# Udacity nd889 > Lesson 2 > 8. Your conda...
cd ~/project/nd889/download
wget https://d17h27t6h515a5.cloudfront.net/topher/2017/January/588297be_aind-environment-unix/aind-environment-unix.yml

PATH="${HOME}/anaconda3/bin:${PATH}"

cd ~/project/nd889/download
conda env create -f aind-environment-unix.yml
