# 2048

> This board supports tiles up to 65536

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
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 2, 4, 4,
            0, 2, 1, 3,
            0, 1, 1, 3,
            0, 0, 2, 1
        ]

window.update_view( board ) # 1D list representing the board
```

## Screen dump
<img src="https://raw.githubusercontent.com/jorgenkg/IT3105/master/module4/gui_screendump.png" width="250px" />
