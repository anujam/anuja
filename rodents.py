class Rodent:
  def _init_(self, tag_id):
    self.tag_id = tag_id
    self.weights = []
    
  def plot(self):
    return self.tag_id[0]
    
  def add_weight(self, weight):
    self.weights.append(weight)
  
#x = Rodent("abc")
rodents = {}
file = open("rodents.dat")
while True:
  line = file.readline()
  my_dic = {}
  x= Rodent("abc")
  
  print line
  if not line:
      break  
