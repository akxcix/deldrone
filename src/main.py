class WayPoint:
    """
    WayPoint is a class that defines the waypoints which are available on the map
    """
    def __init__(self, name = "defaultName", lat = 0.0, lon = 0.0):
        """
        Init the class with following properties:
        name (str): name of the waypoint (default = "genericWaypoint")
        lat (float): latitude of the waypoint (defalt = 0.0)
        lon (float): longitude of the waypoint (default = 0.0)
        """
        self.name = name
        self.lat = lat
        self.lon = lon

    def __hash__(self):
        return hash((self.name, self.lat, self.lon))

    def __eq__(self, other):
        return (self.name, self.lat, self.lon) == (other.name, other.lat, other.lon)

    def __ne__(self, other):
        return not(self == other)
    
    def __str__(self):
        return "name: {}, lat: {:>8}, lon: {:>8}".format(self.name, self.lat, self.lon)

class Graph:
    """
    Graph is an directed graph of `WayPoint`s stored using an adjacency matrix
    """
    def __init__(self):
        """
        Initializes an empty graph
        """
        self._graph = dict()

    def insert(self, A):
        """
        Inserts a new node into the graph
        A (WayPoint): The node which is to be inserted
        """
        assert type(A) == WayPoint
        self._graph[A] = dict()

    def connect(self, A, B, Weight):
        """
        connects two nodes already inserted into the graph
        A (WayPoint): First Point
        B (WayPoint): Second Point 
        """
        assert type(A) == WayPoint
        assert type(B) == WayPoint
        self._graph[A][B] = Weight
        # self._graph[B][A] = Weight

    def __str__(self):
        string = []
        string.append("  ")
        string += [i.name + " " for i in self._graph.keys()]
        string += "\n"
        for i in self._graph:
            string.append(i.name + " ")
            for j in self._graph:
                try:
                    string.append(str(self._graph[i][j])+" ")
                    continue
                except:
                    string.append("0 ")
                    continue
            string.append("\n")
        return "".join(string)

if __name__ == "__main__":
    A = WayPoint("A", 14.0, 13.0)
    B = WayPoint("B", 3.14, -1.45)
    C = WayPoint("C")
    D = WayPoint("D")
    E = WayPoint("E")
    F = WayPoint("E")
    G = Graph()
    G.insert(A)
    G.insert(B)
    G.insert(C)
    G.insert(D)
    G.connect(A, B, 1)
    G.connect(A, A, 1)
    G.connect(A, C, 10)
    G.connect(C, A, -10)
    print(A)
    print(B)
    print(G)
