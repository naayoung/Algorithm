import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    """target보다 큰 값이 처음 나타나는 위치 반환"""
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

N, K = map(int, input().split())
score = list(map(int, input().split()))
score.sort()

# 누적합 배열 만들기
prefix = [0] * (N + 1)
for i in range(N):
    prefix[i + 1] = prefix[i] + score[i]

low, high = 0, score[-1]
ans = high

while low <= high:
    mid = (low + high) // 2
    idx = lower_bound(score, mid)  # mid보다 큰 점수의 시작 index

    cnt = N - idx  # 사탕 줄 사람 수
    total = prefix[N] - prefix[idx] - mid * cnt

    if total <= K:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
