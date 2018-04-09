# Define the Surfer Class
class Surfer():

  # Initialize the Surfer constructor 
  def __init__(self, name, hometown, rank):
      self.name = name + " " + "Dude"
      self.hometown = hometown + " " + "Waves"
      self.rank = rank

# Create an instance of the Surfer Class
surfer = Surfer('Kelly Slater', 'Cocoa Beach', 1)

# Print the object's attributes
print(surfer.name)
print(surfer.hometown)
print(surfer.rank)