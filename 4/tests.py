import pytest
import first


@pytest.mark.parametrize("number", [111111, 112345])
def test_meets_criteria(number):
    assert first.meets_criteria(number)


@pytest.mark.parametrize('number', [110000])
def test_doesnt_meet_criteria(number):
    assert not first.meets_criteria(number)
