# -*- coding: UTF-8 -*-

'''
 Module
     read_template.py
 Copyright
     Copyright (C) 2020 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_unnamed_pipe is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by the
     Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_unnamed_pipe is distributed in the hope that it will be useful, but
     WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Defined class ReadTemplate with attribute(s) and method(s).
     Created API for read a template file and return a content.
'''

import sys
from os.path import isdir, dirname, realpath

try:
    from gen_unnamed_pipe.pro.config import ProConfig
    from gen_unnamed_pipe.pro.config.template_dir import TemplateDir
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2020, https://vroncevic.github.io/gen_unnamed_pipe'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_unnamed_pipe/blob/dev/LICENSE'
__version__ = '1.0.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ReadTemplate(FileChecking, TemplateDir):
    '''
        Defined class ReadTemplate with attribute(s) and method(s).
        Created API for read a template file and return a content.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | TEMPLATE_DIR - template dir path.
                | __template_dir - absolute file path of template dir.
            :methods:
                | __init__ - initial constructor.
                | read - read a template and return a string representation.
                | __str__ - dunder method for ReadTemplate.
    '''

    GEN_VERBOSE = 'GEN_UNNAMED_PIPE::PRO::READ_TEMPLATE'
    TEMPLATE_DIR = '/../conf/template/'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        TemplateDir.__init__(self, verbose=verbose)
        verbose_message(ReadTemplate.GEN_VERBOSE, verbose, 'init reader')
        pro_template_dir = '{0}{1}'.format(
            dirname(realpath(__file__)), ReadTemplate.TEMPLATE_DIR
        )
        if isdir(pro_template_dir):
            self.template_dir = pro_template_dir

    def read(self, config, unp_type, verbose=False):
        '''
            Read a templates and return a content.

            :param config: parameter file name.
            :type config: <dict>
            :param unp_type: parameter UNP type.
            :type unp_type: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: template content list | empty list.
            :rtype: <list>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:config', config), ('str:unp_type', unp_type)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        templates, modules, loaded_templates = None, None, []
        for configuration in config[ProConfig.TEMPLATES]:
            if unp_type in configuration:
                templates = configuration[unp_type]
        for configuration in config[ProConfig.MODULES]:
            if unp_type in configuration:
                modules = configuration[unp_type]
        for template_file, module_file in zip(templates, modules):
            template_content, template_file_path = None, None
            template_file_path = '{0}{1}/{2}'.format(
                self.template_dir, unp_type, template_file
            )
            self.check_path(file_path=template_file_path, verbose=verbose)
            self.check_mode(file_mode='r', verbose=verbose)
            self.check_format(
                file_path=template_file_path, file_format=ProConfig.FORMAT,
                verbose=verbose
            )
            if self.is_file_ok():
                with open(template_file_path, 'r') as template_module:
                    template_content = template_module.read()
                    loaded_templates.append({module_file: template_content})
        return loaded_templates

    def __str__(self):
        '''
            Dunder method for ReadTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            TemplateDir.__str__(self)
        )
