from heapq import heappop,heappush

def djkistra(g,st,dist): #g contains b,dist(a to b) and dist is initiaalised by 10**9 initiallly
    pq = []
    dist[st] = 0
    heappush(pq,(0,st))
    while(len(pq) != 0):
        curr = heappop(pq)[1]
        for i in range(0,len(g[curr])):
            b = g[curr][i][0]
            w = g[curr][i][1]
            if(dist[b] > dist[curr] + w):
                dist[b] = dist[curr]+w
                heappush(pq,(dist[b],b))

"""
    store graph as from - (to,distance between from-to)
    example - 
    g[a].append((b,c))
    initalise distance with dist = [inf]*(n)
"""
