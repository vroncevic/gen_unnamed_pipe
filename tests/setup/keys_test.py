# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
Info
    Unit tests for GenUnnamedPipeBundleKeys class.
'''

from __future__ import annotations

import unittest
from types import MappingProxyType

from gen_unnamed_pipe.setup.keys import GenUnnamedPipeBundleKeys


class TestGenUnnamedPipeBundleKeys(unittest.TestCase):

    def test_get_dependency_to_type(self) -> None:
        deps = GenUnnamedPipeBundleKeys.get_dependency_to_type()
        self.assertIsInstance(deps, MappingProxyType)
        self.assertIn(GenUnnamedPipeBundleKeys.DEPENDENCY_BASE, deps)
        self.assertIn(GenUnnamedPipeBundleKeys.DEPENDENCY_SERVICE, deps)
        self.assertIn(GenUnnamedPipeBundleKeys.DEPENDENCY_SUBPROCESSOR, deps)
        self.assertIn(GenUnnamedPipeBundleKeys.DEPENDENCY_CLI, deps)

    def test_get_option_to_type(self) -> None:
        opts = GenUnnamedPipeBundleKeys.get_option_to_type()
        self.assertIsInstance(opts, MappingProxyType)
        self.assertIn(GenUnnamedPipeBundleKeys.OPTION_INFO_FILE, opts)
