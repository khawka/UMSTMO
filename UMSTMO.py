import networkx as nx
import time
import itertools
def modu1(G,U,N,O):


    n=len(U);
    i=0
    m=0
    S=G.subgraph(U)
    cpt=float(S.number_of_edges())
   
   
    while i< n:
        j=i
        #print(i)
        while j<n:
            
           
            b1=(O[G.nodes().index(U[i])])
           
         
            b2=(O[G.nodes().index(U[j])])
            if G.has_edge(U[i],U[j]):
                #temp=b1*b2*(1-((G.degree(U[i])*G.degree(U[j]))/(2*N)))
                temp=(1/(b1*b2))*(1-((G.degree(U[i])*G.degree(U[j]))/(2*N)))
                m=m+2*temp
            elif i==j:
                
                temp=-(1/(b1*b2))*(((G.degree(U[i])*G.degree(U[j]))/(2*N)))
                m=m+temp
            else:
                temp=-(1/(b1*b2))*((G.degree(U[i])*G.degree(U[j]))/(2*N))
                m=m+2*temp
            
            j=j+1
        i=i+1
    
    
    return(m)
parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    #print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
        
    return sorted(minimum_spanning_tree)


def UMSTMO(f,sep):
    #Graph construction  
    G=nx.read_edgelist(f, comments='#', delimiter=sep, nodetype=int,encoding='utf-8')
    #G=nx.barabasi_albert_graph(1000, 3, seed=None)
    #G=nx.read_gml(f)
    G3=nx.Graph()
    t=time.time()
    
    #number of nodes in G
    ns=G.number_of_nodes()
    #number of edges in G
    N=G.number_of_edges()
    i=0
    w1=[]
    #list of edges in la list T
    T=G.edges()
    
     
    i=0
    #joinning each edge to its weight
    z2=[]
    while i<len(T):
        # z is number of common neighbors e(i,j)
        z=len(list(nx.common_neighbors(G, T[i][0], T[i][1])))
        # x the number of neighbors i and x1 for j
        x=len(G.neighbors(T[i][0]))
        x1=len(G.neighbors(T[i][1]))
        if z>0:
            #p is the value of jaccard coefficient
            p=((z)/(x+x1+z))
            #add weight to the edge
            G[T[i][0]][T[i][1]]['weight']=p
            #list of edges and their weights
            z2.append([p,T[i][0],T[i][1]])
        else: 
            G[T[i][0]][T[i][1]]['weight']=0
            z2.append([0,T[i][0],T[i][1]])
        i=i+1
        
    
    for l in G.nodes():
        make_set(l)
    
    #sort the list of edges according to their weights
    z2.sort(reverse=True)
    B=[]
    eu=[]
    i=0
    #construction of the union of all maximum spanning tree
    print('spanning tree construction')
    for k in z2:
        #print(k)
        M=[]
        elarge=[]
        
        while i < len(z2):
            if z2[i][0]==k[0]:
                elarge.append([z2[i][1],z2[i][2]])
                i=i+1
                t8=i
            else:
                i=len(z2)
        i=t8
        for ll in elarge:
            if (find(ll[0])!=find(ll[1])):
                M.append(ll)
        for kk in M:
            union(kk[0], kk[1])
        eu.extend(M)
        B.append(elarge)
    
    
    tr1=eu           
    
    
   
    L=[]
    su=0
    cpt=0
    for i in tr1:
        G3.add_edge(i[0],i[1])
        
    
    print('extraction of list of links in the UMST G3')
    l1=[]
    
    for i in G3.nodes():
        l1.append([G3.degree(i),i])

    
    i=0
    l1.sort(reverse=True)
    ll=[]
    for k in l1:
        ll.append(k[1])
    #print(ll)
    re=[]
    re2=[]
    mm=0
    up=[]
    for k in ll:
        b=G3.neighbors(k)
        #print(b)
        c=[]
        c1=[]
        
        
        i=0
        while i <len(b):
            j=i+1
            while j<len(b):
                
                if G.has_edge(b[i],b[j]):
                    #if G[b[i]][b[j]].get("weight")>su:
                        c1.extend([b[i],b[j]])
                j=j+1
            i=i+1
        #print(c)
        
        c1=list(set(c1))    
        jj=0
        c.append(c1)
        #print(set(b)-set(c1))
        #print(len(b)-len(c1))
        if len(b)==1 :
            if not k in up :
                c.append([b[0]])
                #up.append(k)
                up.append(b[0])
        for k2 in c:
            if len(k2) >0:
                k2.append(k)
                k2.sort()
                if not k2 in re:
                    re.append(k2)
                #ll.remove(k)
                for ll2 in k2:
                    up.append(ll2)
                    
    sup=list(set(G.nodes())-set(up))
    #sup1=list(set(G.nodes())-set(G3.nodes()))
    ##print('sup', sup)
    #print('nodes',G3.nodes())
    re.sort(key=len,reverse=True)
    
    #print('re',re)
    res=re
    
    r=0
    
    #tr=G.nodes()
    #G.clear()
    
        
    print('assign nodes without local communities to the suitable group')
    for k in sup:
            #print(k)
            #G3.neighbors(k)
            max=0
            ne=G.neighbors(k)
            #print(ne)
            i=0
            while i <len(res):
                aa=len(set(ne).intersection(res[i]))
                
                if aa>=max:
                    max=aa
                    temp=i
                    if (aa)>len(ne)-aa:
                        
                        i=len(res)
                i=i+1
            if max>0:
                res[temp].append(k)
            else:
                res.append([k])
    
    
    
    print('merge the local communities with threashold 0.5')
    
    r=0
    while(r<len(res)):
        j=r+1
        while j<len(res):
            if  len(set(res[r]).intersection(res[j]))/(len(res[j]))>=0.5:
                res[r]=list(set(res[r]).union(res[j]))
                res.pop(j)
                
            else:
                j=j+1
        
            
        r=r+1
    #print(res)
    r=0
    print('merge the local communities with threashold 0.33')
    #print("r")
    while(r<len(res)):
        j=r+1
        while j<len(res):
            if  len(set(res[r]).intersection(res[j]))/(len(res[j]))>=0.33:
                res[r]=list(set(res[r]).union(res[j]))
                res.pop(j)
                
            else:
                j=j+1
        
            
        r=r+1
    #print(res)
    r=0
    print('merge the local communities with threashold 0.2')
    while(r<len(res)):
        j=r+1
        while j<len(res):
            if  len(set(res[r]).intersection(res[j]))/(len(res[j]))>=0.2:
                res[r]=list(set(res[r]).union(res[j]))
                res.pop(j)
                
            else:
                j=j+1
        
            
        r=r+1
    
    res.sort()
    res=list(res for res,_ in itertools.groupby(res))
    
    print('find the resulted communities in the file ourcomtt2')
    
    
    fichier = open("ourcomtt2.txt", "w")
    
    for res1 in res:
        for k in res1:
            fichier.write(str(k))
            fichier.write(' ')
        fichier.write('\n')
    fichier.close()
    t2=time.time()
    print('The execution time ',t2-t)
    O=[]
    for i in G.nodes():
        cpt=0
        for r in res:
            if i in r:
                cpt=cpt+1
        O.append(cpt)
    #print(O)
    print(len(O))
    N=len(G.edges())
    
    m=0
    #res=[[2, 26 ,34, 38, 46 ,90, 104 ,106, 110] ,[3, 7 ,14, 16, 33, 40, 48 ,61 ,65 ,101, 107] ,[4 ,6 ,11, 41 ,53 ,73, 75 ,82, 85, 99, 103, 108] ,[1 ,5 ,10, 17, 24 ,42, 94, 105] ,[12, 25, 29, 51, 70, 91 ],[8, 9 ,22 ,23 ,52, 69 ,78 ,79 ,109, 112 ],[13, 15, 19 ,27 ,32, 35, 37, 39, 43, 44, 55, 62 ,72 ,86, 100] ,[47, 50, 54, 59 ,68 ,74 ,84 ,89 ,111 ,115 ],[20, 30, 31, 36 ,56, 80, 81, 83, 95, 102 ],[18 ,21 ,28 ,57 ,60, 63 ,64, 66, 71, 77, 88, 96, 97, 114] ,[45, 49 ,58, 67 ,76, 87, 92, 93, 98, 113 ]]
    #[[2 ,3, 4 ,8 ,9 ,10 ,14 ,15, 16, 19, 21, 23, 24, 25, 26, 27 ,28 ,29, 30, 31 ,32, 33, 34],[1, 2, 3, 4 ,5, 6, 7, 8 ,11, 12, 13, 14 ,17, 18, 20, 22]] 

    #[[2 ,3, 4 ,8 ,9 ,10 ,14 ,15, 16, 19, 21, 23, 24, 25, 26, 27 ,28 ,29, 30, 31 ,32, 33, 34],[1, 2, 3, 4 ,5, 6, 7, 8 ,11, 12, 13, 14 ,17, 18, 20, 22]] 

    m=0
    for i in res:
        print(i)
        m=m+modu1(G,list(i),N,O)
        
    m=m/(2*N)
    print('The overlapping modularity',m)