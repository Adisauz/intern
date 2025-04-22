i = int(input(""))
p =  []
for j in range(i):
  ans = 0
  k = int(input())
  a = list(map(int, input().split()))
  for m in a:
    if m<0:
      ans += m**4
  p.append(ans)
for _ in p:
  print(p) 
