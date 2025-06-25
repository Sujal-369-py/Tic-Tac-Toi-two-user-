def structure_of_game(): 
    arr = [['_','_','_'],
           ['_','_','_'],
           ['_','_','_']] 
    return arr  

def insert(pos,x_turn,o_turn,arr): 
    row = (pos-1)//3
    col = (pos-1)%3
    if arr[row][col] == '_' and x_turn: 
        arr[row][col] = 'X' 
        return True
    elif arr[row][col] == '_' and o_turn: 
        arr[row][col] = 'O' 
        return True
    else: 
        print("Position is already occupied.Please Try in other psoition.") 
        return False
