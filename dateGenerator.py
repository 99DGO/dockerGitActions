
#Fechas iniciales y finales de la lista para los pivotes en formato YYYY-MM
FECHA_INICIAL="2023-10" 
FECHA_FINAL="2025-11"
#Dias de cobro del mes
DIAS_DE_COBRO=["15","28"]


def crearLista(start=FECHA_INICIAL, final=FECHA_FINAL, dias=DIAS_DE_COBRO):
    anioInicial=int(start[:4])
    anioFinal=int(final[:4])
    
    mesInicial=int(start[5:])
    mesFinal=int(final[5:])
    
    ans=""
    
    iY=anioInicial
    iM=mesInicial
    while iY<=anioFinal:
        
        while (iM<=12 and iY!=anioFinal) or (iY==anioFinal and iM<=mesFinal):
            for dia in dias:
                ans+="'"+str(iY)+"-"+f"{iM:02}"+"-"+f"{dia:02}"+"'"+", "
            iM+=1
            
        iM=1 
        iY+=1
        
    return ans[:-2]


print(crearLista())