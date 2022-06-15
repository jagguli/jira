from __future__ import absolute_import
from unittest import TestCase
from jira import JIRA
from jira.magics import JiraMagics
from mock import Mock
import pytest


@pytest.fixture(scope="function", autouse=True)  # Automatically use in tests.
def jira():
    basic_auth = (
        "steven@streethawk.com",
        "rhLozMA7hxc1oMULMgBs8AE3",
    )
    options = {'verify': True, 'server': 'https://streethawk.atlassian.net'}
    return JIRA(options=options, basic_auth=basic_auth, oauth=None)

def test_search(jira):
    magics = JiraMagics(None, jira)
    magics.search("sprint = 44")

def test_current_sprint(jira):
    magics = JiraMagics(None, jira)
    magics.current_sprint()

def test_show(jira):
    magics = JiraMagics(None, jira)
    magics.show('nick')

def test_mysprint(jira):
    magics = JiraMagics(None, jira)
    magics.mysprint('--all')
