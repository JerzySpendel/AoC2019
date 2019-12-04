import pytest
import first


@pytest.fixture()
def wire_data():
    return 'R100,D200,L200,U100'


def test_parser(wire_data):
    pass