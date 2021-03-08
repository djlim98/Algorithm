N, S = map(int, input().split())
A = list(map(int, input().split()))
left, right, hap, result, temp = 0, 0, A[0], 0, 0
while left <= right and right < N:
    if hap < S:
        right += 1
        if right < N:
            hap += A[right]
    elif hap >= S:
        temp = right - left + 1
        if result == 0:
            result = temp
        else:
            result = min(result, temp)
        if left < right:
            hap -= A[left]
            left += 1
        else:
            right += 1
            if right < N:
                hap += A[right]
print(result)