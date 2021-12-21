import os
import sys
import msvcrt

class TermiComic:
  def __init__(self):
    self.scene_count=0
    self.scenes=[]
    self.current_scene=0

  def clear(self):
    if os.name == "nt":
      os.system("cls")
    else:
      os.system("clear")

  def add(self, scene):
    self.scene_count+=1
    self.scenes.append(scene)





  def start(self):
    for i in range(self.scene_count):
      self.clear()
      print(self.scenes[i])
      while True:
        if msvcrt.kbhit():
          k=msvcrt.getch().decode('ascii')
          if k == "n":
            if self.current_scene == len(self.scenes):
              pass
            else:
              self.clear()
              self.current_scene+=1
              print(self.scenes[self.current_scene])                
          if k == "b":
            if self.current_scene == len(self.scenes):
              pass
            else:
              self.clear()
              self.current_scene-=1
              print(self.scenes[self.current_scene])

              