import sys
input = sys.stdin.readline
from collections import defaultdict

# 입력 받기
n, d, k, c = map(int, input().split())
sushi = [int(input().strip()) for _ in range(n)]

# 회전 초밥 벨트를 두 배로 확장
sushi.extend(sushi[:k-1])

# 초밥 종류를 카운트할 dictionary
sushi_count = defaultdict(int)
unique_count = 0

# 초기 슬라이딩 윈도우 설정
for i in range(k):
    if sushi_count[sushi[i]] == 0:
        unique_count += 1
    sushi_count[sushi[i]] += 1

# 쿠폰 초밥 포함 여부 체크
max_unique = unique_count
if sushi_count[c] == 0:
    max_unique += 1

# 슬라이딩 윈도우 이동
for i in range(1, n):
    # 윈도우에서 제거할 초밥
    remove_sushi = sushi[i - 1]
    sushi_count[remove_sushi] -= 1
    if sushi_count[remove_sushi] == 0:
        unique_count -= 1

    # 윈도우에 추가할 초밥
    add_sushi = sushi[i + k - 1]
    if sushi_count[add_sushi] == 0:
        unique_count += 1
    sushi_count[add_sushi] += 1

    # 쿠폰 초밥 포함 여부 체크
    current_unique = unique_count
    if sushi_count[c] == 0:
        current_unique += 1

    max_unique = max(max_unique, current_unique)

print(max_unique)