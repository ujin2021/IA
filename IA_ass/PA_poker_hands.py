
# coding: utf-8

# ***Jupyter Notebook에서 Download as Python으로 받으세요.***
# # PA. Find poker hands
# 포커 게임은 손에 든 패 5장을(hands라 한다) 가지고 hand의 ranking category(포커 족보)가 높은 쪽이 이기는 게임이다.
# 
# 족보에 있는지 알아 보려면, 기본적으로 다음을 check 해야 한다.
# - 5장 모두 suit이 같은지 (`is_flush`)
# - 5장 모두 rank가 연속되었는지 (`is_straight`)
# - 같은 rank가 2장인지, 3장인지, 4장인지에 따른 hand_ranking 명 (`find_a_kind)`
# 
# `tell_hand_ranking` 함수는 위 function을 이용하여 종합 판정한 결과로
# hand rnaking name을 return해야 한다.
# 
# 아래 주어진 function들을 구현하고,
# 이들이 잘 동작함을 보여주는 test case들을 만들어 시험하고 그 결과도 제출하라.
# 
# 제출요령: VS code IDE를 이용하여 script 파일을 만들고 source와 test가 실행된 결과 화면을 zip으로 압축하여 제출한다.
# 
# 참고: [List of poker hands](http://en.wikipedia.org/wiki/List_of_poker_hands)
# - Joker는 없는 것으로 한다. 따라서 'Five of a kind'는 족보에 없다.

# 편의상 suit과 rank는 문자 하나로 표기한다. 따라서 card는 a rank와 a suit으로 구성되므로 2개의 문자나 tuple로 표현할 수 있다. 
# 그리고 sorting 편의를 위해 rank를 suit 전에 두기로 한다.
# 
# 예: '3C' 또는 ('3', 'C')

ranks = '23456789TJQKA' #숫자[0]
suits = 'CDHS' #모양[1]
values = dict(zip(ranks, range(2, 2+len(ranks)))) #value of ranks
hand_ranking = {"None" : 0, "One pair" : 1, "Two pair" : 2, "Three of a kind" : 3, "Straight" : 4, "Flush" : 5, "Four of a kind" : 6}

# 족보 의 순위가 높은사람
# one pair < two pair < three of a kind < straight < flush < full house <four of a kind

# is_flush(cards) : 5의 모양(suit)이 같은지(같으면 True, 틀리면 False)
# is_straight(cards) : 5장의 숫자(rank)가 이어지는지(이어지면 sort해서 card, 아니면 None)
# classify_by_rank(cards) : 카드 숫자(rank)pair 찾기(pair 가 있으면 dict형태로, 아니면 None)
# find_a_kind(cards) : Find if one pair, two pair, or three, four of a kind, or full house(pair 족보의 이름)
# tell_hand_ranking(cards) : tell hand ranking(족보의 이름)

def is_flush(cards):
    check_set = set()
    for i in range(5):
        check_set.add(cards[i][1])
    if(len(check_set) == 1):
        return True
    else:
        return False
    
def is_straight(cards):
    cards.sort(key=lambda x: values[x[0]], reverse=True) #sort by rank
    for i in range(0, 4):
        if(values[cards[i][0]] - 1 == values[cards[i+1][0]]): #check if rank if decreasing
            continue
        else:
            return None
    return cards

def classify_by_rank(cards):
    cards.sort(key=lambda x: values[x[0]], reverse=True)  # sort by rank
    result = dict()
    count = 0 #for finding no pair

    for i in range(5):
        if(cards[i][0] in result):
            temp_list = []
            if(type(result[cards[i][0]]) == list):
                temp_list.extend(result[cards[i][0]])
            else:
                temp_list.append(result[cards[i][0]])
            temp_list.append(cards[i][1])
            result[cards[i][0]] = temp_list
        else:
            result[cards[i][0]] = cards[i][1]
            count += 1
    
    if(count < 5):
        return result
    else: #if count == 5, there is no pair
        return None

def find_a_kind(cards):
    cards_by_ranks = classify_by_rank(cards)
    if(cards_by_ranks == None): #no pair
        return None
    rank_keys = list(cards_by_ranks.keys())
    rank_values = list(cards_by_ranks.values())
    result = ""

    if(len(rank_keys) == 2): #full house or four of a kind
        if(type(rank_values[0]) == list and type(rank_values[1]) == list):
            result = "Full house"
        else:
            result = "Four of a kind"
    elif(len(rank_keys) == 3): #three of a kind two pair
        count = 0
        for i in range(3):
            if(type(rank_values[i]) == list):
                count += 1
        if(count == 1):
            result = "Three of a kind"
        else:
            result = "Two pair"
    else:
        result = "One pair"

    return result


def tell_hand_ranking(cards):
    isFlush = is_flush(cards)
    isStraight = is_straight(cards)
    findAkind = find_a_kind(cards)

    if(isFlush == False and isStraight == None and findAkind == None):
        return "None"
    elif (findAkind != None):
        return findAkind
    elif((isFlush == True and isStraight == None) or (isFlush == True and isStraight != None)):
        return "Flush"
    elif(isFlush == False and isStraight != None):
        return "Straight"


if __name__ == "__main__":    # Only if this script runs as a main,
    import random
    deck = [(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    
    player1_hand = []
    player2_hand = []
    for i in range(5):
        player1_hand.append(deck.pop())
        player2_hand.append(deck.pop())

    a = [[('3', 'D'), ('5', 'D'), ('7', 'C'), ('A', 'D'), ('4', 'D')],
        [('K', 'D'), ('J', 'D'), ('Q', 'C'), ('A', 'D'), ('T', 'D')],
        [('4', 'D'), ('4', 'C'), ('4', 'C'), ('A', 'S'), ('A', 'D')],
        [('2', 'D'), ('3', 'D'), ('4', 'C'), ('5', 'D'), ('6', 'D')],
        [('2', 'D'), ('8', 'D'), ('4', 'D'), ('5', 'D'), ('6', 'D')],
        [('2', 'D'), ('2', 'S'), ('4', 'H'), ('J', 'D'), ('6', 'D')],
        [('4', 'D'), ('A', 'H'), ('A', 'C'), ('A', 'S'), ('A', 'D')],
        [('J', 'H'), ('2', 'S'), ('J', 'S'), ('8', 'H'), ('2', 'H')],
        [('6', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')],
        [('A', 'H'), ('5', 'S'), ('4', 'S'), ('3', 'H'), ('2', 'H')],
        [('4', 'D'), ('6', 'H'), ('6', 'C'), ('6', 'S'), ('6', 'D')],
        [('8', 'H'), ('T', 'D'), ('J', 'H'), ('9', 'H'), ('Q', 'H')],
        [('T', 'H'), ('J', 'H'), ('K', 'H'), ('A', 'H'), ('Q', 'H')],
        [('5', 'S'), ('2', 'S'), ('A', 'S'), ('4', 'S'), ('3', 'S')]]
    for i in a:
        print(tell_hand_ranking(i))

    # player1_hand = [('4', 'D'), ('4', 'C'), ('4', 'C'), ('A', 'S'), ('A', 'D')]
    # player2_hand = [('J', 'D'), ('6', 'S'), ('Q', 'S'), ('9', 'S'), ('4', 'D')]
    # print("player1_hand:",player1_hand)
    # print("player2_hand:", player2_hand)
    #
    # player1 = tell_hand_ranking(player1_hand)
    # player2 = tell_hand_ranking(player2_hand)
    # print("player1 : ", player1)
    # print("player2 : ", player2)
    #
    # if(hand_ranking[player1] > hand_ranking[player2]):
    #     print("player1 win!")
    # elif(hand_ranking[player1] < hand_ranking[player2]):
    #     print("player2 win!")
    # else:
    #     print("again")

    """
           real_result.append('Ace high card')    fail     
           real_result.append('broad way straight')   ok      
           real_result.append('full house')         ok
           real_result.append('6 high straight')        ok 
           real_result.append('flush')         ok
           real_result.append('2 one pair')       ok  
           real_result.append('A four of a kind')    fail (full house)    
           real_result.append('J-2 two pairs')         ok
           real_result.append('6 high straight')        ok 
           real_result.append('baby straight')         fail (none - A를1로봐야함?)
           real_result.append('6 four of a kind')         fail (full house)
           real_result.append('Q high straight')         ok
           real_result.append('royal straight flush')      ok(straight & flush)   
           real_result.append('steel wheel')         fail(5-4-3-2-A)
    """
