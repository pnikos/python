from collections import Counter

n_shoes = int(input())
shoes = map(int, input().split())
shoes = list(shoes)
n_customers = int(input())
for i in range(n_customers):
    c_shoe_size, c_shoe_price = map(int, input())

