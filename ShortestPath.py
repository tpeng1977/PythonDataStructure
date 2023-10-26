class DirectedEdge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def from_vertex(self):
        return self.v

    def to_vertex(self):
        return self.w


class EdgeWeightedDigraph:
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = {}
        for i in range(V):
            self.adj[i] = set()

    def addEdge(self, e: DirectedEdge):
        self.adj[e.from_vertex()].add(e)
        self.E += 1

    def adj_of_vertex(self, v):
        return self.adj[v]

    def edges(self):
        bag = set()
        for i in range(self.V):
            for e in self.adj[i]:
                bag.add(e)
        return bag


class SP:
    def __init__(self, G: EdgeWeightedDigraph, s):
        self.distToVertex = {}
        self.edgeTo = {}
        for i in range(G.V):
            self.distToVertex[i] = None
            self.edgeTo = None
        self.distToVertex[s] = 0

    def distTo(self, v):
        return self.distToVertex[v]

    def hasPathTo(self, v):
        if self.distToVertex[v] is None:
            return False
        else:
            return True

    def pathTo(self, v):
        if not self.hasPathTo(v):
            return None
        path = list()
        e = self.edgeTo[v]
        while e is not None:
            path.append(e)
            e = self.edgeTo[e.from_vertex]
        return path

    def relax(self, e: DirectedEdge):
        v = e.from_vertex()
        w = e.to_vertex()
        if self.distToVertex[w] is None or self.distToVertex[w] > self.distToVertex[v] + e.weight:
            self.distToVertex[w] = self.distToVertex[v] + e.weight
            self.edgeTo[w] = e


def main(G: EdgeWeightedDigraph, s: int):
    sp = SP(G, s)
    for t in range(G.V):
        print(s + " to " + t)
        print(" ({}): ".format(sp.distTo(t)))
        if sp.hasPathTo(t):
            for e in sp.pathTo(t):
                print(e + "  ", end="")
        print()


if __name__ == "__main__":
    main()
