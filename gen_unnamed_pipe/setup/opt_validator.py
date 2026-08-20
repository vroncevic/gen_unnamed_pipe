# -*- coding: UTF-8 -*-

'''
Module
    opt_validator.py
Copyright
    Copyright (C) 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_unnamed_pipe is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_unnamed_pipe is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Validator for the gen_unnamed_pipe bundle options.
'''

from __future__ import annotations

from collections.abc import Mapping

from ats_utilities.validation.check_type import istype
from ats_utilities.exceptions import ATSValueError, ATSTypeError
from ats_utilities.validation.check_value import not_none

from gen_unnamed_pipe.setup.options import GenUnnamedPipeBundleOptions
from gen_unnamed_pipe.setup.keys import GenUnnamedPipeBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_unnamed_pipe'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_unnamed_pipe/blob/dev/LICENSE'
__version__ = '1.0.9'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenUnnamedPipeBundleOptionsValidator:
    '''
        Validator for the gen_unnamed_pipe bundle options.

        It defines:

            :methods:
                | validate - Validates the gen_unnamed_pipe bundle options.
                | is_valid - Checks if the gen_unnamed_pipe bundle options is valid.
    '''

    @classmethod
    def validate(cls, options: GenUnnamedPipeBundleOptions) -> None:
        '''
            Validates the gen_unnamed_pipe bundle options.

            :param options: The gen_unnamed_pipe bundle options to be validated.
            :exceptions:
                | ATSValueError: The gen_unnamed_pipe bundle options must be provided and have proper values.
                | ATSTypeError:  The gen_unnamed_pipe bundle options must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
        '''
        ctx: str = 'gen_unnamed_pipe_bundle_options_validator::validate(...)'
        msg_options_none: str = 'the gen_unnamed_pipe bundle options must be provided'
        msg_options_istype: str = 'the gen_unnamed_pipe bundle options must be a Mapping'

        not_none(options, ctx, msg_options_none)
        istype(options, Mapping, ctx, msg_options_istype)

        for attr_name, expected_type in GenUnnamedPipeBundleKeys.get_option_to_type().items():
            msg_attr_name_istype: str = f'the {attr_name.replace("_", " ")} must be an instance of {expected_type.__name__}'

            attribute = options.get(attr_name)

            istype(attribute, expected_type, ctx, msg_attr_name_istype)

    @classmethod
    def is_valid(cls, genunnamedpipebundleoptions: GenUnnamedPipeBundleOptions) -> bool:
        '''
            Checks if the genunnamedpipebundleoptions is valid.

            :param genunnamedpipebundleoptions: The genunnamedpipebundleoptions to be checked.
            :return: True if valid, False otherwise.
        '''
        try:
            cls.validate(genunnamedpipebundleoptions)
            return True

        except (ATSValueError, ATSTypeError):
            return False
