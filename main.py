from jeopardy import Game, Jeopardy

# Example data (replace with actual question and answer files)
questions_file = "questions.txt"
answers_file = "answers.txt"
column_titles = ["Category 1", "Category 2", "Category 3"]
players = ["Player 1", "Player 2"]

# Create a Jeopardy instance
jeopardy = Jeopardy(["100","200"],column_titles)
jeopardy.fetch_questions(questions_file, answers_file)

# Create a Game instance
game = Game(jeopardy, column_titles, players, rounds=4)

# Game loop
while game.rounds > 0:
    # Display the game board
    game.show_game_board()

    # Get player input (replace with actual input handling)
    player_choice = input("Player turn: Enter row and column (e.g., 1,1): ").split(",")
    row = int(player_choice[0]) - 1  # Adjust for zero-based indexing
    column = int(player_choice[1]) - 1

    # Get the question and answer
    question = game.jeopardy.matrixQ[row][column]
    answer = game.jeopardy.matrixA[row][column]

    # Ask the question
    print(f"\n{question}")

    # Get player answer (replace with actual input handling)
    player_answer = input("Your answer: ")

    # Check the answer
    if player_answer.lower() == answer.lower():
        print("Correct!")
        game.gain_points(game.players[game.playerCount % 2], int(game.jeopardy.matrix[row][column]))
    else:
        print(f"Incorrect. The answer is: {answer}")

    # Switch to the next player
    game.playerCount += 1

    # End the round if all questions are answered
    if all(cell != "" for row in game.jeopardy.matrix for cell in row):
        game.rounds -= 1
        print("\nRound completed!")

# End of game
print("\nGame Over!")
print("Final scores:")
for i, player in enumerate(game.players):
    print(f"{player}: {game.points[i]}")