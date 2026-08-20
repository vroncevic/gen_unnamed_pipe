# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
Info
    Unit tests for GenUnnamedPipeBundleFactory class.
'''

from __future__ import annotations

import unittest

from gen_unnamed_pipe.setup.bundle import GenUnnamedPipeBundle
from gen_unnamed_pipe.setup.factory import GenUnnamedPipeBundleFactory


class TestGenUnnamedPipeBundleFactory(unittest.TestCase):

    def test_create_bundle_default(self) -> None:
        bundle = GenUnnamedPipeBundleFactory.create_bundle()
        self.assertIsInstance(bundle, GenUnnamedPipeBundle)

    def test_create_bundle_with_options(self) -> None:
        options = {'info_file': 'gen_unnamed_pipe/infrastructure/config/gen_unnamed_pipe.cfg'}
        bundle = GenUnnamedPipeBundleFactory.create_bundle(options)
        self.assertIsInstance(bundle, GenUnnamedPipeBundle)

    def test_create_bundle_invalid_options(self) -> None:
        options = {'info_file': 123}
        with self.assertRaises(Exception):
            GenUnnamedPipeBundleFactory.create_bundle(options)

    def test_get_version(self) -> None:
        self.assertEqual(GenUnnamedPipeBundleFactory.get_version(), '1.0.9')
