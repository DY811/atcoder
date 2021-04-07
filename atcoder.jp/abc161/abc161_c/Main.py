n,k = map(int,input().split())
def sa(n,k):
    if n <= abs(n-k):
        return n
    elif n > abs(n-k) and abs(n-k) <= k:
        return sa(abs(n-k),k)
    elif n > abs(n-k) and abs(n-k) > k:
        return sa((n % k),k)
print(sa(n,k))