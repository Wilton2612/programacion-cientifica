##
import numpy as np
from scipy import optimize as opt
import matplotlib.pyplot as plt
#parametros iniciales

def an_V(V):
   return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))

def bn_V(V):
    return 0.125 * np.exp(-(V + 65.0) / 80.0)
def am_V(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))

def bm_V(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)
def ah_V(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)
def bh_V(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))
##
h = 0.01 ## Delta t
ti = 0.0
tf = 500.00
I_dn = 0.4
I_dm = 0.05
I_dh = 0.5

t = np.arange(ti,tf+h,h)

gl = 0.3
ek = -77.0
ena = 50.0
el = -54.0
v0= -65.0

#Sistema de ecuaciones diferenciales

def dn_dt(v,n,m,h):
    return an_V(v)*(1-n) - bn_V(v)*n  #[1]

def dm_dt(v,n,m,h):
    return am_V(v)*(1-m) - bm_V(v) *m  #[2]
def dh_dt(v,n,m,h):
    return ah_V(v)*(1-h) - bh_V(v)*h  #[3]

def dv_dt(Vm,n,m,h,I):
    gk = 36.0 * (n ** 4.0)
    gna = 120.0 * (m ** 3.0) * h
    return -1*((gk*(Vm-ek))+
               (gna*(Vm-ena))+
               (gl*(Vm-el))
               +I)  #denominador cm
        # [0]

I_v = np.zeros(len(t))
for i in range(len(t)):
    if 200 < t[i] < 300:
        I_v[i] = 14
#Euler back:

def FunBack (yt2, y1t1, y2t1, y3t1, y4t1,I_v,h):
    return [y1t1 + h * dv_dt(yt2[0],yt2[1],yt2[2],yt2[3],I_v) - yt2[0],
            y2t1 + h *dn_dt(yt2[0],yt2[1],yt2[2],yt2[3]) - yt2[1],
            y3t1 + h *dm_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[2],
            y4t1 + h * dh_dt(yt2[0],yt2[1],yt2[2],yt2[3]) - yt2[3]]
def FEulerModRoot(yt2,y1t1,y2t1,y3t1,y4t1,I_v,h):
    return [y1t1 + (h/2.0) * dv_dt(y1t1,y2t1,y3t1,y4t1,I_v) + dv_dt(yt2[0], yt2[1], yt2[2], yt2[3],I_v) - yt2[0],
            y2t1 + (h/2.0) * dn_dt(y1t1,y2t1,y3t1,y4t1) + dn_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[1],
            y3t1 + (h/2.0) * dm_dt(y1t1,y2t1,y3t1,y4t1) + dm_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[2],
            y4t1 + (h/2.0) * dh_dt(y1t1,y2t1,y3t1,y4t1) + dh_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[3]
            ]


#Valores iniciales

#vectores para cada una de las ecuaciones
#para las ecuaciones de dn
dnEuBack = np.zeros(len(t))
dnEuMod = np.zeros(len(t))
dnEuFor = np.zeros(len(t))
dnRK2 = np.zeros(len(t))
dnRK4 = np.zeros(len(t))

#para las ecuaciones dm
dmEuBack = np.zeros(len(t))
dmEuMod = np.zeros(len(t))
dmEuFor = np.zeros(len(t))
dmRK2 = np.zeros(len(t))
dmRK4 = np.zeros(len(t))

#para las ecuaciones dh
dhEuBack = np.zeros(len(t))
dhEuMod = np.zeros(len(t))
dhEuFor = np.zeros(len(t))
dhRK2 = np.zeros(len(t))
dhRK4 = np.zeros(len(t))

#para voltaje
dvEuBack = np.zeros(len(t))
dvEuMod = np.zeros(len(t))
dvEuFor = np.zeros(len(t))
dvRK2 = np.zeros(len(t))
dvRK4 = np.zeros(len(t))


#primeras posiciones
#dn
dnEuBack [0] = I_dn
dnEuMod [0] = I_dn
dnEuFor [0] = I_dn

#dm
dmEuBack [0] = I_dm
dmEuMod [0] = I_dm
dmEuFor [0] = I_dm

#dh
dhEuBack [0] = I_dh
dhEuMod [0] = I_dh
dhEuFor [0] = I_dh

#dv
dvEuBack [0] = -65.00
dvEuMod [0] = -65.00
dvEuFor [0] = -65.00

##
#iteraciones
for time in range (1,len(t)):
    #Euler Forward
    dvEuFor[time] = dvEuFor[time -1] + h * dv_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1],I_v[time])
    dnEuFor[time] = dnEuFor[time -1] + h * dn_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])
    dmEuFor[time] = dmEuFor[time -1] + h * dm_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])
    dhEuFor[time] = dhEuFor[time -1] + h * dh_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])

    #RK2
    kv1 = dv_dt(dvRK2[time-1],dnRK2[time-1],dmRK2[time -1], dhRK2[time-1],I_v[time] )
    kn1 = dn_dt(dvRK2[time-1],dnRK2[time-1],dmRK2[time -1], dhRK2[time-1])
    km1 = dm_dt(dvRK2[time-1],dnRK2[time-1],dmRK2[time -1], dhRK2[time-1])
    kh1 = dh_dt(dvRK2[time-1],dnRK2[time-1],dmRK2[time -1], dhRK2[time-1])
    kv2 = dv_dt(dvRK2[time-1] + kv1 * h, dnRK2[time-1] +kn1 *h, dmRK2[time-1] + km1 *h, dhRK2[time-1] + kh1 *h,I_v[time])
    kn2 = dn_dt(dvRK2[time-1] + kv1 * h, dnRK2[time-1] +kn1 *h, dmRK2[time-1] + km1 *h, dhRK2[time-1] + kh1 *h)
    km2 = dm_dt(dvRK2[time-1] + kv1 * h, dnRK2[time-1] +kn1 *h, dmRK2[time-1] + km1 *h, dhRK2[time-1] + kh1 *h)
    kh2 = dh_dt(dvRK2[time-1] + kv1 * h, dnRK2[time-1] +kn1 *h, dmRK2[time-1] + km1 *h, dhRK2[time-1] + kh1 *h)

    dvRK2[time] = dvRK2[time-1] + (h/2.0)*(kv1+kv2)
    dnRK2[time] = dnRK2[time-1] + (h/2.0)*(kn1+kn2)
    dmRK2[time] = dmRK2[time-1] + (h/2.0)*(km1+km2)
    dhRK2[time]=  dhRK2[time-1] + (h/2.0)*(kh1+kh2)

    #RK4

    kv1 = dv_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1],I_v[time])
    kn1 = dn_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
    km1 = dm_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
    kh1 = dh_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])

    kv2= dv_dt(dvRK4[time -1] + (0.5 * kv1*h), dnRK4[time-1] + (0.5 + kn1*h), dmRK4[time -1] + (0.5*km1*h),
                dhRK4[time-1] + (0.5*kh1*h),I_v[time])
    kn2 = dn_dt(dvRK4[time -1] + (0.5 * kv1*h), dnRK4[time-1] + (0.5 + kn1*h), dmRK4[time -1] + (0.5*km1*h),
                dhRK4[time-1] + (0.5*kh1*h))
    km2 = dm_dt(dvRK4[time -1] + (0.5 * kv1*h), dnRK4[time-1] + (0.5 + kn1*h), dmRK4[time -1] + (0.5*km1*h),
                dhRK4[time-1] + (0.5*kh1*h))
    kh2 = dh_dt(dvRK4[time -1] + (0.5 * kv1*h), dnRK4[time-1] + (0.5 + kn1*h), dmRK4[time -1] + (0.5*km1*h),
                dhRK4[time-1] + (0.5*kh1*h))

    kv3 = dv_dt(dvRK4[time -1] + (0.5 * kv2*h), dnRK4[time-1] + (0.5 + kn2*h), dmRK4[time -1] + (0.5*km2*h),
                dhRK4[time-1] + (0.5*kh2*h),I_v[time])
    kn3 = dn_dt(dvRK4[time -1] + (0.5 * kv2*h), dnRK4[time-1] + (0.5 + kn2*h), dmRK4[time -1] + (0.5*km2*h),
                dhRK4[time-1] + (0.5*kh2*h))
    km3 = dm_dt(dvRK4[time -1] + (0.5 * kv2*h), dnRK4[time-1] + (0.5 + kn2*h), dmRK4[time -1] + (0.5*km2*h),
                dhRK4[time-1] + (0.5*kh2*h))
    kh3 = dh_dt(dvRK4[time -1] + (0.5 * kv2*h), dnRK4[time-1] + (0.5 + kn2*h), dmRK4[time -1] + (0.5*km2*h),
                dhRK4[time-1] + (0.5*kh2*h))

    kv4= dv_dt(dvRK4[time -1] + (kv3*h), dnRK4[time-1] + (kn3*h), dmRK4[time -1] + (km3*h),
                dhRK4[time-1] + (kh3*h),I_v[time])
    kn4 = dn_dt(dvRK4[time -1] + (kv3*h), dnRK4[time-1] + (kn3*h), dmRK4[time -1] + (km3*h),
                dhRK4[time-1] + (kh3*h))
    km4 = dm_dt( dvRK4[time -1] + (kv3*h), dnRK4[time-1] + (kn3*h), dmRK4[time -1] + (km3*h),
                dhRK4[time-1] + (kh3*h))
    kh4 = dh_dt(dvRK4[time -1] + (kv3*h), dnRK4[time-1] + (kn3*h), dmRK4[time -1] + (km3*h),
                dhRK4[time-1] + (kh3*h))

    dvRK4[time] = dvRK4[time-1] + (h/6.0)*(kv1 +2*kv2 +2*kv3 +kv4)
    dnRK4[time] = dnRK4[time-1] + (h/6.0)*(kn1 +2*kn2 +2*kn3 +kn4)
    dmRK4[time] = dmRK4[time-1] + (h/6.0)*(km1 +2*km2 +2*km3 +km4)
    dhRK4[time] = dhRK4[time-1] + (h/6.0)*(kh1 +2*kh2 +2*kh3 +kh4)

    #Euler hacia atrás
    solBack = opt.fsolve(FunBack,
                         np.array([dvEuBack[time-1],
                                  dnEuBack[time-1],
                                  dmEuBack[time-1],
                                  dhEuBack[time-1]]),
                         (dvEuBack[time - 1],
                         dnEuBack[time - 1],
                         dmEuBack[time - 1],
                         dhEuBack[time - 1],I_v[time], h),
                         xtol=10 ** -15)
    dvEuBack[time] = solBack[0]
    dnEuBack[time] = solBack[1]
    dmEuBack[time] = solBack[2]
    dhEuBack[time] = solBack[3]

    #Euler modificado
    solMod = opt.fsolve(FEulerModRoot,
                         np.array([dvEuBack[time - 1],
                                  dnEuBack[time - 1],
                                  dmEuBack[time - 1],
                                  dhEuBack[time - 1]]),
                         (dvEuBack[time - 1],
                          dnEuBack[time - 1],
                          dmEuBack[time - 1],
                          dhEuBack[time - 1],I_v[time],h),
                         xtol=10 ** -15)
    dvEuMod[time] = solMod[0]
    dnEuMod[time] = solMod[1]
    dmEuMod[time] = solMod[2]
    dhEuMod[time] = solMod[3]


##
import matplotlib.pyplot as plt
#plt.figure()
#plt.plot(dvEuFor)
plt.plot(dvEuMod)
#plt.plot(dvRK2)
#plt.show()