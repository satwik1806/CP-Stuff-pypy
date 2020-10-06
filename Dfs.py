"""
    This is recursive code and will be too slow for python
"""

def dfs(v,visited,st,new):
    new.append(st)
    visited[st] = 1
    for i in v[st]:
        if(visited[i] == 0):
            dfs(v,visited,i,new)


"""
    Iterative Recursion - 
"""

from collections import deque
def dfsusingstack(v,visited,st,new):
    d = deque([])
    d.append(st)
    visited[st] = 1
    while(len(d) != 0):
        curr = d.pop()
        new.append(curr)
        for i in v[curr]:
            if(visited[i] == 0):
                visited[i] = 1
                d.append(i)

    return new

"""
    We can also use iterative recursion using generaot
    Taken from Pyrival repository made by Pajenegod - 
    https://github.com/cheran-senthil/PyRival
"""

### START ITERATE RECURSION ###
from types import GeneratorType
def iterative(f, stack=[]):
  def wrapped_func(*args, **kwargs):
    if stack: return f(*args, **kwargs)
    to = f(*args, **kwargs)
    while True:
      if type(to) is GeneratorType:
        stack.append(to)
        to = next(to)
        continue
      stack.pop()
      if not stack: break
      to = stack[-1].send(to)
    return to
  return wrapped_func
#### END ITERATE RECURSION ####



@iterative
def dfs(v,visited,st,new):
    new.append(st)
    visited[st] = 1
    for i in v[st]:
        if(visited[i] == 0):
            ok = yield dfs(v,visited,i,new)
    yield True

