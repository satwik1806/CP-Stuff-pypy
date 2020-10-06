#========================================================================
#for min of sebstring segment tree
def BSegmentT(a,ans,st,end,pos):
    #ans is segment tree
    #pos is postion at which i need to store the value
    if(st==end):   #the only base case is
        ans[pos] = a[st]
        return  #this return is very imp. took me 10 fucking minutes to understood.

    mid = (st+end)//2
    BSegmentT(a,ans,st,mid,2*pos)
    BSegmentT(a,ans,mid+1,end,2*pos+1)
    ans[pos] = min(ans[2*pos],ans[2*pos+1])

def query(ans,l,r,st,end,pos):
    if(st>r or end<l): #no overlap scene bhaiya
        return(10**9)
    if(st>=l and end<=r): #total overlap scene bhaiya
        return (ans[pos])

    mid = (st+end)//2 #this is partial overlap
    return(min(query(ans,l,r,st,mid,2*pos),query(ans,l,r,mid+1,end,2*pos+1)))


a = list(map(int,input().split()))
x = 0
while(2**x<len(a)):
    x+=1

ans = [-1]*(2**(x+1))

BSegmentT(a,ans,0,5,1)
print(a,'  == original array')
print(ans,'  == segment tree')
print(query(ans,3,4,0,5,1),'  ==min range query')

#template for segment tree in python made by satwik. with min query
#===========================================================================
