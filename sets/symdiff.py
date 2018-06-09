#get the symmetric difference of two sets
a, b = input(), set(map(int,input().split()))
c, d = input(), set(map(int,input().split()))
print(*sorted(b^d,key=int),sep='\n')
