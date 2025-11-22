import board as b
import game_rules as rules
import ai_agent as ai
import logger as log

def play_game():
    #Board is a list of 9 spaces
    the_board = [' ' for _ in range(9)]
    print("Welcome to Unbeatable AI Tic-Tac-Toe!")
    
    while True:
        #Human part
        b.print_board(the_board)
        try:
            user_input = int(input("Enter position (1-9): ")) 
            move = user_input - 1 
            if move < 0 or move > 8:
                print("Please enter a number between 1-9.")
                continue
            if not b.is_space_free(the_board, move):
                print("Invalid move! Try again.")
                continue
        except:
            print("Please enter a number between 1-9.")
            continue
            
        the_board[move] = 'X'

        if rules.check_win(the_board, 'X'):
            b.print_board(the_board)
            print("You Win! (This shouldn't happen...)")
            log.log_game("Human Won")
            break
        if rules.check_draw(the_board):
            print("It's a Draw!")
            log.log_game("Draw")
            break
            
        #AI part
        print("AI is thinking...")
        ai_move = ai.get_best_move(the_board)
        the_board[ai_move] = 'O'
        
        if rules.check_win(the_board, 'O'):
            b.print_board(the_board)
            print("AI Wins! Better luck next time.")
            log.log_game("AI Won")
            break
        if rules.check_draw(the_board):
            print("It's a Draw!")
            log.log_game("Draw")
            break

if __name__ == "__main__":
    play_game()
