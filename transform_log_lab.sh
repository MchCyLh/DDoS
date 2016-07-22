#!/usr/bin/env bash

TOOL=./tools/TransformLog.py
FILENAME_INPUT=./data_input/log_lab.txt
FILENAME_MIDDLE=./data_middle/transform_log_lab.txt
MODE=LAB

python $TOOL $MODE $FILENAME_INPUT $FILENAME_MIDDLE

echo 'Done!'

