import random
import sys
from collections import defaultdict
from abc import ABCMeta, abstractmethod

# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit

    def __repr__(self):
        return self.card

    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")


    # card comparison operators
    def __gt__(self, other):
        return self.value() > other.value()

    def __ge__(self, other):
        return self.value() >= other.value()

    def __lt__(self, other):
        return self.value() < other.value()

    def __le__(self, other):
        return self.value() <= other.value()

    def __eq__(self, other):
        return self.value() == other.value()

    def __ne__(self, other):
        return self.value() != other.value()

#  0,   1,   2,   3,   4,   5,   6,   7,   8,    9,   10,  11,  12
# '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
#  2,   3,   4 ,  5,   6,   7,   8,   9,   10,   11,  12,  13,  14
class PKCard(Card):
    """Card for Poker game
    """
    def value(self):
        return ranks.index(self.card[0]) + 2

    def suit_value(self):
        return self.card[1]
    pass


class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.deck = [cls(r + s) for s in suits for r in ranks]

    def __str__(self):
        return f'{self.deck}'

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, index):
        return self.deck[index]

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop(self):
        return self.deck.pop()

    pass


class Hands:
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)


    def is_flush(self, cards):  # suits가 같고 rank만 다른것
        # """"return: bool
        # """
        check_suit = []
        for i in range(len(cards)):
            check_suit.append(PKCard.suit_value(cards[i]))
        # print(check_suit)
        if len(set(check_suit)) == 1:
            return "Flush", sorted([PKCard.value(i) for i in cards], reverse= True)
        else:
            return None
        pass

    def is_straight(self, cards):  # suits는 달라도 rank가 순차적
        """:return: the cards making flush in decreasing order if found,
                None, otherwise
        """
        rank_values = sorted([PKCard.value(i) for i in cards], reverse= True)
        # print("rank_values", rank_values)
        for i in range(len(rank_values) - 1):
            if rank_values[i] - rank_values[i + 1] == 1:
                continue
            else:
                return None


        # value = sorted(cards, reverse= True)
        return "Straight", rank_values[0]

    def classify_by_rank(self, cards):
        """Classify the cards by ranks.

        :return: dict of the form { rank: [card, ...], ...}
            None if same ranks not found
        """
        classify_list = defaultdict(list)
        for i in cards:
            classify_list[PKCard.value(i)].append(PKCard.suit_value(i))

        if len(classify_list) >= 0:
            return classify_list

        pass

    def find_a_kind(self, cards):
        """Find if one pair, two pair, or three, four of a kind, or full house

        :return: hand-ranking name including 'Full house'
        """
        cards_by_ranks = self.classify_by_rank(cards)
        # print(cards_by_ranks)
        dictkey = list(cards_by_ranks.keys())
        dictvalue = list(cards_by_ranks.values())
        # print(dictkey)
        # print(dictvalue)


        # one pair
        if len(cards_by_ranks) == 4:
            newlist = []
            for i in range(len(dictvalue)):
                if len(dictvalue[i]) == 2:
                    newlist.append(dictkey[i])
                    newlist += sorted((dictkey[0:i] + dictkey[i+1:]), reverse= True)

            return "One pair", newlist

        # Two pair || Three of a kind
        elif len(cards_by_ranks) == 3:
            for i in range(len(dictvalue)):
                # Two pair
                if len(dictvalue[i]) == 2:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 2:
                            newlist.insert(0, dictkey[i])
                        elif len(dictvalue[i]) == 1:
                            newlist.append(dictkey[i])

                    if newlist[0] < newlist[1]:
                        temp = newlist[1]
                        newlist[1] = newlist[0]
                        newlist[0] = temp

                    return "Two pair", newlist

                # Three of a kind
                elif len(dictvalue[i]) == 3:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 3:
                            newlist.insert(0, dictkey[i])
                            newlist += sorted((dictkey[0:i] + dictkey[i+1:]), reverse= True)

                    return "Three of a kind", newlist

        # Full house || Four of a kind
        elif len(cards_by_ranks) == 2:
            for i in range(len(dictvalue)):
                # Full house
                if len(dictvalue[i]) == 3:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 3:
                            newlist.insert(0, dictkey[i])
                        else:
                            newlist.append(dictkey[i])

                    return "Full house", newlist

                # Four of a kind
                elif len(dictvalue[i]) == 4:
                    newlist = []
                    for i in range(len(dictvalue)):
                        if len(dictvalue[i]) == 4:
                            newlist.insert(0, dictkey[i])
                        else:
                            newlist.append(dictkey[i])

                    return "Four of a kind", newlist
        # High card
        elif len(cards_by_ranks) == 5:
            return "High card", sorted(dictkey, reverse= True)

        pass

    def tell_hand_ranking(self, cards):
        straight_val = self.is_straight(cards)
        flush_val = self.is_flush(cards)
        find_val = self.find_a_kind(cards)

        if straight_val and (find_val[0] == "High card") and not flush_val:
            return straight_val
        elif straight_val and flush_val:
            return "Straight flush", self.is_straight(cards)[1]
        elif (find_val[0] == "High card") and flush_val:
            return flush_val
        elif find_val[0] == "High card":
            return find_val
        elif find_val and not straight_val:
            return find_val

        pass

    def tie_break(self, other):
        rank_list = {"High card" : 0, "One pair" : 1, "Two pair" : 2, "Three of a kind" : 3, "Straight" : 4,
                     "Flush" : 5, "Full house" : 6, "Four of a kind" : 7, "Straight flush" : 8}
        player1 = self.tell_hand_ranking(self.cards)
        player2 = other.tell_hand_ranking(other.cards)

        if rank_list[player1[0]] > rank_list[player2[0]]:
            return True
        elif rank_list[player1[0]] == rank_list[player2[0]]:
            # High card
            if rank_list[player1[0]] == 0:
                for i in range(len(player1[1])):
                    if player1[1][i] > player2[1][i]:
                        return True
                    elif player1[1][i] < player2[1][i]:
                        return False

            # One pair
            elif rank_list[player1[0]] == 1:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1[1])):
                        if player1[1][i] > player2[1][i]:
                            return True
                        elif player1[1][i] < player2[1][i]:
                            return False

            # Two pair
            elif rank_list[player1[0]] == 2:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False
                    elif player1[1][1] == player2[1][1]:
                        if player1[1][2] > player2[1][2]:
                            return True
                        elif player1[1][2] < player2[1][2]:
                            return False

            # Three of a kind
            elif rank_list[player1[0]] == 3:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1)):
                        if player1[1][i] > player2[1][i]:
                            return True
                        elif player1[1][i] < player2[1][i]:
                            return False

            # Straight
            elif rank_list[player1[0]] == 4:
                if player1[1] > player2[1]:
                    return True
                elif player1[1] < player2[1]:
                    return False

            # Flush
            elif rank_list[player1[0]] == 5:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    for i in range(1, len(player1)):
                        if player1[1][i] > player2[1][i]:
                            return True
                        if player1[1][i] < player2[1][i]:
                            return False

            # Full house
            elif rank_list[player1[0]] == 6:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False

            # Four of a kind
            elif rank_list[player1[0]] == 7:
                if player1[1][0] > player2[1][0]:
                    return True
                elif player1[1][0] < player2[1][0]:
                    return False
                elif player1[1][0] == player2[1][0]:
                    if player1[1][1] > player2[1][1]:
                        return True
                    elif player1[1][1] < player2[1][1]:
                        return False

            # straight flush
            elif rank_list[player1[0]] == 8:
                if player1[1] > player2[1]:
                    return True
                elif player1[1] < player2[1]:
                    return False
        else:
            return False

if __name__ == '__main__':
    #
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)

    # your test cases here
    test_code = [Hands([PKCard('3D'), PKCard('5D'), PKCard('7C'), PKCard('AD'), PKCard('4D')]),
                 Hands([PKCard('KD'), PKCard('JD'), PKCard('QC'), PKCard('AD'), PKCard('TD')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # high card < straight => False

    test_code = [Hands([PKCard('4D'), PKCard('4C'), PKCard('4C'), PKCard('AS'), PKCard('AD')]),
                 Hands([PKCard('2D'), PKCard('3D'), PKCard('4C'), PKCard('5D'), PKCard('6D')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # full house > straight => True

    test_code = [Hands([PKCard('2D'), PKCard('8D'), PKCard('4D'), PKCard('5D'), PKCard('6D')]),
                 Hands([PKCard('2D'), PKCard('2S'), PKCard('4H'), PKCard('JD'), PKCard('6D')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # flush > one pair => True

    test_code = [Hands([PKCard('4D'), PKCard('AH'), PKCard('AC'), PKCard('AS'), PKCard('AD')]),
                 Hands([PKCard('JH'), PKCard('2S'), PKCard('JS'), PKCard('8H'), PKCard('2H')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # four of a kind > two pair => True

    test_code = [Hands([PKCard('2D'), PKCard('8D'), PKCard('4D'), PKCard('5D'), PKCard('6D')]),
                 Hands([PKCard('6H'), PKCard('5S'), PKCard('4S'), PKCard('3H'), PKCard('2H')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # flush > straight => True

    test_code = [Hands([PKCard('QC'), PKCard('QS'), PKCard('2S'), PKCard('QH'), PKCard('9H')]),
                 Hands([PKCard('4D'), PKCard('4C'), PKCard('4C'), PKCard('AS'), PKCard('AD')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # three of a kind < full house => False

    # 같은 hand_ranking 일 때
    test_code = [Hands([PKCard('TC'), PKCard('8S'), PKCard('7S'), PKCard('6H'), PKCard('4C')]),
                 Hands([PKCard('TD'), PKCard('8D'), PKCard('7D'), PKCard('6H'), PKCard('3D')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # high card(T-8-7-6-4) > high card(T-8-7-6-3) => True

    test_code = [Hands([PKCard('TS'), PKCard('8S'), PKCard('TH'), PKCard('7H'), PKCard('4C')]),
                 Hands([PKCard('2D'), PKCard('2S'), PKCard('4H'), PKCard('JD'), PKCard('6D')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # one pair(T) > one pair(2) => True

    test_code = [Hands([PKCard('2S'), PKCard('8S'), PKCard('2H'), PKCard('7H'), PKCard('4C')]),
                 Hands([PKCard('2D'), PKCard('2C'), PKCard('4H'), PKCard('JD'), PKCard('6D')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # one pair(2-8) < one pair(2-J) => False

    test_code = [Hands([PKCard('5C'), PKCard('5S'), PKCard('4S'), PKCard('4H'), PKCard('TH')]),
                 Hands([PKCard('5C'), PKCard('5S'), PKCard('3C'), PKCard('3D'), PKCard('QH')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # two pair(5-4) > two pair(5-3) => True

    test_code = [Hands([PKCard('KD'), PKCard('KS'), PKCard('7D'), PKCard('7H'), PKCard('8H')]),
                 Hands([PKCard('KC'), PKCard('KS'), PKCard('7S'), PKCard('7H'), PKCard('6H')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # two pair(K-7-8) > two pair(K-7-6) => True

    test_code = [Hands([PKCard('3D'), PKCard('3S'), PKCard('3C'), PKCard('JC'), PKCard('7H')]),
                 Hands([PKCard('3D'), PKCard('3S'), PKCard('3C'), PKCard('JS'), PKCard('5H')])]
    print(test_code[0].tell_hand_ranking([PKCard('3D'), PKCard('3S'), PKCard('3C'), PKCard('JC'), PKCard('7H')]))
    print(test_code[1].tell_hand_ranking([PKCard('3D'), PKCard('3S'), PKCard('3C'), PKCard('JS'), PKCard('5H')]))
    test(test_code[0].tie_break(test_code[1]) == True)  # three of a kind(3-j-7) > three of a kind(3-j-5) => True ---fail

    test_code = [Hands([PKCard('AH'), PKCard('5S'), PKCard('4S'), PKCard('3H'), PKCard('2H')]),
                 Hands([PKCard('6H'), PKCard('5S'), PKCard('4S'), PKCard('3H'), PKCard('2H')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # straight(5) < straight(6) => False

    test_code = [Hands([PKCard('KD'), PKCard('JD'), PKCard('9D'), PKCard('6D'), PKCard('4D')]),
                 Hands([PKCard('QC'), PKCard('JC'), PKCard('7C'), PKCard('6C'), PKCard('5C')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # flush(K) < flush(Q) => True

    test_code = [Hands([PKCard('JH'), PKCard('TH'), PKCard('8H'), PKCard('4H'), PKCard('3H')]),
                 Hands([PKCard('JC'), PKCard('TC'), PKCard('8C'), PKCard('4C'), PKCard('2C')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # flush(j-t-8-4-3) > flush(j-t-8-4-2) => True ----fail

    test_code = [Hands([PKCard('8S'), PKCard('8D'), PKCard('8H'), PKCard('7D'), PKCard('7C')]),
                 Hands([PKCard('4D'), PKCard('4C'), PKCard('4S'), PKCard('9D'), PKCard('9C')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # full house(8) > full house(4) => True

    test_code = [Hands([PKCard('8S'), PKCard('8D'), PKCard('8H'), PKCard('7D'), PKCard('7C')]),
                 Hands([PKCard('8D'), PKCard('8C'), PKCard('8S'), PKCard('9D'), PKCard('9C')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # full house(8-7) < full house(8-9) => False

    test_code = [Hands([PKCard('5C'), PKCard('2D'), PKCard('5D'), PKCard('5H'), PKCard('5S')]),
                 Hands([PKCard('4D'), PKCard('6H'), PKCard('6C'), PKCard('6S'), PKCard('6D')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # four of a kind(5) < four of a kind(6) => False

    test_code = [Hands([PKCard('5C'), PKCard('2D'), PKCard('5D'), PKCard('5H'), PKCard('5S')]),
                 Hands([PKCard('4D'), PKCard('5H'), PKCard('5C'), PKCard('5S'), PKCard('5D')])]
    test(test_code[0].tie_break(test_code[1]) == False)  # four of a kind(5-2) < four of a kind(5-4) => False

    test_code = [Hands([PKCard('TH'), PKCard('JH'), PKCard('KH'), PKCard('AH'), PKCard('QH')]),
                 Hands([PKCard('5S'), PKCard('2S'), PKCard('AS'), PKCard('4S'), PKCard('3S')])]
    test(test_code[0].tie_break(test_code[1]) == True)  # straight flush(A) > straight flush(5) => True