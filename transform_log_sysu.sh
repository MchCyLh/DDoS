#!/usr/bin/env bash

TOOL=./tools/TransformLog.py
FILENAME_INPUT=./data_input/log_sysu.txt
FILENAME_MIDDLE=./data_middle/transform_log_sysu.txt
MODE=SYSU

python $TOOL $MODE $FILENAME_INPUT $FILENAME_MIDDLE

echo 'Done!'

