from flask import Flask, request, jsonify, render_template
import math

app = Flask(__name__)

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.ai = 'O'
    
    def print_board(self):
        return self.board[:]
    
    def is_winner(self, player):
        """Check if player has won"""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False
    
    def is_board_full(self):
        """Check if board is full"""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """Get list of available positions"""
        return [i for i in range(9) if self.board[i] == ' ']
    
    def minimax(self, depth, is_maximizing):
        """Minimax algorithm with Alpha-Beta pruning"""
        # Check terminal states
        if self.is_winner(self.ai):
            return 10 - depth
        if self.is_winner(self.human):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            max_eval = -math.inf
            for move in self.get_available_moves():
                self.board[move] = self.ai
                eval_score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                max_eval = max(max_eval, eval_score)
            return max_eval
        else:
            min_eval = math.inf
            for move in self.get_available_moves():
                self.board[move] = self.human
                eval_score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                min_eval = min(min_eval, eval_score)
            return min_eval
    
    def get_best_move(self):
        """Get best move for AI using minimax"""
        best_score = -math.inf
        best_move = None
        
        for move in self.get_available_moves():
            self.board[move] = self.ai
            score = self.minimax(0, False)
            self.board[move] = ' '
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def make_move(self, position, player):
        """Make a move on the board"""
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def reset(self):
        """Reset the game"""
        self.board = [' ' for _ in range(9)]
    
    def get_game_status(self):
        """Get current game status"""
        if self.is_winner(self.ai):
            return 'ai_win'
        elif self.is_winner(self.human):
            return 'human_win'
        elif self.is_board_full():
            return 'draw'
        else:
            return 'ongoing'

# Initialize game
game = TicTacToe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_human_move():
    """Handle human player move"""
    data = request.json
    position = data.get('position')
    
    if not isinstance(position, int) or position < 0 or position > 8:
        return jsonify({'error': 'Invalid position'}), 400
    
    # Human makes move
    if not game.make_move(position, game.human):
        return jsonify({'error': 'Position already taken'}), 400
    
    # Check if human won
    status = game.get_game_status()
    if status == 'human_win':
        return jsonify({
            'board': game.board,
            'status': 'human_win',
            'message': 'You won! 🎉'
        })
    elif status == 'draw':
        return jsonify({
            'board': game.board,
            'status': 'draw',
            'message': 'It\'s a draw! 🤝'
        })
    
    # AI makes move
    ai_move = game.get_best_move()
    if ai_move is not None:
        game.make_move(ai_move, game.ai)
    
    # Check if AI won
    status = game.get_game_status()
    if status == 'ai_win':
        return jsonify({
            'board': game.board,
            'status': 'ai_win',
            'ai_move': ai_move,
            'message': 'AI won! 🤖'
        })
    elif status == 'draw':
        return jsonify({
            'board': game.board,
            'status': 'draw',
            'ai_move': ai_move,
            'message': 'It\'s a draw! 🤝'
        })
    
    return jsonify({
        'board': game.board,
        'status': 'ongoing',
        'ai_move': ai_move
    })

@app.route('/reset', methods=['POST'])
def reset_game():
    """Reset the game"""
    game.reset()
    return jsonify({
        'board': game.board,
        'status': 'reset'
    })

@app.route('/board', methods=['GET'])
def get_board():
    """Get current board state"""
    return jsonify({
        'board': game.board,
        'status': game.get_game_status()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
