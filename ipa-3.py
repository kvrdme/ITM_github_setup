'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    fromMemberDict=social_graph[from_member]
    toMemberDict=social_graph[to_member]
    
    if to_member in fromMemberDict["following"]:
        if from_member in toMemberDict["following"]:
            return "friends"
        else:
            return "follower"
    else:
        if from_member in toMemberDict["following"]:
            return "followed by"
        else:
            return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    win_cases=[]
    board_size=len(board)
    #row
    for i in range(board_size):
        win_case=[]
        for j in range(board_size):
            win_case.append((i,j))
        win_cases.append(win_case)
        
    #column
    for j in range(board_size):
        win_case=[]
        for i in range(board_size):
            win_case.append((i,j))
        win_cases.append(win_case)
        
    #diagonals
    win_case_1=[]
    win_case_2=[]
    
    for i in range(board_size):
        win_case_1.append((i, i))
        win_case_2.append((board_size - i - 1, i))

    win_cases.append(win_case_1)
    win_cases.append(win_case_2)
    

    for win_case in win_cases:
        for win_symbol in ['O','X']:               
            if all(board[y][x]==win_symbol for y,x in win_case):
                return win_symbol

    return "NO WINNER"            
        

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if first_stop == second_stop:
        total_travel_time = 0
        for leg in route_map:
            total_travel_time += route_map[leg]['travel_time_mins']
        return total_travel_time
    
    visited = set()
    queue = [(first_stop, 0)]
    queue_index = 0
    
    while queue_index < len(queue):
        current_stop, total_travel_time = queue[queue_index]
        queue_index += 1
        
        if current_stop == second_stop:
            return total_travel_time
        
        visited.add(current_stop)
        
        for leg in route_map:
            if leg[0] == current_stop and leg[1] not in visited:
                next_stop = leg[1]
                travel_time = route_map[leg]['travel_time_mins']
                queue.append((next_stop, total_travel_time + travel_time))
    
    raise ValueError(f"No route found from {first_stop} to {second_stop}")

