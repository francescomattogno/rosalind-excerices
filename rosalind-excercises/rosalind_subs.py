def rossubs(a, b):
    positions = []
    for i in range(len(a)):
        if b == a[i: i+len(b)]:
            positions.append(i+1)
    return positions

f=open('rosalind_subs.txt','r')
a = f.readline().strip()
b = f.readline().strip()
positions = rossubs(a, b)
for i in positions:
    print(i, end=" ")