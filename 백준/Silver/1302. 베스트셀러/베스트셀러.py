import sys
input = sys.stdin.readline

n = int(input().strip())
book = {}
for _ in range(n):
    title = input().strip()

    if title in book:
        book[title] += 1
    else:
        book[title] = 1

sorted_books = sorted(book.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])