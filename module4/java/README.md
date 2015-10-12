# 2048 written by [@freva](https://github.com/freva)

> This board support all tile values

# Usage


Displaying a board:

```Java
public static void main(String args[]) throws InterruptedException {
    GUI gui = GUI.getWindow();
    int[] board = {0, 2, 4, 4, 0, 2, 1, 3, 0, 1, 1, 3, 0, 0, 2, 1};
    gui.drawBoard(board);
}
```

Update the view by calling *drawBoard*:

```Java
int[] board = {   
            # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display, 
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 2, 4, 4, 
            0, 2, 1, 3, 
            0, 1, 1, 3, 
            0, 0, 2, 1
        }

gui.drawBoard(board) // 1D list representing the board
```

## Screen dump
<img src="https://raw.githubusercontent.com/jorgenkg/IT3105/master/module4/gui_screendump.png" width="250px" />

# Kudos
This code has been written by [@freva](https://github.com/freva) in its entirety.
