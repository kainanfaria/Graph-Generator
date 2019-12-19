from flask import Flask, render_template, request
from random import randint
import os
import graphviz

class graph():

    def __init__(self, typeG, vertex, edges):
        self.typeG = typeG
        self.vertex = vertex
        self.edges = edges
        self.edgeArray = []

    def edge_generator(self):
        if self.typeG == "CONNECTED":
            self.graph_conexo()

        elif self.typeG == "TRIANGULAR":
            self.graph_triangular()

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
                if (int(j), int(i)) not in self.edgeArray:
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
                    if (a, i) not in self.edgeArray:
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
        arq = open("/home/kainan/PycharmProjects/Estagio/flask/static/graph_"+name_graph+".txt", 'w')
        NP = "c "+name_graph
        VE = "p edge "+str(self.vertex)+" "+str(self.edges)
        texto = NP + "\n" + VE + "\n"
        arq.write(texto)
        for i in range(self.edges):
            arq.write("e " + str(self.edgeArray[i][0]) + " " + str(self.edgeArray[i][1]) + "\n")
        
        arq.close()
	
    
class Generator():

	def __init__(self, graph_name):
		self.graph_name = graph_name
		self.file = open("/home/kainan/PycharmProjects/Estagio/flask/static/graph_"+graph_name+".txt",  "r")
		self.graphp4 = graphviz.Digraph()
		self.graphp4 = graphviz.Graph(filename="/home/kainan/PycharmProjects/Estagio/flask/static/graph_"+self.graph_name, format='png')
		self.arquivo = []


	def create_graph(self):
		for l in self.file:
			linha = l
			linha = linha.split()
			if(linha[0] == 'c'):
				continue
			if(linha[0] == 'e'):
				if (str(linha[1]), str(linha[2])) not in self.arquivo:
					self.graphp4.edge(str(linha[1]), str(linha[2]))
					self.arquivo.append((str(linha[1]), str(linha[2])))
	
	def view(self):
		self.graphp4.view()




app = Flask(__name__)

@app.route('/')
def index():
    return render_template("pagina.html")

@app.route('/download.html', methods=['POST'])
def down():
    graphType = request.form['graphType']
    if graphType == "connected":
        graphVertex = request.form['graphVertex']
        graphEdge = request.form['graphEdge']
        graphName = request.form['graphName']
        graphType = graphType.upper()
        graphs = graph(graphType, int(graphVertex), int(graphEdge))
        graphs.edge_generator()
        graphs.save_graph(graphName)
        figure = Generator(graphName)
        
        figure.create_graph()
        figure.view()
        return render_template("download.html", msg="http://localhost:5000/static/graph_"+graphName)

    elif graphType == "triangular":
        graphVertex = request.form['graphVertex']
        graphEdge = request.form['graphEdge']
        graphName = request.form['graphName']
        graphType = graphType.upper()
        graphs = graph(graphType, int(graphVertex), int(graphEdge))
        graphs.edge_generator()
        graphs.save_graph(graphName)
        figure = Generator(graphName)
        figure.create_graph()
        figure.view()
        return render_template("download.html", msg="http://localhost:5000/static/graph_"+graphName)

if __name__ == "__main__":
    app.run(host= '0.0.0.0') 
