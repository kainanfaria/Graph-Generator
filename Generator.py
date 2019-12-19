from random import randint
import os

class graph():

    def __init__(self, type, vertex, edges):
        self.type = type
        self.vertex = vertex
        self.edges = edges
        self.edgeArray = []

    def edge_generator(self):
        if self.type == "CONEXO":
            self.graph_conexo()

        elif self.type == "TRIANGULAR":
            self.graph_triangular()
        elif self.type == "RANDOM":
            self.graph_random()

    def graph_random(self):
        i = 1
        while i <= self.edges+1:
            if i <= self.vertex:
                k = randint(1, self.vertex)
                if (i, k) not in self.edgeArray and (k, i) not in self.edgeArray:
                    self.edgeArray.append((i, k))
                    i+=1
                else:
                    continue
            else:
                j = randint(1, self.vertex)
                k = randint(1, self.vertex)
                if (j, k) not in self.edgeArray and (k, j) not in self.edgeArray:
                    self.edgeArray.append((j, k))
                    i+=1
                else:
                    continue

    def graph_conexo(self):
        i = 1
        while i <= self.edges:
            j = randint(1, self.vertex)
            if i > self.vertex:
                j = randint(1, self.vertex)
                k = randint(1, self.vertex)
                if j != k:
                    if (k, j) not in self.edgeArray and (j, k) not in self.edgeArray:
                        self.edgeArray.append((int(k), int(j)))
                        i += 1
                    else:
                        continue
                else:
                    continue
            if j != i and i <= self.vertex:
                if (int(j), int(i)) not in self.edgeArray and (j, i) not in self.edgeArray:
                    self.edgeArray.append((int(i), int(j)))
                    i +=1
                else:
                    continue
            else:
                continue

    def graph_triangular(self):
        i = 1
        three = False
        if self.vertex == 3:
            self.edgeArray.append((int(1), int(2)))
            self.edgeArray.append((int(1), int(3)))
            self.edgeArray.append((int(2), int(3)))
            self.edges = 3
        else:
            while i <= self.vertex:
                if three == False:   
                    self.edgeArray.append((int(1), int(2)))
                    self.edgeArray.append((int(1), int(3)))
                    self.edgeArray.append((int(2), int(3)))
                    self.edges = 3
                    three = True
                    i += 3

                else:
                    a = randint(1, i-1)
                    vizinho_a = self.vizinho(a)
                    indice = randint(1, len(vizinho_a))               
                    if (a, i) not in self.edgeArray and (i, a) not in self.edgeArray:
                        self.edgeArray.append((i, a))
                        if (vizinho_a[indice-1], i) not in self.edgeArray and vizinho_a[indice-1] != i:
                            self.edgeArray.append((i, vizinho_a[indice-1]))
                            self.edges+=2
                            i+=1
                        else:
                            self.edgeArray.remove((i, a))
                            continue
                    else:
                        continue


    def vizinho(self, v):
        ret =[]
        for i in self.edgeArray:
            if i[0] == v:
                ret.append(i[1])
            if i[1] == v:
                ret.append(i[0])
        return ret


    def save_graph(self, name_graph):
        arq = open("/home/kainan/Documentos/Pesquisa/Python/Grafos/graph_"+name_graph+".txt", 'w')
        NP = "c "+name_graph
        VE = "p edge "+str(self.vertex)+" "+str(self.edges)
        texto = NP + "\n" + VE + "\n"
        arq.write(texto)
        for i in range(self.edges):
            arq.write("e " + str(self.edgeArray[i][0]) + " " + str(self.edgeArray[i][1]) + "\n")

        arq.close()
