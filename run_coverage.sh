#!/bin/bash
#
# @brief   gen_unnamed_pipe
# @version 1.0.9
# @date    Sun Aug 09 08:09:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_unnamed_pipe
pylint gen_unnamed_pipe > gen_unnamed_pipe.report
echo "Done"
