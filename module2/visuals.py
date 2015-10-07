import turtle


class MapGUI:
   def __init__(self, ):
      self.cell_size = 20
      self.previous_color = {}
   #end
   
   def initialize_plot(self, positions):
      self.positions = positions
      self.minX = minX = min(x for x,y in positions.values())
      maxX = max(x for x,y in positions.values())
      minY = min(y for x,y in positions.values())
      self.maxY = maxY = max(y for x,y in positions.values())
      
      ts = turtle.getscreen()
      if ts.window_width > ts.window_height:
          max_size = ts.window_height()
      else:
          max_size = ts.window_width()
      self.width, self.height = max_size, max_size
      
      turtle.setworldcoordinates(minX-5,minY-5,maxX+5,maxY+5)
      
      turtle.setup(width=self.width, height=self.height)
      turtle.speed("fastest") # important! turtle is intolerably slow otherwise
      turtle.tracer(False)    # This too: rendering the 'turtle' wastes time
      turtle.hideturtle()
      turtle.penup()
      
      self.colors = ["#d9684c","#3d658e","#b5c810","#ffb160","#bd42b3","#0eab6c","#1228da","#60f2b7" ]

      for color in self.colors:         
         s = turtle.Shape("compound")
         poly1 = ((0,0),(self.cell_size,0),(self.cell_size,-self.cell_size),(0,-self.cell_size))
         s.addcomponent(poly1, color, "#000000")
         turtle.register_shape(color, s)
      
      s = turtle.Shape("compound")
      poly1 = ((0,0),(self.cell_size,0),(self.cell_size,-self.cell_size),(0,-self.cell_size))
      s.addcomponent(poly1, "#000000", "#000000")
      turtle.register_shape("uncolored", s)
   #end
      
   def draw_vertex(self,  domain_name, domain ):
      if len(domain) == 1:
         shape_name = self.colors[ domain[0] ]
      else:
         shape_name = "uncolored"
      
      if shape_name != self.previous_color[domain_name]:
         self.previous_color[domain_name] = shape_name
         position = tuple(map(lambda x: x+0.4, self.positions[domain_name]))
         turtle.shape( shape_name )
         turtle.setposition( position )
         turtle.stamp()
   #end
   
   def draw_line(self, start_node, end_node ):
      start = self.positions[start_node]
      end = self.positions[end_node]
      
      turtle.setposition( start )
      turtle.pendown()
      turtle.setposition( end )
      turtle.penup()
   
   def update(self, ):
      turtle.update()
   #end
   
   def clear(self, ):
      turtle.clear()
   #end
   
   def clearstamps(self, ):
      turtle.clearstamps()
   #end
    
   def plot(self, positions ):
      """
      positions eg. = {'0': (0.0, 5.0),
       '1': (3.0, 3.0),
       '2': (0.0, 25.0),
       '3': (3.0, 23.0),
       '4': (3.0, 27.0),
       '5': (4.0, 25.0),
       '6': (5.0, 24.0),
       '6': (5.0, 26.0)}
      """
      self.previous_color = {domain_name:"init" for domain_name in positions.keys()}
      self.initialize_plot( positions )
      self.update()
   #end
   
   def stop(self, ):
      turtle.clear()
      turtle.bye()
   #end
#end class