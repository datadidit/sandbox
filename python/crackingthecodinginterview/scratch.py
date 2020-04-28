import copy

def cellCompete(states, days):
    '''
        states: 8 length array with 0 and 1's
        days: number of days to run the test
    '''
    prev_state = copy.copy(states)
    print(prev_state)
    for i in range(days):
        # Loop over number of days
        for idx, val in enumerate(prev_state):
            # 1 = active, 0 = inactive
            # if both neighbors inactive/active the next state is inactive
            # Unoccupied space next to ends inactive
            if idx - 1 >= 0:
                left_neighbor = prev_state[idx - 1]
            else:
                left_neighbor = 0

            if idx + 1 < len(prev_state):
                right_neighbor = prev_state[idx + 1]
            else:
                right_neighbor = 0

            print(f"left_neighbor={left_neighbor}, right_neighbor={right_neighbor}, idx={idx}")
            if right_neighbor == left_neighbor:
                state_update = 0
            else:
                state_update = 1
            print(f"left_neighbor={left_neighbor}, right_neighbor={right_neighbor}, idx={idx}, state_update={state_update}")
            states[idx] = state_update
        prev_state = copy.copy(states)

    return states


def generalizedGCD(num, arr):
    max_num = max(arr)
    max_denom = 1
    for i in range(1, max_num + 1):
        common_denom = True
        for entry in arr:
            if entry % i != 0:
                common_denom = False
                break

        print(f"i={i} common_denom={common_denom}, max_denom={max_denom}")
        if common_denom and i > max_denom:
            max_denom = i

    return max_denom


def numberAmazonGoStores(rows, column, grid):
    '''

    :param rows:
    :param column:
    :param grid:
    :return:
    '''
    # Builing = 1, land area = 0
    # adjacent blocks with value 1 are considered clusters of buildings
    # diagonal blocks w/ 1 are not clusters
    # 1 store in each cluster
    # What is adjacent
    clusters = 0
    for row_idx in range(rows):
        for column_idx in range(column):
            # For each entry figure out if there's a cluster
            current = grid[row_idx][column_idx]
            if column_idx + 1 < column:
                # Get right neighbor
                right_neighbor = grid[row_idx][column_idx + 1]
            else:
                right_neighbor = None

            if row_idx + 1 < rows:
                bottom_neighbor = grid[row_idx + 1][column_idx]
            else:
                bottom_neighbor = None

            if row_idx + 1 < rows and column_idx + 1 < column:
                diagonal_below = grid[row_idx + 1][column_idx + 1]
            elif row_idx + 1 == rows and column_idx + 1 == column:
                # Special Case
                diagonal_below = grid[row_idx - 1][column_idx - 1]
            else:
                diagonal_below = None

            if row_idx - 1 > 0 and column_idx + 1 < column:
                diagonal_above = grid[row_idx - 1][column_idx + 1]
            else:
                None

            if current and right_neighbor:
                clusters+=1
            if current and bottom_neighbor:
                clusters+=1
            if current and diagonal_below:
                clusters+=1
            if current and diagonal_above:
                clusters+=1

    return clusters


if __name__ == "__main__":
    # t1 = [1, 0, 0, 0, 0, 1, 0, 0]
    # print(cellCompete(t1, 1))
    # print(generalizedGCD(5, [2, 4, 6, 8, 10]))
    t1 = [[1, 1, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 0, 0]]
    t2 = [[1, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 1]]
    t3 = [[1, 1],
          [1, 1]]
    print(numberAmazonGoStores(4, 4, t1))
    print(numberAmazonGoStores(7, 7, t2))
    print(numberAmazonGoStores(2, 2, t3))
