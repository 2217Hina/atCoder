N = int(input())
cards =  list(map(int,input().split()))
Alice = 0
Bob = 0

cards.sort( reverse=True)


Alice = sum(cards[0::2])
Bob = sum(cards[1::2])

answer = Alice - Bob

print(answer)

