def t_hanoi(n, start, end, mid):
    if n==1:
        t_print(f"Mova {n} de {start} para {end}")
    else:
        t_hanoi(n-1, start, mid, end)
        print(f"Mova {n} de {start} para {end}")
        t_hanoi(n-1, mid, end, start)
                
t_hanoi(5, "A", "C", "B")
