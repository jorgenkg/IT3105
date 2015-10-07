# Usage

Import GameWindow from visuals:

```Python
from visuals import GameWindow
```

Create a new window and initialize the view with the constructor:

```Python
window = GameWindow( )
```

Update the view by calling *update_view*:

```Python
board = [   # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display, 
            # 2^4 = 16, the digit 16.
            2, 1, 0, 0,
            1, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0
        ]

window.update_view( board ) # 1D list representing the board
```