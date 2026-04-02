#!/bin/bash

echo -e "\nstep1"
./parser.py tests/step1/invalid.json
./parser.py tests/step1/valid.json

echo -e "\nstep2"
./parser.py tests/step2/invalid.json
./parser.py tests/step2/invalid2.json
./parser.py tests/step2/valid.json
./parser.py tests/step2/valid2.json

echo -e "\nstep3"
./parser.py tests/step3/invalid.json
./parser.py tests/step3/valid.json

echo -e "\nstep4"
./parser.py tests/step4/invalid.json
./parser.py tests/step4/valid.json
./parser.py tests/step4/valid2.json

