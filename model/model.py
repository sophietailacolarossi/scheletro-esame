import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = []
        self._idMap = {}
        self._edges = []
        self._bestPath = None
        self._maxLen = None
        self._valore=None

    def returnDD(self):
        return DAO.getDD()

    def buildGraph(self, valore):
        if self._valore==valore:
            return
        self._graph.clear()
        self._nodes = []
        self._edges = []
        self._idMap = {}
        self._nodes=DAO.getNodes()
        self._graph.add_nodes_from(self._nodes)
        for nodo in self._nodes:
            self._idMap[nodo.id]=nodo
        self.addEdges()
        self._valore=valore

    def addEdges(self):
        archi=DAO.getAllEdges()
        for u_id, v_id in archi:
            if u_id in self._idMap and v_id in self._idMap:
                u = self._idMap[u_id]
                v = self._idMap[v_id]
                self._graph.add_edge(u, v)
                self._edges.append((u, v))

    def getNumNodi(self):
        return self._graph.number_of_nodes()

    def getNumArchi(self):
        return self._graph.number_of_edges()

    def stampaDettagli1(self):
        pass

    def stampaDettagli2(self):
        pass

    def stampaDettagli3(self):
        pass

    def handleRicorsione(self):
        pass

    def ricorsione(self):
        pass



