# Reversi game simulator
## With MinMax algorithm and Alpha-Beta Pruning

## Usage


```console 
> python main.py
```

By default depth of minmax and alpha-beta pruning are set to 3. You can change it by set env variable `DEPTH` to desire depth.
After start two computer players will play game, BLACK player starts. 
 - Alpha-beta pruning driven player WHITE.
 - MinMax driven player BLACK. 

## Heuristics

### Coin parity heuristic
```
Coin Parity Heuristic Value = 100* (Max Player Coins –Min Player Coins) / (Max Player Coins + Min Player Coins)
```

### Mobility heuristic
```
if((Max Player Actual Mobility Value + Min Player Actual Mobility Value) != 0)
    Actual Mobility Heuristic Value = 100* (Max Player Actual Mobility Value –Min Player Actual Mobility Value)/ (Max Player Actual Mobility Value + Min Player Actual Mobility Value)
else
    Actual Mobility Heuristic Value = 0
```

### Static Weights Heuristic Function

|  4 | -3 |  2 |  2 |  2 |  2 | -3 |  4 |
|--- |--- |--- |--- |--- |--- |--- |--- |
| -3 | -4 | -1 | -1 | -1 | -1 | -4 | -3 |
|  2 | -1 |  1 |  0 |  0 |  1 | -1 |  2 |
|  2 | -1 |  0 |  1 |  1 |  0 | -1 |  2 |
|  2 | -1 |  0 |  1 |  1 |  0 | -1 |  2 |
|  2 | -1 |  1 |  0 |  0 |  1 | -1 |  2 |
| -3 | -4 | -1 | -1 | -1 | -1 | -4 | -3 |
|  4 | -3 |  2 |  2 |  2 |  2 | -3 |  4 |

#### All heuristics from paper:
https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
