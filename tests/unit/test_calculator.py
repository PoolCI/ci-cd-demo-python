"""Pruebas unitarias para src/calculator.py."""
import pytest

from src.calculator import add, subtract, multiply, divide


class TestAdd:
    def test_add_positivos(self):
        assert add(2, 3) == 5

    def test_add_negativos(self):
        assert add(-1, -1) == -2

    def test_add_cero(self):
        assert add(0, 5) == 5

    def test_add_decimales(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)


class TestSubtract:
    def test_subtract_basico(self):
        assert subtract(10, 4) == 6

    def test_subtract_negativo(self):
        assert subtract(3, 7) == -4


class TestMultiply:
    def test_multiply_basico(self):
        assert multiply(3, 4) == 12

    def test_multiply_por_cero(self):
        assert multiply(5, 0) == 0


class TestDivide:
    def test_divide_basico(self):
        assert divide(10, 2) == 5

    def test_divide_por_cero_lanza_error(self):
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            divide(10, 0)

    def test_divide_decimal(self):
        assert divide(1, 3) == pytest.approx(0.3333, rel=1e-3)
