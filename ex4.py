file = open("uniprot_sprot.fasta")
while True:
  line = file.readline()
#  print line
  if not line:
      break

