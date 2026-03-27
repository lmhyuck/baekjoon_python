import sys
from collections import deque
input=sys.stdin.readline
# 1부터 N까지 카드존재 -> 1번 카드가 제일 위에 N번카드가 제일 아래 순서대로
# 맨위 카드를 버리고 그다음 제일 위에 있는 카드를 맨 아래로 옮기는 행위 반복
# N이 주어졌을대 마지막에 남는 카드 구하기

N=int(input())
cards=deque()

for i in range(N):
    cards.appendleft(i+1)

for _ in range(len(cards)):
    if len(cards) > 1:
        cards.pop()
        cards.rotate()
    elif len(cards) == 1:
        print(cards.popleft())
