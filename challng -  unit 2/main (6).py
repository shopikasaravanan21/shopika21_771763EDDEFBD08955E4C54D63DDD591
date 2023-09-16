# defline the base class player
class player:
  def play(self):
    print("the player is playing cricket.")
# defline the derivd class batsman
class batsman(player):
  def play(self):
    print("the batsman is batting.")
#defline the derived class bowler
class bowler(player):
  def play(self):
    print("the bowler is bowling.")
# creat objects of batsman and bowler classes
batsman = batsman()
bowler = bowler()
#call the play() method for each object
batsman.play()
bowler.play()