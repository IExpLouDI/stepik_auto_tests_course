from pickle import FALSE

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
	assert True

@pytest.mark.xfail
def test_no_suceed():
	assert False

@pytest.mark.skip
def test_skipped():
	assert False
