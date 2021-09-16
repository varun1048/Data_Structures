def locate_card(cards,query ):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
    

