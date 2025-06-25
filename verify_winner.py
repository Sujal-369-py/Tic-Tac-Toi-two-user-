def verify(arr): 
    if arr[0][0] == arr[0][1] == arr[0][2] == 'X' or arr[1][0] == arr[1][1] == arr[1][2] == 'X' or arr[2][0] == arr[2][1] == arr[2][2] == 'X' or arr[0][0] == arr[1][0] == arr[2][0] == 'X' or arr[0][1] == arr[1][1] == arr[2][1] == 'X'or arr[0][2] == arr[1][2] == arr[2][2] == 'X'or arr[0][0] == arr[1][1] == arr[2][2] == 'X'or arr[0][2] == arr[1][1] == arr[2][0] == 'X':
        print("X is winner")
        print("ThankYou for playing")
        return True
    elif arr[0][0] == arr[0][1] == arr[0][2] == 'O' or arr[1][0] == arr[1][1] == arr[1][2] == 'O' or arr[2][0] == arr[2][1] == arr[2][2] == 'O' or arr[0][0] == arr[1][0] == arr[2][0] == 'O' or arr[0][1] == arr[1][1] == arr[2][1] == 'O'or arr[0][2] == arr[1][2] == arr[2][2] == 'O'or arr[0][0] == arr[1][1] == arr[2][2] == 'O'or arr[0][2] == arr[1][1] == arr[2][0] == 'O':
        print("O is winner") 
        print("ThankYou for playing")
        return True 
    else: 
        return False 
