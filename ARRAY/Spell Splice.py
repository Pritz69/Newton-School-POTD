# Your code here
for _ in range(int(input())) :
    n=int(input())
    spells=[]
    for i in range(n) :
        spells.append(list(map(int,input().split())))
    max_strength = 0
    for i in range(n):
        for j in range(i + 1, n):
            Vi, Ai = spells[i]
            Vj, Aj = spells[j]
            strength = Ai * Vj + Aj * Vi
            if strength > max_strength:
                max_strength = strength
    print(max_strength)
