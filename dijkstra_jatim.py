from collections import defaultdict
import sys

# ============ INISIASI GRAF ============
grafJatim = {
        'Pacitan':{'Ponorogo':78, 'Trenggalek':117},
        'Ponorogo':{'Pacitan':78, 'Trenggalek':52, 'Magetan':53, 'Madiun':29},
        'Trenggalek':{'Pacitan':117, 'Tulungagung':32, 'Ponorogo':52},
        'Magetan':{'Ponorogo':53, 'Ngawi':34, 'Madiun':24},
        'Ngawi':{'Magetan':34, 'Madiun':32, 'Bojonegoro':78},
        'Madiun':{'Ngawi':32, 'Magetan':24, 'Ponorogo':29, 'Nganjuk':50, 'Bojonegoro':110},
        'Bojonegoro':{'Ngawi':78, 'Madiun':110, 'Nganjuk':125, 'Lamongan':63, 'Tuban':65},
        'Tuban':{'Bojonegoro':65, 'Lamongan':58},
        'Lamongan':{'Tuban':58, 'Bojonegoro':63, 'Jombang':80, 'Gresik':27},
        'Gresik':{'Lamongan':27, 'Surabaya':18},
        'Jombang':{'Kediri':44, 'Nganjuk':40, 'Lamongan':80, 'Mojokerto':30},
        'Nganjuk':{'Bojonegoro':125, 'Madiun':50, 'Jombang':40, 'Kediri':28},
        'Kediri':{'Tulungagung':31, 'Blitar':44, 'Nganjuk':28, 'Jombang':44},
        'Tulungagung':{'Trenggalek':32, 'Kediri':31, 'Blitar':33},
        'Blitar':{'Tulungagung':33, 'Kediri':44, 'Malang':78},
        'Malang':{'Blitar':78, 'Lumajang':117, 'Batu':49, 'Pasuruan':55},
        'Batu':{'Malang':49, 'Mojokerto':40},
        'Mojokerto':{'Jombang':30, 'Batu':40, 'Surabaya':49, 'Sidoarjo':72, 'Pasuruan':61},
        'Sidoarjo':{'Surabaya':23, 'Mojokerto':72, 'Pasuruan':37},
        'Surabaya':{'Gresik':18, 'Mojokerto':49, 'Sidoarjo':23, 'Bangkalan':28},
        'Bangkalan':{'Surabaya':28, 'Sampang':62},
        'Sampang':{'Bangkalan':62, 'Pamekasan':33},
        'Pamekasan':{'Sampang':33, 'Sumenep':52},
        'Sumenep':{'Pamekasan':52},
        'Pasuruan':{'Sidoarjo':37, 'Mojokerto':61, 'Malang':55, 'Probolinggo':39},
        'Probolinggo':{'Pasuruan':39, 'Lumajang':46, 'Jember':96, 'Situbondo':95},
        'Lumajang':{'Malang':117, 'Probolinggo':46, 'Jember':172},
        'Jember':{'Lumajang':172, 'Probolinggo':96, 'Bondowoso':32, 'Banyuwangi':105},
        'Bondowoso':{'Jember':32, 'Situbondo':35},
        'Situbondo':{'Probolinggo':95, 'Bondowoso':35, 'Banyuwangi':94},
        'Banyuwangi':{'Jember':105, 'Situbondo':94}
}

# ============ DAFTAR KOTA DI JATIM ============
kota = list(grafJatim.keys())
kota.sort()

# ============ CLASS GRAF ============
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                               
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]
    
    def add_edge(self, u, v, weight):
        self.graph = defaultdict(dict, self.graph)
        self.graph[u][v] = weight
        self.graph[v][u] = weight
        self.graf = dict(self.graph)
        self.nodes = list(self.graph.keys())

# ============ ALGORITMA DIJKSTRA ============
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
  
    shortest_path = {}
    previous_nodes = {}
 
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value  
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

# ============ CETAK HASIL ALGORITMA DIJKSTRA ============
def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    return str(f"{shortest_path[target_node]} KM"), str(" -> ".join(reversed(path)))

# ============ MEMBUAT OBJEK GRAF ============
jatim = Graph(kota, grafJatim)

# ============ MENU PROGRAM ============
def menu():
    print()
    print("+==========================================+")
    print("|          PROGRAM MAP JAWA TIMUR          |")
    print("+==========================================+")
    print("| 1. Tampilkan Graf                        |")
    print("| 2. Tambahkan Jalur                       |")
    print("| 3. Cari Rute Terpendek                   |")
    print("| 4. Keluar Program                        |")
    print("+==========================================+")
    
ulang = True
while ulang == True:
    menu()
    pil = int(input("  Masukkan Pilihan Anda  : "))
    match pil:
        case 1:
            print()
            print("+====== GRAF JAWA TIMUR ======+")
            for i in grafJatim:
                print(f"{i} = {grafJatim.get(i)}")
            ulang = True
        case 2:
            print()
            print("+====== TAMBAHKAN JALUR ======+")
            tAsal = input(" Masukkan Kota Pertama          : ")
            tTujuan = input(" Masukkan Kota Kedua            : ")
            tJarak = int(input(" Masukkan Jalur Kedua Kota (KM) : "))
            jatim.add_edge(tAsal, tTujuan, tJarak)
            ulang = True
        case 3:
            print()
            print("+====== MENCARI RUTE TERPENDEK ======+")
            dAsal = input(" Masukkan Kota Asal         : ")
            dTujuan = input(" Masukkan Kota Tujuan       : ")
            previous_nodes, shortest_path = dijkstra_algorithm(jatim, dAsal)
            jrk, rte = print_result(previous_nodes, shortest_path, dAsal, dTujuan)
            print(f"\n====== HASIL ======:")
            print(f"Jarak Terdekat : \n{jrk}")
            print(f"Rute Terdekat : \n{rte}")
            ulang = True
        case 4:
            ulang = False
