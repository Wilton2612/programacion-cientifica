


def validar_entradas(metodo, variable,ek, ena, el,gk,gna, vector_tiempo,ti,tf,valor_estimulacion ):
    re = False
    if (metodo is not None) and (variable is not None) and len(ek)!=0 and len(ena)!=0 and len(el)!=0 and len(gk)!=0 and len(gna)!=0 and len(vector_tiempo)!=0 and len(ti)!=0 and len(tf)!=0 and len(valor_estimulacion)!=0 :
        re = True
    return re


