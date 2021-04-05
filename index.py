def t_hanoi(n, start, end, mid):
    if n==1:
        print(f"Mova {n} de {start} para {end}")
    else:
        hanoi(n-1, start, mid, end)
        print(f"Mova {n} de {start} para {end}")
        hanoi(n-1, mid, end, start)
                
t_hanoi(5, "A", "C", "B")
