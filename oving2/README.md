# Usage

Import MapGUI from visuals:

```Python
from visuals import MapGUI
```

Load the position information about the nodes from the input file and represent it as a dictionary with *variable names* as the key and *coordinates* as the dictionary value:

```Python

positions = {
        # variable_name : (x_coordinate, y_coordinate)
        '0': (0.0, 5.0),
        '1': (3.0, 3.0),
        '2': (0.0, 25.0),
        '3': (3.0, 23.0),
        '4': (3.0, 27.0),
        '5': (4.0, 25.0),
        '6': (5.0, 24.0),
   }
```

Create a new window with the constructor, eg.:

```Python
window = MapGUI( )
```

Initialize the view by drawing the first state:

```Python
window.plot( positions ) # the dictionary initialized above
for rule in rules:
    # Loop over the specified rules to determine which nodes are connected with a line.
    # In this assignment, it should be two variables involved in each atomic rule.
    # @params variable_names should be represented as a string with respect to how 
    # the `positions` dictionary was initialized.
    first_variable_name = rule.variable1
    second_variable_name = rule.variable2
    
    plotter.draw_line( first_variable_name, second_variable_name )
```

Update the view during the search:

```Python
for domain_name, domain_variables in current_state:
    # Loop through the domains and update the graphics using a call to *draw_vertex*.
    # @param domain_name is a string according to how the `positions` dictionary was formatted
    # @param domain is a list of currently valid domain values eg: [0, 1, 2]
    window.draw_vertex( domain_name, domain )
window.update()
```

Call *stop* to close the window:

```Python
window.stop()
```
