def locate_card(cards,query ):
    position = 0
    print(f"cards :{list(cards)}")
    print(f"query :{query}")

    high , low = len(cards)-1 , 0

    while low <= high:
        mid = (high + low) //2 
        mid_number = cards[mid]
        
        print(f" High:{high} Low:{low} Mid:{mid}  Mid number:{mid_number}")
    
        if query == mid_number:
            return cards.index(mid_number)

        elif  mid_number < query:
            high = mid - 1
        elif  mid_number > query:
            low = mid + 1        
             

    return -1


#test_cases 
test_cases= []
test_cases.append({
    "inputs":{
        "cards":[13, 11, 10, 7, 4, 3, 1, 0],
        "query":1
    },
    "output":6
})


test_cases.append({
    "inputs":{
        "cards":[4, 2, 1, -1],
        "query":4
    },
    "output":0
})


test_cases.append({
    "inputs":{
        "cards":[9,1,2],
        "query":9
    },
    "output":0
})

test_cases.append({
    "inputs":{
        "cards":[],
        "query":23
    },
    "output":-1
})
    

