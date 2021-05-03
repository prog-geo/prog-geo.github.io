L = 1
C1 = 6
C2 = 7.5
G = 2.5

def EVI(nir, red, blue):
    num = G * (nir - red)
    den = nir + (C1 * red) - (C2 * blue) + L

    return num / den