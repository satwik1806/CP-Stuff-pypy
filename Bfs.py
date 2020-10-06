from collections import deque
def bfs(g,st):
    visited = [0]*(len(g))
    visited[st] = 1
    queue = deque([])
    queue.append(st)
    new = []
    while(len(queue) != 0):
        s = queue.popleft()
        new.append(s)
        for i in g[s]:
            if(visited[i] == 0):
                visited[i] = 1
                queue.append(i)
    return new
