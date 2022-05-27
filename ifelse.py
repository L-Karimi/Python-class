# x = range(20)
# for y in x:
#   if y%2==0:
#     print(f'{y} is an even number')
#   else:
#     print(f'{y} is a odd number')

x=1
y=20
while x<y:
  x+=1
  if x%2 !=0:
    continue
  print(x)