def transcribe(dna):
	return dna.replace('T', 'U')
	
def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A': rc.append('T')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		elif nt == 'T': rc.append('A')
		else: rc.append('N')
	return ''.join(rc)
	
def translate(dna):
	aas = [] #initializes an empty list for the aa
	for i in range(0, len(dna), 3): #steps through indices by threes. Val of i contain starting index of each codon
		 codon = dna[i:i+3] # create codon
		 if codon == 'ATG': aas.append('M') #actual translation
		 elif codon == 'TAA': aas.append('*')
		 else: aas.append('X')
	return ''.join(aas)
	
"""
def translate(dna):
	codons = ('ATG', 'TAA')
	aminos = 'M*'
	aas = []
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in codons:
			idx = codons.index(codon)
			aa= aminos[idx]
			aas.append(aa)
		else:
			aas.append('X')
	return ''.join(aas)	
"""
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)
	
def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	if c + g == 0: return 0
	return (g - c) / (g + c)
	
	gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}
def translate(seq):
	pro = []
	for i in range(0, len(seq), 3):
		codon = seq[i:i+3]
		if codon in gcode: aa = gcode[codon]
		else:              aa = 'X'
		pro.append(aa)
	return ''.join(pro)
	
kdh = {
	'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5,
	'M':  1.9, 'A':  1.8, 'G': -0.4, 'T': -0.7, 'S': -0.8,
	'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
	'Q': -3.5, 'D': -3.5, 'K': -3.9, 'N': -3.5, 'R': -4.5,
}
def hydropathy(seq):
	s = 0
	for aa in seq:
		s += kdh[aa]
	return s / len(seq)
	
def kd_cond(seq):
    kd = 0
    for aa in seq:
        if   aa == 'I': kd += 4.5
        elif aa == 'V': kd += 4.2
        elif aa == 'L': kd += 3.8
        elif aa == 'F': kd += 2.8
        elif aa == 'C': kd += 2.5
        elif aa == 'M': kd += 1.9
        elif aa == 'A': kd += 1.8
        elif aa == 'G': kd += -0.4
        elif aa == 'T': kd += -0.7
        elif aa == 'S': kd += -0.8
        elif aa == 'W': kd += -0.9
        elif aa == 'Y': kd += -1.3
        elif aa == 'P': kd += -1.6
        elif aa == 'H': kd += -3.2
        elif aa == 'E': kd += -3.5
        elif aa == 'Q': kd += -3.5
        elif aa == 'D': kd += -3.5
        elif aa == 'N': kd += -3.5
        elif aa == 'K': kd += -3.9
        elif aa == 'R': kd += -4.5
    return kd/len(seq)