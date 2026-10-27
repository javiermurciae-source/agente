"""Tests para conversor_temperatura.py"""

import pytest

from conversor_temperatura import c_to_f, f_to_c


@pytest.mark.parametrize(
    "celsius, fahrenheit",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
    ],
)
def test_c_to_f(celsius, fahrenheit):
    assert c_to_f(celsius) == pytest.approx(fahrenheit)


@pytest.mark.parametrize(
    "fahrenheit, celsius",
    [
        (32, 0),
        (212, 100),
        (-40, -40),
    ],
)
def test_f_to_c(fahrenheit, celsius):
    assert f_to_c(fahrenheit) == pytest.approx(celsius)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
