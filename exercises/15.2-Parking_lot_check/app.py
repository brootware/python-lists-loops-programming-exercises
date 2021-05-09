parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
    state = {
        "total_slots" : 0,
        "available_slots" : 0,
        "occupied_slots" : 0
    }

    for row in parking_state:
        for col in row:
            if col == 1:
                state["occupied_slots"] += 1
                state["total_slots"] += 1
            elif col == 2:
                state["available_slots"] += 1
                state["total_slots"] += 1

    return state          

print(get_parking_lot())