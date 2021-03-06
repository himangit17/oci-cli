# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

import unittest
from tests import util


class TestIntegration(unittest.TestCase):
    def setUp(self):
        pass

    def test_integration_instance_change_compartment(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'change-compartment'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_delete(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'delete'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_get(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'get'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output

    def test_integration_instance_update(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'update'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output
        result = util.invoke_command(
            ['integration', 'integration-instance', 'update', '--type'])
        assert 'Error: --type option requires an argument' in result.output

    def test_integration_instance_create(self):
        result = util.invoke_command(
            ['integration', 'integration-instance', 'create', '--type'])
        assert 'Error: --type option requires an argument' in result.output

    def test_work_request_list(self):
        result = util.invoke_command(
            ['integration', 'work-request', 'list'])
        assert 'Error: Missing option(s)' in result.output
        assert '--id' in result.output
