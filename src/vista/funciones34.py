##
import matplotlib.pyplot as plt
import numpy as np

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



def dn_dt(v,n,m,h):
    return an_V(v)*(1-n) - bn_V(v)*n  #[1]

def dm_dt(v,n,m,h):
    return am_V(v)*(1-m) - bm_V(v) *m  #[2]
    
def dh_dt(v,n,m,h):
    return ah_V(v)*(1-h) - bh_V(v)*h  #[3]

#v(t)
def dv_dt(Vm,n,m,h,I, ek,ena, el,gk, gna, gl ):
    gk = gk * (n ** 4.0)
    gna = gna * (m ** 3.0) * h
    return -1*((gk*(Vm-ek))+
               (gna*(Vm-ena))+
               (gl*(Vm-el))
               +I)  #denominador cm
        # [0]


def corriente(t):
    I_v = np.zeros(len(t))
    for i in range(len(t)):
        if 200 < t[i] < 300:
            I_v[i] = 14
    return I_v

"""
gl = 0.3 #no ingresa por interfaz
ek = -77.0 #lista
ena = 50.0 #lista
el = -54.0 #lista
v0= -65.0 #
"""

def euler_hacia_adelante(h,ti,tf,ek,ena, el,gk,gna, variable, gl=0.3):
    I_dn = 0.4
    I_dm = 0.05
    I_dh = 0.5
    t = np.arange(ti,tf+h,h)
    I_v= corriente(t)
    dnEuFor = np.zeros(len(t))
    dmEuFor = np.zeros(len(t))
    dhEuFor = np.zeros(len(t))
    dvEuFor = np.zeros(len(t))

    dnEuFor [0] = I_dn
    dmEuFor [0] = I_dm
    dhEuFor [0] = I_dh
    dvEuFor [0] = -65.00

    for time in range (1,len(t)):
        #Euler Forward
        dvEuFor[time] = dvEuFor[time -1] + h * dv_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1],I_v[time],ek, ena,el, gk,gna, gl) 
        dnEuFor[time] = dnEuFor[time -1] + h * dn_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])
        dmEuFor[time] = dmEuFor[time -1] + h * dm_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])
        dhEuFor[time] = dhEuFor[time -1] + h * dh_dt(dvEuFor[time-1],dnEuFor[time-1],dmEuFor[time-1],dhEuFor[time-1])

    if variable==1:
        return dvEuFor, t
    elif variable==2:
        return dmEuFor, t
    return dnEuFor, t


plt.figure()
#Gráfica Euler for
euler_adelante = euler_hacia_adelante(0.01, 0.0, 500.00, -77.00, 50.0, -54.0, 36.0, 120.0,2)
plt.plot(euler_adelante[1], euler_adelante[0], "r")
plt.suptitle("Euler Forward")
plt.show()
##
def FunBack (yt2, y1t1, y2t1, y3t1, y4t1,I_v,h):
    return [y1t1 + h * dv_dt(yt2[0],yt2[1],yt2[2],yt2[3],I_v) - yt2[0],
            y2t1 + h *dn_dt(yt2[0],yt2[1],yt2[2],yt2[3]) - yt2[1],
            y3t1 + h *dm_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[2],
            y4t1 + h * dh_dt(yt2[0],yt2[1],yt2[2],yt2[3]) - yt2[3]]

def euler_atras (h,ti,tf,ek,ena, el,gk,gna, variable, gl=0.3):
    I_dn = 0.4
    I_dm = 0.05
    I_dh = 0.5
    t = np.arange(ti, tf + h, h)
    I_v = corriente(t)
    dnEuBack = np.zeros(len(t))
    dmEuBack = np.zeros(len(t))
    dhEuBack = np.zeros(len(t))
    dvEuback = np.zeros(len(t))

    dnEuBack[0] = I_dn
    dmEuBack[0] = I_dm
    dhEuBack[0] = I_dh
    dvEuBack[0] = -65.00

    for time in range (1,len(t)):
        solBack = opt.fsolve(FunBack,
                             np.array([dvEuBack[time - 1],
                                       dnEuBack[time - 1],
                                       dmEuBack[time - 1],
                                       dhEuBack[time - 1]]),
                             (dvEuBack[time - 1],
                              dnEuBack[time - 1],
                              dmEuBack[time - 1],
                              dhEuBack[time - 1], I_v[time], h),
                             xtol=10 ** -15)
        dvEuBack[time] = solBack[0]
        dnEuBack[time] = solBack[1]
        dmEuBack[time] = solBack[2]
        dhEuBack[time] = solBack[3]

    if variable == 1:
        return dvEuBack, t
    elif variable == 2:
        return dmEuBack, t
    return dnEuBack, t


plt.figure()
#Gráfica Euler Back
euler_atras = euler_atras(0.01, 0.0, 500.00, -77.00, 50.0, -54.0, 36.0, 120.0,2)
plt.plot(euler_atras[1], euler_atras[0], "r")
plt.suptitle("Euler Backwards")
plt.show()
##
def RK2(h,ti,tf,ek,ena, el,gk,gna, variable, gl=0.3):
    I_dn = 0.4
    I_dm = 0.05
    I_dh = 0.5
    t = np.arange(ti, tf + h, h)
    I_v = corriente(t)
    dnRK2 = np.zeros(len(t))
    dmRK2 = np.zeros(len(t))
    dhRK2 = np.zeros(len(t))
    dvRK2 = np.zeros(len(t))

    dnRK2[0] = I_dn
    dmRK2[0] = I_dm
    dhRK2[0] = I_dh
    dvRK2[0] = -65.00

    for time in range(1, len(t)):
        kv1 = dv_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1], I_v[time])
        kn1 = dn_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
        km1 = dm_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
        kh1 = dh_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
        kv2 = dv_dt(dvRK2[time - 1] + kv1 * h, dnRK2[time - 1] + kn1 * h, dmRK2[time - 1] + km1 * h,
                    dhRK2[time - 1] + kh1 * h, I_v[time])
        kn2 = dn_dt(dvRK2[time - 1] + kv1 * h, dnRK2[time - 1] + kn1 * h, dmRK2[time - 1] + km1 * h,
                    dhRK2[time - 1] + kh1 * h)
        km2 = dm_dt(dvRK2[time - 1] + kv1 * h, dnRK2[time - 1] + kn1 * h, dmRK2[time - 1] + km1 * h,
                    dhRK2[time - 1] + kh1 * h)
        kh2 = dh_dt(dvRK2[time - 1] + kv1 * h, dnRK2[time - 1] + kn1 * h, dmRK2[time - 1] + km1 * h,
                    dhRK2[time - 1] + kh1 * h)

        dvRK2[time] = dvRK2[time - 1] + (h / 2.0) * (kv1 + kv2)
        dnRK2[time] = dnRK2[time - 1] + (h / 2.0) * (kn1 + kn2)
        dmRK2[time] = dmRK2[time - 1] + (h / 2.0) * (km1 + km2)
        dhRK2[time] = dhRK2[time - 1] + (h / 2.0) * (kh1 + kh2)

    if variable==1:
        return dvRK2, t
    elif variable==2:
        return dmRK2, t
    return dnRK2, t

plt.figure()
#Gráfica RK2
euler_atras = RK2(0.01, 0.0, 500.00, -77.00, 50.0, -54.0, 36.0, 120.0,2)
plt.plot(RK2[1], RK2[0], "r")
plt.suptitle("RK2")
plt.show()
##
def RK4(h,ti,tf,ek,ena, el,gk,gna, variable, gl=0.3):
    I_dn = 0.4
    I_dm = 0.05
    I_dh = 0.5
    t = np.arange(ti, tf + h, h)
    I_v = corriente(t)
    dnRK4 = np.zeros(len(t))
    dmRK4 = np.zeros(len(t))
    dhRK4 = np.zeros(len(t))
    dvRK4 = np.zeros(len(t))

    dnRK4[0] = I_dn
    dmRK4[0] = I_dm
    dhRK4[0] = I_dh
    dvRK4[0] = -65.00

    for time in range(1, len(t)):
        kv1 = dv_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1], I_v[time])
        kn1 = dn_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
        km1 = dm_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])
        kh1 = dh_dt(dvRK2[time - 1], dnRK2[time - 1], dmRK2[time - 1], dhRK2[time - 1])

        kv2 = dv_dt(dvRK4[time - 1] + (0.5 * kv1 * h), dnRK4[time - 1] + (0.5 + kn1 * h),
                    dmRK4[time - 1] + (0.5 * km1 * h),
                    dhRK4[time - 1] + (0.5 * kh1 * h), I_v[time])
        kn2 = dn_dt(dvRK4[time - 1] + (0.5 * kv1 * h), dnRK4[time - 1] + (0.5 + kn1 * h),
                    dmRK4[time - 1] + (0.5 * km1 * h),
                    dhRK4[time - 1] + (0.5 * kh1 * h))
        km2 = dm_dt(dvRK4[time - 1] + (0.5 * kv1 * h), dnRK4[time - 1] + (0.5 + kn1 * h),
                    dmRK4[time - 1] + (0.5 * km1 * h),
                    dhRK4[time - 1] + (0.5 * kh1 * h))
        kh2 = dh_dt(dvRK4[time - 1] + (0.5 * kv1 * h), dnRK4[time - 1] + (0.5 + kn1 * h),
                    dmRK4[time - 1] + (0.5 * km1 * h),
                    dhRK4[time - 1] + (0.5 * kh1 * h))

        kv3 = dv_dt(dvRK4[time - 1] + (0.5 * kv2 * h), dnRK4[time - 1] + (0.5 + kn2 * h),
                    dmRK4[time - 1] + (0.5 * km2 * h),
                    dhRK4[time - 1] + (0.5 * kh2 * h), I_v[time])
        kn3 = dn_dt(dvRK4[time - 1] + (0.5 * kv2 * h), dnRK4[time - 1] + (0.5 + kn2 * h),
                    dmRK4[time - 1] + (0.5 * km2 * h),
                    dhRK4[time - 1] + (0.5 * kh2 * h))
        km3 = dm_dt(dvRK4[time - 1] + (0.5 * kv2 * h), dnRK4[time - 1] + (0.5 + kn2 * h),
                    dmRK4[time - 1] + (0.5 * km2 * h),
                    dhRK4[time - 1] + (0.5 * kh2 * h))
        kh3 = dh_dt(dvRK4[time - 1] + (0.5 * kv2 * h), dnRK4[time - 1] + (0.5 + kn2 * h),
                    dmRK4[time - 1] + (0.5 * km2 * h),
                    dhRK4[time - 1] + (0.5 * kh2 * h))

        kv4 = dv_dt(dvRK4[time - 1] + (kv3 * h), dnRK4[time - 1] + (kn3 * h), dmRK4[time - 1] + (km3 * h),
                    dhRK4[time - 1] + (kh3 * h), I_v[time])
        kn4 = dn_dt(dvRK4[time - 1] + (kv3 * h), dnRK4[time - 1] + (kn3 * h), dmRK4[time - 1] + (km3 * h),
                    dhRK4[time - 1] + (kh3 * h))
        km4 = dm_dt(dvRK4[time - 1] + (kv3 * h), dnRK4[time - 1] + (kn3 * h), dmRK4[time - 1] + (km3 * h),
                    dhRK4[time - 1] + (kh3 * h))
        kh4 = dh_dt(dvRK4[time - 1] + (kv3 * h), dnRK4[time - 1] + (kn3 * h), dmRK4[time - 1] + (km3 * h),
                    dhRK4[time - 1] + (kh3 * h))

        dvRK4[time] = dvRK4[time - 1] + (h / 6.0) * (kv1 + 2 * kv2 + 2 * kv3 + kv4)
        dnRK4[time] = dnRK4[time - 1] + (h / 6.0) * (kn1 + 2 * kn2 + 2 * kn3 + kn4)
        dmRK4[time] = dmRK4[time - 1] + (h / 6.0) * (km1 + 2 * km2 + 2 * km3 + km4)
        dhRK4[time] = dhRK4[time - 1] + (h / 6.0) * (kh1 + 2 * kh2 + 2 * kh3 + kh4)

    if variable==1:
        return dvRK4, t
    elif variable==2:
        return dmRK4, t
    return dnRK4, t

plt.figure()
#Gráfica RK2
euler_atras = RK4(0.01, 0.0, 500.00, -77.00, 50.0, -54.0, 36.0, 120.0,2)
plt.plot(RK4[1], RK4[0], "r")
plt.suptitle("RK4")
plt.show()
##
def FEulerModRoot(yt2,y1t1,y2t1,y3t1,y4t1,I_v,h):
    return [y1t1 + (h/2.0) * dv_dt(y1t1,y2t1,y3t1,y4t1,I_v) + dv_dt(yt2[0], yt2[1], yt2[2], yt2[3],I_v) - yt2[0],
            y2t1 + (h/2.0) * dn_dt(y1t1,y2t1,y3t1,y4t1) + dn_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[1],
            y3t1 + (h/2.0) * dm_dt(y1t1,y2t1,y3t1,y4t1) + dm_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[2],
            y4t1 + (h/2.0) * dh_dt(y1t1,y2t1,y3t1,y4t1) + dh_dt(yt2[0], yt2[1], yt2[2], yt2[3]) - yt2[3]
            ]
def Euler_Mod(h,ti,tf,ek,ena, el,gk,gna, variable, gl=0.3):
    I_dn = 0.4
    I_dm = 0.05
    I_dh = 0.5
    t = np.arange(ti, tf + h, h)
    I_v = corriente(t)
    dnEuMod = np.zeros(len(t))
    dmEuMod = np.zeros(len(t))
    dhEuMod = np.zeros(len(t))
    dvEuMod = np.zeros(len(t))

    for time in range (1, len(t)):
        solMod = opt.fsolve(FEulerModRoot,
                            np.array([dvEuBack[time - 1],
                                      dnEuBack[time - 1],
                                      dmEuBack[time - 1],
                                      dhEuBack[time - 1]]),
                            (dvEuBack[time - 1],
                             dnEuBack[time - 1],
                             dmEuBack[time - 1],
                             dhEuBack[time - 1], I_v[time], h),
                            xtol=10 ** -15)
        dvEuMod[time] = solMod[0]
        dnEuMod[time] = solMod[1]
        dmEuMod[time] = solMod[2]
        dhEuMod[time] = solMod[3]

    dnEuMod[0] = I_dn
    dmEuMod[0] = I_dm
    dhEuMod[0] = I_dh
    dvEuMod[0] = -65.00

    if variable==1:
        return dvEuMod, t
    elif variable==2:
        return dmEuMod, t
    return dnEuMod, t

plt.figure()
#Gráfica Euler Back
euler_atras = euler_atras(0.01, 0.0, 500.00, -77.00, 50.0, -54.0, 36.0, 120.0,2)
plt.plot(euler_Mod[1], euler_Mod[0], "r")
plt.suptitle("Euler Modificado")
plt.show()
