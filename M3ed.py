cached_fibonacci = dict()

def fibonacci(n):
    if n==0: return 0
    if n==1: return 1
    if str(n) in cached_fibonacci: return cached_fibonacci[str(n)]
    answer = fibonacci(n-1) + fibonacci(n-2)
    cached_fibonacci[str(n)] = answer
    return answer

print( fibonacci(50) )