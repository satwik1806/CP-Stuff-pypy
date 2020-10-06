from collections import *
def toposort(g,dependency):
    queue = deque([])
    for i in range(1,len(dependency)):
        if(dependency[i] == 0):
            queue.append(i)

    new = []
    while(len(queue)):
        s = queue.pop()
        new.append(s)
        for i in g[s]:
            dependency[i] -=1
            if(dependency[i] == 0):
                queue.append(i)
    return new

n,m = map(int,input().split())
graph = [[] for i in range(n+1)]
dependency = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    dependency[b]+=1

order = toposort(graph,dependency)
print(order)

# 10 7
# 3 2
# 4 2
# 6 5
# 7 5
# 8 7
# 9 7
# 10 9


