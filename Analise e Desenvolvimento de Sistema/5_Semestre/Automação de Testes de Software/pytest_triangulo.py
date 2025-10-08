def triangulo(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise TypeError("Os lados do triângulo devem ser números.")
    if a <= 0 or b <= 0 or c <= 0:
        return "Inválido"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Inválido"
    if a == b == c:
        return "Equilátero"
    if a == b or b == c or a == c:
        return "Isósceles"
    return "Escaleno"
