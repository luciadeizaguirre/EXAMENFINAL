from heapq import heappush,heappop
class Ciudad:
    def __init__(self,nombre,distancia,costo):
        self.nombre=nombre
        self.distancia=distancia
        self.costo=costo

    def camino_corto(self,ciudad,ciudad_inicial):
        monticulo=[(0,ciudad_inicial)]
        distancia={ciudad:self.distancia}
        while monticulo:
            costo,ciudad=heappop(monticulo)
            if ciudad in distancia:
                continue
            distancia[ciudad]=costo
            for ciudad in set(ciudades) - set(distancia):
                heappush(monticulo, (costo+costo(distancia[-1], ciudad), distancia+[ciudad]))
            return
ciudades=[]
ciudades.append(Ciudad("Madrid",10,40))
ciudades.append(Ciudad("Barcelona",40,20))
ciudades.append(Ciudad("Viena",20,9))
ciudades.append(Ciudad("Zaragoza",30,15))
ciudad_inicial=Ciudad("Jaen",30,15)
ciudad=ciudades
    print(camino_corto(ciudad,ciudad_inicial))



        