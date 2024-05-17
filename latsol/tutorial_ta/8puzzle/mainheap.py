from copy import deepcopy
import heapq

# NOTE: This is the same as main.py,
# just using heapq to maintain a min-heap to the pq structure


def read_board_state(path):
    state_str = open(path, "r").readline()
    board_state = state_str.split(",")
    return board_state


def print_board_state(board):
    for row in range(0, 7):
        if row % 2 == 0:
            print("+-----+-----+-----+")
        else:
            start_id = (row // 2) * 3
            print(
                f"|{board[start_id]:>{3}}  |{board[start_id+1]:>{3}}  |{board[start_id+2]:>{3}}  |"
            )


def move_atas(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id + 3]
    new_state[current_zero_id + 3] = "0"
    return new_state


def move_bawah(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id - 3]
    new_state[current_zero_id - 3] = "0"
    return new_state


def move_kiri(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id + 1]
    new_state[current_zero_id + 1] = "0"
    return new_state


def move_kanan(current_state, current_zero_id):
    new_state = deepcopy(current_state)
    new_state[current_zero_id] = new_state[current_zero_id - 1]
    new_state[current_zero_id - 1] = "0"
    return new_state


def manhattan_distance(state, goal_state):
    distance = 0
    for i in range(9):
        if state[i] != "0":
            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_state.index(state[i]), 3)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


def update_queue_and_visited(
    queue: list, visited, new_state, move, current_state_key, cost, goal_state
):
    visited_key = ",".join(new_state)
    if visited.get(visited_key) is None or cost < visited[visited_key][1]:
        heuristic = manhattan_distance(new_state, goal_state)
        heapq.heappush(queue, (cost + heuristic, cost, new_state, move))
        visited[visited_key] = [True, cost, current_state_key, move]


def A_star(init_state: list, goal_state: list):
    queue = [(0, 0, init_state, None)]
    visited = {",".join(init_state): [True, 0, None, None]}

    while queue:
        _, cost, current_state, move = heapq.heappop(queue)
        current_state_key = ",".join(current_state)
        current_zero_id = current_state.index("0")

        if current_state == goal_state:
            print("Found solution")
            break

        # cek available move
        # tile pindah ke atas
        if current_zero_id < 6:
            new_state = move_atas(current_state, current_zero_id)
            update_queue_and_visited(
                queue, visited, new_state, "up", current_state_key, cost + 1, goal_state
            )

        # tile pindah bawah
        if current_zero_id > 2:
            new_state = move_bawah(current_state, current_zero_id)
            update_queue_and_visited(
                queue,
                visited,
                new_state,
                "down",
                current_state_key,
                cost + 1,
                goal_state,
            )

        # tile pindah kiri
        if current_zero_id % 3 < 2:
            new_state = move_kiri(current_state, current_zero_id)
            update_queue_and_visited(
                queue,
                visited,
                new_state,
                "left",
                current_state_key,
                cost + 1,
                goal_state,
            )

        # tile pindah kanan
        if current_zero_id % 3 > 0:
            new_state = move_kanan(current_state, current_zero_id)
            update_queue_and_visited(
                queue,
                visited,
                new_state,
                "right",
                current_state_key,
                cost + 1,
                goal_state,
            )

    path_key = ",".join(goal_state)
    init_key = ",".join(init_state)
    paths = []
    while path_key != init_key:
        _, _, new_key, move = visited[path_key]
        paths.append((new_key, move))
        path_key = new_key

    counter = 1
    for state_key, move in paths[::-1]:
        state = state_key.split(",")
        print(f"{counter}. Move:{move}")
        counter += 1


def main():
    init_state = read_board_state("start.txt")
    goal_state = read_board_state("goal.txt")
    print("START")
    print_board_state(init_state)
    print("GOAL")
    print_board_state(goal_state)

    # start searching
    print("Begin search ... ")
    A_star(init_state, goal_state)


if __name__ == "__main__":
    main()
