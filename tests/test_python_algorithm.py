#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `python_algorithm` package."""


import unittest
from click.testing import CliRunner

from python_algorithm import python_algorithm
from python_algorithm import cli


class TestPython_algorithm(unittest.TestCase):
    """Tests for `python_algorithm` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'python_algorithm.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
