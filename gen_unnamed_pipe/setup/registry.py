# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Encapsulates core gen_unnamed_pipe components for simplification of gen_unnamed_pipe bundle.
'''

from __future__ import annotations

from ats_utilities.base.setup.bundle import BaseBundle

from gen_unnamed_pipe.core.service.iservice import IService
from gen_unnamed_pipe.core.service.isubprocessor import ISubProcessor
from gen_unnamed_pipe.infrastructure.cli.icli import ICLI
from gen_unnamed_pipe.setup.bundle import GenUnnamedPipeBundle
from gen_unnamed_pipe.setup.validator import GenUnnamedPipeBundleValidator
from gen_unnamed_pipe.setup.keys import GenUnnamedPipeBundleKeys
from gen_unnamed_pipe.setup.dependencies import GenUnnamedPipeBundleDependencies
from gen_unnamed_pipe.setup.dep_validator import GenUnnamedPipeBundleDependenciesValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2026, https://vroncevic.github.io/gen_unnamed_pipe'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_unnamed_pipe/blob/dev/LICENSE'
__version__ = '1.0.5'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenUnnamedPipeBundleRegistry:
    '''
        Encapsulates core gen_unnamed_pipe components for simplification of gen_unnamed_pipe bundle.

        It defines:

            :methods:
                | create_bundle - Creates the gen_unnamed_pipe bundle.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenUnnamedPipeBundleDependencies) -> GenUnnamedPipeBundle:
        '''
            Creates the gen_unnamed_pipe bundle.

            :param dependencies: The gen_unnamed_pipe bundle dependencies.
            :return: The gen_unnamed_pipe bundle.
            :exceptions:
                | ATSValueError: The gen_unnamed_pipe bundle dependencies must be provided and have proper values.
                | ATSTypeError:  The gen_unnamed_pipe bundle dependencies must be an instance of Mapping and its
                |                attributes must be instances of their respective types.
                | ATSValueError: The gen_unnamed_pipe bundle must be provided and have proper values.
                | ATSTypeError:  The gen_unnamed_pipe bundle must be an instance of GenUnnamedPipeBundle and
                |                its attributes must be instances of their respective types.
        '''
        GenUnnamedPipeBundleDependenciesValidator.validate(dependencies)

        base: BaseBundle | None = dependencies.get(GenUnnamedPipeBundleKeys.DEPENDENCY_BASE) if dependencies else None
        service: IService | None = dependencies.get(GenUnnamedPipeBundleKeys.DEPENDENCY_SERVICE) if dependencies else None
        subprocessor: ISubProcessor | None = dependencies.get(GenUnnamedPipeBundleKeys.DEPENDENCY_SUBPROCESSOR) if dependencies else None
        cli: ICLI | None = dependencies.get(GenUnnamedPipeBundleKeys.DEPENDENCY_CLI) if dependencies else None

        bundle: GenUnnamedPipeBundle = GenUnnamedPipeBundle(base=base, service=service, subprocessor=subprocessor, cli=cli)

        GenUnnamedPipeBundleValidator.validate(bundle)

        return bundle
