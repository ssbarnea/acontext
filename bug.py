#!/usr/bin/env python
# Reproducer for https://github.com/ansible/ansible/issues/69758
# Based on API example from https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html

import os  # noqa

# Uncommenting next line make is find the module!
# os.environ['ANSIBLE_LIBRARY'] = "modules"

from ansible.module_utils.common.collections import ImmutableDict
from ansible import context
from ansible.parsing.mod_args import ModuleArgsParser

# since the API is constructed for CLI it expects certain options to always be set in the context object
context.CLIARGS = ImmutableDict(connection='local', module_path=['modules'], forks=10, become=None,
                                become_method=None, become_user=None, check=False, diff=False)

ModuleArgsParser({"fake_module": {"foo": "bar"}}).parse()
# ^ this should not fail as "fake_module" is present inside ./modules folder.
