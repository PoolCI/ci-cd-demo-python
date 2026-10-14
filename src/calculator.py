"""Módulo de calculadora básica con operaciones aritméticas."""


def add(a: float, b: float) -> float:
    """Suma dos números."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Resta dos números."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplica dos números."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide dos números. Lanza ValueError si b == 0."""
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b
