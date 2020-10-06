"""
self BIT
"""

class BIT:
    def __init__(self,n):
        self.n = n
        self.tree = [0]*(n+1)

    def sum(self,x):
        sum = 0
        while(x>0):
            sum+=self.tree[x]
            x-=x&(-x)
        return sum

    def update(self,x,k):
        while(x<=self.n):
            self.tree[x]+=k
            x+=x&(-x)

    def build(self,a):
        for i in range(len(a)):
            k = a[i]
            x = i+1
            while(x<=self.n):
                self.tree[x]+=k
                x+=x&(-x)

    def findkth(self, k):
        # """Find largest idx such that sum(bit[:idx]) <= k"""
        # find the index of kth element in sorted list
        idx = -1
        for d in reversed(range(len(self.tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.tree) and k >= self.tree[right_idx]:
                idx = right_idx
                k -= self.tree[idx]
        return idx + 1



# a = [1,2,3,4,5,1]
# bit = BIT(len(a))
# bit.build(a)
# print(bit.sum(6))
# bit.update(3,-3)
# print(bit.sum(4))

# ----------------------------------------------------------------

"""
    taken form pyrival , inspired from this code - 
    https://github.com/cheran-senthil/PyRival
"""
class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1

"""
    arr = [*,*,*,*,*,*,*]
    bit  =  Fenwick(arr)
    bit this is range sum
"""
