import copy
from main import *

def kolorowanie(G : Graph_List, BFS = True):
    if G.size() == 0: return []
    start = G.getVertex(0)
    Color_lst = [0]
    result = []
    visited = []
    dic_map = {}
    Q = []
    Q.append(G.getVertexIdx(start))
    while Q != []:
        if BFS:
            temp = Q[0]
            Q.pop(0)
        else:
            temp = Q[-1]
            Q.pop()
        visited.append(temp)
        color = copy.deepcopy(Color_lst)
        for i in G.neighbours(temp):
            if i in visited:
                try: 
                    color.remove(dic_map[i])
                except:
                    pass
        if color != []:
            dic_map[temp] = color[0]
        else:
            Color_lst.append(Color_lst[-1] + 1)
            dic_map[temp] = Color_lst[-1]
        for i in G.neighbours(temp):
            if (i not in Q) and (i not in dic_map.keys()):
                Q.append(i)
            pass
    for i in dic_map.keys():
        result.append((G.getVertex(i).key, dic_map[i]))
    return result
    pass




g_lst = Graph_List()
for i in polska.graf:
        a = Vertex(i[0])
        b = Vertex(i[1])
        g_lst.insertVertex(a)
        g_lst.insertVertex(b)
        g_lst.insertEdge(a,b,Edge())

polska.draw_map(g_lst.edges(),kolorowanie(g_lst))
