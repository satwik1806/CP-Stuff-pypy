def bs(a,l,h,x):
    while(l<h):
        # print(l,h)
        mid = (l+h)//2
        if(a[mid] == x):
            return mid
        if(a[mid] < x):
            l = mid+1
        else:
            h = mid
    return l

