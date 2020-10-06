
def makepreferedmoretbale(Wprefer):
    new = [[0]*n for i in range(n)] #for storing the position of all men in preference order
    for i in range(n):
        for j in range(n):
            new[i][Wprefer[i][j]] = j
    return new

def solve(Mprefer,preferedmore):
    matched = [False]*n  #marking all false
    mapping = {} # Woman -> Man
    notmatchedtillnow = n

    while(notmatchedtillnow > 0):
        currman = 0
        for i in range(n):
            if(not matched[i]): #picking a currman which is not matched till yet
                currman = i
                break

        for i in Mprefer[currman]:
            if(i not in mapping):  #this woman is not matched yet
                mapping[i] = currman
                notmatchedtillnow -=1
                matched[currman] = True #matched the man and woman and break
                break
            else:
                if(preferedmore[i][currman] < preferedmore[i][mapping[i]]): #this man is prefered more than the current partner.
                    matched[mapping[i]] = False
                    matched[currman] = True
                    mapping[i] = currman
                    break

    return mapping




"""
lets say we have preference order of man 0,1,2,3,4
and woman 0,1,2,3,4 as

M0 - 2,4,3,1,0
M1 - 2,3,1,0,4
M2 - 3,0,4,1,2
M3 - 0,2,3,1,4
M4 - 4,1,2,0,3

given in a grid form.

W0 - 2,3,1,0,4
W1 - 1,0,4,2,3
W2 - 0,2,1,4,3
W3 - 0,2,1,3,4
W4 - 4,0,3,1,2

"""
n = 5 #number of pairs.
Mpreference = [[2,4,3,1,0],[2,3,1,0,4],[3,0,4,1,2],[0,2,3,1,4],[4,1,2,0,3]]
Wpreference = [[2,3,1,0,4],[1,0,4,2,3],[0,2,1,4,3],[0,2,1,3,4],[4,0,3,1,2]]

#to chck if a man is prefered more than the other man.
#we'll make a preference table for women preferences.

preferedmore = makepreferedmoretbale(Wpreference)

matches = solve(Mpreference,preferedmore)

print("Woman" , "Man")
for i in matches:
    print(i , "   " , matches[i])

