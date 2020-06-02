# -*- coding: utf-8 -*-
"""
@author: Cynthia Roberti Lima
"""
import math

# Parâmetros para o elipsoide GRS80
a = 6378137
b = 6356752.314
f = 1/298.25722356
e2 = 0.00669438
e = 0.081819191
a_b = 21384.702

A = 1.005052502
B = 0.005063109
C = 1.0627590E-05
D = 2.08204E-08
E = 3.93237E-11
F = 7.10845E-14

A_lin = 1.00336409
B_lin = 0.000113059
C_lin = 1.69946E-06

def deg2rad(val):
    return (val*math.pi)/180

def calc_N(lat):
    N = a/math.sqrt((1-((e2)*math.pow(math.sin(lat),2))))
    return N

def raio_esfera(M,N):
    aux = M*N
    return math.sqrt(aux)

def calc_M(lat):
    p1 = (a*(1-e2))
    p2 = math.pow((1-(e2*(math.pow(math.sin(lat),2)))),(3/2))
    M = p1/p2
    return M

def comprimento_paralelo(lat,long1,long2):
    N = calc_N(lat)
    S = N * math.cos(lat) * (long2-long1)
    return S

def comprimento_meridiano(lat1,lat2):
    p1 = a*(1-e2)*(lat2-lat1)*A;
    p2 = ((math.sin(2*lat2))-math.sin(2*lat1))*(1/2)*B
    p3 = ((math.sin(4*lat2))-math.sin(4*lat1))*(1/4)*C
    p4 = ((math.sin(6*lat2))-math.sin(6*lat1))*(1/6)*D
    p5 = ((math.sin(8*lat2))-math.sin(8*lat1))*(1/8)*E
    p6 = ((math.sin(10*lat2))-math.sin(10*lat1))*(1/10)*F

    Spq = p1 - p2 + p3 - p4 + p5 - p6
    return Spq

def delta_lambda(lon1,lon2):
    return lon2-lon1

def delta_phi(lat1,lat2):
    return (lat2-lat1)/2

def phi_medio(lat1,lat2):
    return (lat2+lat1)/2

def area_quadrilatero(lat1,lat2,lon1,lon2):
    dlambda = delta_lambda(lon1,lon2)
    dphi = delta_phi(lat1,lat2)
    phiMedio = phi_medio(lat1,lat2)
    p1 = 2 * (b * b)
    p2 = A_lin * math.sin(dphi) * math.cos(phiMedio)
    p3 = B_lin * math.sin(3*dphi) * math.cos(3*phiMedio)
    p4 = C_lin * math.sin(5*dphi) * math.cos(5*phiMedio)
    result = p1 * (p2 - p3 + p4) * dlambda
    return result

def raio_curvatura(azimute,M,N):
    p1 = math.pow(math.cos(azimute),2)/M
    p2 = math.pow(math.sin(azimute),2)/N
    return 1/(p1+p2)

def latitude_geocentrica(lat):
    p1 = 1-e2
    p2 = math.tan(lat)
    p3 = p1*p2
    p4 = math.atan(p3)
    p5 = (p4*180)/math.pi
    return p5

def latitude_reduzida(lat):
    p1 = math.pow((1-e2),(1/2))
    p2 = math.tan(lat)
    p3 = math.atan(p1*p2)
    return (p3*180)/math.pi
    