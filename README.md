

# connect-four
Connect four with integrated match engine and post-review of game

## Connect Four with Post-Game Analysis
A Connect Four game built in Python with an AI opponent and a post-game review engine inspired by chess analysis tools like Stockfish.
## What it does
Play Connect Four against an AI opponent, then get a move-by-move breakdown of your game. The engine evaluates every position you played and flags where you went wrong, classifying each move as good, inaccurate, a mistake, or a blunder based on how much it shifted the position's score.
## How the engine works
The AI uses minimax search with alpha-beta pruning to evaluate positions. Connect Four has at most 7 legal moves per turn, which makes deep searches feasible even on a laptop. The evaluation function scores positions by counting and weighting threats (three-in-a-row with an open fourth slot), factoring in how accessible the winning slot actually is.
Since Connect Four is a solved game (first player wins with perfect play), the engine can often determine the objective outcome of a position, not just estimate it.
## Post-game review
After a game ends, the engine replays every board state and compares your move to its best move. Moves where the score difference exceeds a threshold get flagged:

Good move: close to or matching the engine's top choice
Inaccuracy: slightly suboptimal, minor score loss
Mistake: a meaningfully worse move that shifts the evaluation
Blunder: a move that flips the position from winning to losing (or equal to losing)

Early moves rarely trigger flags since most openings are roughly equal. The interesting analysis happens in the midgame and endgame where single moves can decide the game.

## Built with

* Python
* Minimax with alpha-beta pruning
