def locate_card(cards,query ):
    position = 0
    print(f"cards :{list(cards)}")
    print(f"query :{query}")

    high , low = len(cards)-1 , 0

    while low <= high:
        position += 1
        # print(cards[position])

        mid = (high + low) //2
        mid_number = cards[mid]
        
        print(mid_number)
    
        if query == mid_number:
            return mid_number
        elif  mid_number < query:
            high = mid - 1

        elif  mid_number > query:
            low = mid + 1        
             

    return -1
    

