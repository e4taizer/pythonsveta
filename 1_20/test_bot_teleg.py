import  random
print("Привет, хочешь сыграть в игру?")


print()

CARD_RANKS = ["2","3","4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_SUITS =     ['♠️','♥️', '♣','♦']
card_rank = random.choice(CARD_RANKS)
card_suit =random.choice(CARD_SUITS)
print(card_rank,card_suit)
user_answer = input('Введите "K" или "Ч": ")
print(user_answer)

if user_answer =='K' and card_suit in['♥️','♦']:
    print(Gg)
elif user_answer == 'Ч' and card_suit in []
else:
    print()

