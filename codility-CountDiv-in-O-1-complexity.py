def solution(A, B, K):
    if A > B:
        raise Exception('B must be greater than A!')
    if K > A and K > B:
        z = 0
    while B%K != 0:
        B-=1
    while A%K != 0:
        A+=1
    z = ((B/K) - (A/K)) + 1
    return int(z)
