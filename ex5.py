def base_count(sequence, base):
    return sequence.count(base)
    
def gc_count(sequence):
    return (base_count(sequence, 'G') + 
            base_count(sequence, 'C')) / float(len(sequence))

sequence = "GATCTAGTGATGCAG"
print base_count(sequence,"G")
print gc_count(sequence)
