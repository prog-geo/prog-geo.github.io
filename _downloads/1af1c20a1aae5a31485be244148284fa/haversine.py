"""Distância de Haversine.

A fórmula de Haversine possibilita o cálculo de distâncias entre
dois pontos em uma esfera a partir de suas latitudes e longitudes.

Este módulo contém uma função chamada ``DistanciaHaversine``
que implementa esse cálculo.
"""

import math


# Raio da Terra: 6371km
raio_terra = 6371


def DistanciaHaversine(lat1, long1, lat2, long2):
    """Computa a distância entre dois pontos na esfera.

    O cálculo de distância é baseado na fórmula de Haversine.

    Args:
        lat1 (float): latitude do primeiro pronto, em graus decimais.
        long1 (float): longitude do primeiro pronto, em graus decimais.
        lat2 (float): latitude do segundo pronto, em graus decimais.
        long3 (float): longitude do segundo pronto, em graus decimais.

    Returns:
        float:
    """
    # Covertendo de graus decimais para radianos
    ϕ1  = math.radians(lat1)
    ϕ2 = math.radians(lat2)

    λ1 = math.radians(long1)
    λ2 = math.radians(long2)

    # Pré-computando alguns valores da fórmula de Haversine
    Δϕ = ϕ2 - ϕ1
    Δλ = λ2 - λ1

    sin2_fi = math.sin(Δϕ / 2.0) ** 2

    sin2_lambda = math.sin(Δλ / 2.0) ** 2

    # Computando a distância de Haversine
    distancia = 2.0 * raio_terra \
                * math.asin(
                    math.sqrt(
                        sin2_fi + math.cos(ϕ1) \
                        * math.cos(ϕ2) * sin2_lambda
                    )
                  )

    # Retornando a distância computada
    return distancia

if __name__ == "__main__":
    import sys
    print(DistanciaHaversine(
            float(sys.argv[1]), float(sys.argv[2]),
            float(sys.argv[3]), float(sys.argv[4])
          )
    )
