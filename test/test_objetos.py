import pytest
import src.objetos


def test_perimetro():
    assert src.objetos.perimetro([1.0, 2.0, 3.0]) ==pytest.approx(6.0), " 6!=7" # This messeage is in case that we've a error

