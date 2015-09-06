USAGE

1. import MapGUI from visuals:

```
from visuals import MapGUI
```

2. Initialize a 2D list representing the window tiles:

```
board = [[0] * width] * height # 0 represents the background color
```

3. Create a new window with the constructor:

```
window = MapGUI( width, height, board )
```

4. Call *update_view* when you whish to update the window:

```
window.update_view( list ) # the list contains your 2D list representation of the window
```

5. Call *destroy* to close the window:

```
window.destroy()
```