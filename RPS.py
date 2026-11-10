# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], my_history=[], play_order={}):
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        play_order.clear()

    if prev_play:
        opponent_history.append(prev_play)

    n = 3

    if len(opponent_history) >= n + 1:
        pattern = "".join(opponent_history[-(n + 1):])
        play_order[pattern] = play_order.get(pattern, 0) + 1

    guess = "R"

    if len(opponent_history) >= n:
        recent_seq = "".join(opponent_history[-n:])
        potential_next_moves = [recent_seq + "R", recent_seq + "P", recent_seq + "S"]

        predicted_move = max(
            potential_next_moves,
            key=lambda seq: play_order.get(seq, 0)
        )[-1]

        ideal_response = {"R": "P", "P": "S", "S": "R"}
        guess = ideal_response[predicted_move]

    my_history.append(guess)
    return guess
