def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)
ans=sum(5)
print(ans)