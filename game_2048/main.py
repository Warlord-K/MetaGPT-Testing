import game

def main():
    # Initialize the Game object with default values
    game_instance = game.Game(difficulty=1, max_value=2048)
    
    while True:
        # Get the current state of the board and UI
        board = game_instance.get_board().get_grid()
        theme = game_instance.get_ui().get_theme()
        
        # Print the current state of the board and UI
        print("Board:")
        for row in board:
            print(row)
        print("\nTheme:", theme)
        
        # Play the game
        game_instance.play()
