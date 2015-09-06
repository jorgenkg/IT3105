# Usage

Import MapGUI from visuals:

```Python
from visuals import MapGUI
```

Initialize a 2D list representing the window tiles:

```Python
board = [[0] * width] * height # 0 represents the background color
```

Create a new window with the constructor, eg.:

```Python
width = 3
height = 3
board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
window = MapGUI( width, height, board )
```

Call *update_view* when you whish to update the window:

```Python
window.update_view( list ) # the list contains your 2D list representation of the window
```

Call *destroy* to close the window:

```Python
window.destroy()
```

## Screen dump
<img src="https://raw.githubusercontent.com/jorgenkg/IT3105/master/oving1/gui_screendump.png" width="250px" />
