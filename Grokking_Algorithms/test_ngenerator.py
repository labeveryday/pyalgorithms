import ngenerator
import pytest


@pytest.fixture(scope=any_non_session_scope,  autouse=True)
def faker_seed():
    return 12345

def test_get_names(faker):
    assert ngenerator.get_names(1) == [faker]
