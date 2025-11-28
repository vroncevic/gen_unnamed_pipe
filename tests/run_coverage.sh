#!/bin/bash
#
# @brief   gen_unnamed_pipe
# @version v1.0.1
# @date    Thu Jun 13 06:19:47 PM CEST 2024
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_unnamed_pipe_coverage.xml gen_unnamed_pipe_coverage.json .coverage
rm -rf mytool
python3 -m coverage run -m --source=../gen_unnamed_pipe unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_unnamed_pipe_coverage.xml 
python3 -m coverage json -o gen_unnamed_pipe_coverage.json
python3 -m coverage report --format=markdown -m
python3 ats_coverage.py -n gen_unnamed_pipe
rm htmlcov/.gitignore
echo "Done"