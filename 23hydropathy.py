# Write a function that returns the Kyte-Doolittle hydrophobicity value for an amino acid letter. 
#Demonstrate that the function works by calling it multiple times with different letters, one of which should be outside the amino acid alphabet.

def hydropathy(x):
	if x == 'A': return 1.8
	if x == 'C': return 2.5
	if x == 'D': return -3.5
	if x == 'E': return -3.5
	if x == 'F': return -3.5
	if x == 'G': return -0.4
	if x == 'H': return -3.2
	if x == 'I': return 4.5
	if x == 'K': return -3.9	
	if x == 'L': return 3.8
	if x == 'M': return 1.9
	if x == 'N': return -3.5
	if x == 'P': return -1.6
	if x == 'Q': return -3.5
	if x == 'R': return -4.5
	if x == 'S': return -0.8
	if x == 'T': return -0.7
	if x == 'V': return 4.2
	if x == 'W': return -0.9
	if x == 'Y': return -1.3
	else: return "Not in Amino Acid alphabet"
print(hydropathy('A'))
print(hydropathy('F'))
print(hydropathy('Z'))