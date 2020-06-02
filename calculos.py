# -*- coding: utf-8 -*-
"""
@author: Cynthia Roberti Lima
"""
import functions as fc
import math

# Coordenadas dos vertices do retangulo envolvente 
#  Campo Grande - MS
lat1 = -20.60387
lat2 = -20.37103
lon1 = -54.50932
lon2 = -54.76407

lats = [lat1,lat2]
longs = [lon1,lon2]

#radianos
lats_rad = list(map(fc.deg2rad,lats))
longs_rad = list(map(fc.deg2rad,longs))

#Comprimento dos lados do quadrilátero
#paralelos
N = fc.calc_N(lats_rad[0])
paralelo1 = fc.comprimento_paralelo(lats_rad[0],longs_rad[0],longs_rad[1])
paralelo2 = fc.comprimento_paralelo(lats_rad[1],longs_rad[0],longs_rad[1])
#meridianos
meridiano = fc.comprimento_meridiano(lats_rad[0],lats_rad[1])

# Area do quadrilatero
dlambda = fc.delta_lambda(longs_rad[0],longs_rad[1])
dphi = fc.delta_phi(lats_rad[0],lats_rad[1])
phiMedio = fc.phi_medio(lats_rad[0],lats_rad[1])
areaQuadrilatero = fc.area_quadrilatero(lats_rad[0],lats_rad[1],longs_rad[0],longs_rad[1])

# Coordenadas ponto central
latMedio = fc.phi_medio(lat1,lat2)
lonMedio = fc.phi_medio(lon1,lon2)
lats_rad.append(fc.deg2rad(latMedio)) #radianos
lats_rad.append(fc.deg2rad(lonMedio))

# Raio da esfera que melhor se ajusta a regiao
M = fc.calc_M(lats_rad[2])
N = fc.calc_N(lats_rad[2])
raioEsfera = fc.raio_esfera(M,N)

# Raio do paralelo que contem o ponto indicado
raioParalelo = N * math.cos(lats_rad[2])

# Raio de curvatura com azimute de 30 graus
az = fc.deg2rad(30)
raioCurvatura = fc.raio_curvatura(az,M,N)

# Latitude Geocentrica
latitudeGeocentrica = fc.latitude_geocentrica(lats_rad[2])

# Latitude Reduzida
latitudeReduzida = fc.latitude_reduzida(lats_rad[2])





