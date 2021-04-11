def NDVI(nir, red):
    num = nir - red
    den = nir + red

    return num / den