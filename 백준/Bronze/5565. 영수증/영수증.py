import sys
input = sys.stdin.readline

price = int(input().strip())
book_price = 0
for _ in range(9):
    book = int(input().strip())
    book_price += book

print(price-book_price)