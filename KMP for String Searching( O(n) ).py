def findoccurences(s, pat):
   arr = generatearr(pat)         #call to give arr of out pattern
   ind = []                          #stores indices
   i = 0
   j = 0
   while(i<len(s)):
       if(s[i] == pat[j]):        #current alphabet same in string and pattern
           i+=1
           j+=1
       else:
           while(s[i]!=pat[j] and j!=0):
               j = arr[j-1]
           if(s[i] == pat[j]):
               i+=1
               j+=1
           else:
               i+=1

       if(j == len(pat)):          #i if j gets out of pattern than match found.
           ind.append(i-len(pat))
           j = arr[j-1]
   return ind



def generatearr(pat):
   arr = [0]*len(pat)
   i = 1
   j = 0
   while(i<len(pat)):
       if(pat[i] == pat[j]):     # character same in prefix and suffix
           arr[i] = arr[j]+1
           j+=1
           i+=1
       else:
           while(pat[i]!=pat[j] and j!=0):
               j = arr[j-1]
           if(pat[i] == pat[j]):
               arr[i] = arr[j]+1
               j+=1
               i+=1
           else:
               arr[i] = arr[j]
               i+=1
   return arr


S = 'AABAABCAABAD'
pat = 'AABCAABA'
ans = findoccurences(S, pat)

print('pattern exists at indexes - ', end=' ')
print(' '.join(str(ans[i]) for i in range(len(ans))))
