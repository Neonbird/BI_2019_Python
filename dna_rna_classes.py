class NucleotideSeq:
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
        if isinstance(other_seq, NucleotideSeq):
            return self.seq == other_seq.seq
        return NotImplemented

    def __hash__(self):
        return hash(self.seq)

    def __str__(self):
        return self.seq

    def __repr__(self):
        return self.seq

    def gc_content(self):
        gc_count = self.seq.count('G') + self.seq.count('C')
        return str(gc_count*100/len(self.seq))+'%'


class Rna(NucleotideSeq):
    def reverse_complement(self):
        reverse_dict = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
        reverse_seq = ""
        for nucl in self.seq:
            reverse_seq += reverse_dict[nucl]
        return reverse_seq[::-1]


class Dna(NucleotideSeq):
    def reverse_complement(self):
        reverse_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        reverse_seq = ""
        for nucl in self.seq:
            reverse_seq += reverse_dict[nucl]
        return reverse_seq[::-1]
