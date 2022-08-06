#!/bin/bash

for file in $(ls scripts/usuario*.json); do python main.py $file; done
for file in $(ls scripts/ong*.json); do python main.py $file; done
for file in $(ls scripts/doacao*.json); do python main.py $file; done
