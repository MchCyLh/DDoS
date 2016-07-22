#!/usr/bin/env bash

TOOL=./tools/UriDict.py
FILENAME_URI_DICT=./data_middle/uridict.txt
FILENAME_INPUTS=(./data_middle/transform_log_lab.txt ./data_middle/transform_log_sysu.txt)

python $TOOL $FILENAME_URI_DICT ${FILENAME_INPUTS[*]}

echo 'Done!'

