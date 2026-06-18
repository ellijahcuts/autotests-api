"""
import pytest


@pytest.mark.smoke
def test_smoke_case():
    assert 1+1==2

@pytest.mark.regress
def test_regression_case():
    assert 2+2==4

@pytest.mark.fast
def test_fast():
    assert 2+2==4

@pytest.mark.slow
def test_slow():
    assert 2 + 2 == 4

@pytest.mark.smoke
class TestSuite:
    def test_case(self):
        ...
    def test_case1(self):
        ...

@pytest.mark.regress
class TestAuthUser:
    @pytest.mark.smoke
    def test_login(self):
        ...

    @pytest.mark.slow
    def test_pass_reset(self):
        ...

    @pytest.mark.fast
    def test_logout(self):
        ...


@pytest.mark.crit
def test_crit():
    ...


@pytest.mark.registration
def test_user_registration():
    pass

@pytest.mark.smok1
def test_user_login():
    pass

@pytest.mark.registration
@pytest.mark.regression
def test_password_reset():
    pass

"""