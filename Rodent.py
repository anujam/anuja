class Rodent:
  def _init_(self, tag_id):
    self.tag_id = tag_id
    self.weights = []
    
  def plot(self):
    return self.tag_id[0]
    
  def add_weight(self, weight):
  ..self.weights.append(weight)
  
Rodent.add_weight(10)  
