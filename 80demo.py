import json

person = {
	'name': 'Ian Korf',
	'age': 57,
	'weight': 163.8,
	'pets': ['Hesper', 'Mouserat', 'Labrat'],
	'mentees': {
		'Claire': 'undergrad',
		'Dell': 'undergrad',
	}
}

people = []
people.append(person)
people[0]['mentees']['Ismael'] = 'grad' #set to new thing
people[0]['pets'].append('Fizzbuzz')
print(json.dumps(person, indent=4))

#print(people[0]['mentees']['Claire'])
"""
{
    "name": "Ian Korf",
    "age": 57,
    "weight": 163.8,
    "pets": [
        "Hesper",
        "Mouserat",
        "Labrat"
    ],
    "mentees": {
        "Claire": "undergrad",
        "Dell": "undergrad"
    }
}
undergrad
"""

import mcb185
import sys
#count kmers in a file
k = int(sys.argv[2])
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for i in range(len(seq) -k + 1):
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] = 1
		else: 
			kcount[kmer] += 1
		
print(json.dumps(kcount,indent=4))
#call: python3 80demo.py ~/code/MCB185/data/C.elegans.fa.gz 2


