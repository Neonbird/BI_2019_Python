class Nucleotide_seq():
    def __init__(self, sequence):
        self.seq = sequence
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.seq):
            curr_el = self.seq[self.counter]
            self.counter += 1
            return curr_el
        else:
            raise StopIteration

    def __eq__(self, other_seq):
        if isinstance(other_seq, Nucleotide_seq):
            return self.seq == other_seq.seq
        return NotImplemented

    def __hash__(self):
        return(hash(self.seq))

    def __str__(self):
        return self.seq

    def __repr__(self):
        return self.seq

    def gc_content(self):
        gc_count = self.seq.count('G') + self.seq.count('C')
        return str(gc_count*100/len(self.seq))+'%'


class Dna(Nucleotide_seq):
    def reverse_complement(self):
        reverse_seq = ""
        for nucl in self.seq:
            if nucl == 'A':
                reverse_seq += 'T'
            elif nucl == "T":
                reverse_seq += "A"
            elif nucl == 'C':
                reverse_seq += 'G'
            else:
                reverse_seq += 'C'
        return reverse_seq[::-1]


class Rna(Nucleotide_seq):
    def reverse_complement(self):
        reverse_seq = ""
        for nucl in self.seq:
            if nucl == 'A':
                reverse_seq += 'U'
            elif nucl == "U":
                reverse_seq += "A"
            elif nucl == 'C':
                reverse_seq += 'G'
            else:
                reverse_seq += 'C'
        return reverse_seq[::-1]


a = Dna('AATA')
b = Rna('ACCA')
c = Rna('ACCA')

# print(set([a,b,c]))
# for i in b:
#    print(i)
# print(a == b)
# print(a.gc_content())
# print(b.reverse_complement())