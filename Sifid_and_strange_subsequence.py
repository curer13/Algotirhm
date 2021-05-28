n=3
a=[1,2,3]

def isStrange(a,n):
    m=max(a)
    for i in range(n-1):
        for j in range(i+1,n):
            if abs(a[i]-a[j])<m:
                return False
    return True

def subs(m,n,k):
    if k>m:
        return k
    for i in range(k,n-m+k):
        print(i,subs(m,n,k+1))

subs(2,3,0)



# if isStrange(a,n):
  #  print(n)



# longest=a.copy()
# print(longest)
# for i in range(1,n):
  #   for j in range(n):
   #      print(a[:j]+a[j+1:])

# print(longest)