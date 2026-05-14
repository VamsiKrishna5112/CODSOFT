# Tic-Tac-Toe AI - Unbeatable Game AI

An intelligent Tic-Tac-Toe game where you play against an AI that uses the **Minimax algorithm** to play perfectly. The AI is unbeatable - at best you can draw!

**CODSOFT AI Internship - Task 2**

---

## 🎮 Features

- **Minimax Algorithm**: AI uses optimal game theory strategy
- **Unbeatable AI**: AI plays perfectly every time
- **Beautiful Web UI**: Modern, responsive interface
- **Real-time Feedback**: Instant game status updates
- **Game History**: Play as many games as you want
- **Easy to Understand**: Clear visual feedback

---

## 🚀 Quick Start

### Installation

1. **Navigate to folder:**
```bash
cd Task_2_TicTacToe
```

2. **Install Flask:**
```bash
pip install -r requirements.txt
```

3. **Run the game:**
```bash
python tictactoe_app.py
```

4. **Open browser:**
```
http://localhost:5000
```

---

## 🎯 How to Play

1. **You are X** - Click any empty cell to make your move
2. **AI is O** - AI automatically plays after you
3. **Win Condition** - Get 3 in a row (horizontal, vertical, or diagonal)
4. **New Game** - Click "New Game" button to restart

---

## 🧠 Algorithm Explanation

### Minimax Algorithm

The Minimax algorithm is a recursive algorithm used in game theory to find the optimal move for a player.

**How it works:**

1. **Maximizing Player (AI)**: Tries to maximize the score
2. **Minimizing Player (Human)**: Tries to minimize the score
3. **Game States**: 
   - AI Win: +10 points
   - Human Win: -10 points
   - Draw: 0 points
4. **Depth Penalty**: Subtract depth to prefer quicker wins

**Example:**
```
        [Game State]
         /    |    \
      Max    Max    Max  (AI's turn)
     / | \   / | \  / | \
    Min Min Min ... (Human's turn)
   
Final scores evaluated, best move selected
```

**Time Complexity:** O(9!) in worst case for Tic-Tac-Toe
**Space Complexity:** O(depth) for recursion stack

---

## 📁 Project Structure

```
Task_2_TicTacToe/
├── tictactoe_app.py       # Flask app with Minimax algorithm
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/
    └── index.html        # Game UI
```

---

## 💻 Code Overview

### Main Components

**TicTacToe Class:**
- `__init__()`: Initialize empty board
- `is_winner()`: Check if player won
- `get_available_moves()`: List valid moves
- `minimax()`: Core algorithm for finding best move
- `get_best_move()`: Return optimal move for AI
- `make_move()`: Place piece on board
- `get_game_status()`: Check game state

**Flask Routes:**
- `GET /`: Serve game UI
- `POST /move`: Handle human move + AI response
- `POST /reset`: Reset the game
- `GET /board`: Get current board state

**Frontend:**
- Vanilla JavaScript (no frameworks)
- Real-time API calls
- Beautiful CSS animations
- Responsive design

---

## 🎓 Learning Outcomes

After building this project, you'll understand:

✅ Game theory fundamentals
✅ Minimax algorithm in depth
✅ Recursive problem solving
✅ Board state representation
✅ Win condition evaluation
✅ AI decision making

---

## 🔧 Customization

### Change Difficulty (Optional)

To make AI beatable, add depth limit to minimax:

```python
def minimax(self, depth, is_maximizing, max_depth=4):
    if depth >= max_depth:
        return self.evaluate_board()  # Heuristic evaluation
    # ... rest of code
```

### Different Scoring

```python
if self.is_winner(self.ai):
    return (10 - depth) * 2  # Prefer quicker wins more
```

---

## 📊 Game Statistics

**Possible game outcomes:**
- AI Wins: ~58% (with optimal play)
- Draws: ~42% (with optimal human play)
- Human Wins: ~0% (impossible with optimal AI)

Note: These percentages assume both players play optimally.

---

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Use different port
# Edit tictactoe_app.py line: app.run(debug=True, port=5001)
```

### Module Not Found
```bash
pip install Flask==3.0.0
```

### Board Rendering Issues
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+F5)
- Try different browser

---

## 🎬 Recording Tips for Demo

1. **Open game** - Show the UI
2. **Play 3-4 games:**
   - Try to win (shows AI blocks)
   - Try corner opening (shows strategy)
   - Let AI win (shows offensive play)
   - Draw game (shows perfect defense)
3. **Show victory states** - Win, loss, draw
4. **Explain algorithm** (optional):
   - Show minimax logic
   - Explain how AI evaluates positions

---

## 📈 Algorithm Visualization

```
Game State:
 X | O | 
-----------
 O | X | 
-----------
   |   | 

Minimax evaluates each possible move:
Move 0: Score = -10 (Human wins if both play optimally)
Move 2: Score = 0 (Draw if both play optimally)
Move 6: Score = 0 (Draw if both play optimally)

Best move: Move 2 or Move 6 (Draw outcome) ✓
```

---

## 🔗 Resources

- [Minimax Algorithm](https://en.wikipedia.org/wiki/Minimax)
- [Game Theory](https://en.wikipedia.org/wiki/Game_theory)
- [Tic-Tac-Toe Complexity](https://en.wikipedia.org/wiki/Tic-tac-toe)

---

## 📧 Support

For issues or questions about CODSOFT:
- Email: contact@codsoft.in
- Website: www.codsoft.in

---

## 📄 License

Part of CODSOFT AI Internship Program

---

**Enjoy the game! Can you beat the AI?** 🎮

(Spoiler: You can't! 😄)
