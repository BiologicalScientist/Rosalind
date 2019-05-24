"""
This program is designed to identify the shared motifs in a list of Fasta files.

It takes as an argument the input file which should be multiple sequences in FASTA format.

i.e. in the command line run
>python3 FINDING_A_SHARED_MOTIF.py input_fasta.fa/txt 

"""


import sys
filename = sys.argv[1]

try:
    fasta_file = open(filename, 'r') #open file in read mode
except IOError:
    print ('file does not exist')
    
FASTA_DICT = {} #initialise dictionary object

for line in fasta_file: #iterate through the lines in the fasta file
    line = line.rstrip() #remove the newline character from the end of the line
    
    if line[0] == '>':
        seq_name = line[1:]
        FASTA_DICT[seq_name] = '' # create empty entry in dictionary value 
    elif line[0] != '>':
        sequence = line
        FASTA_DICT[seq_name] = FASTA_DICT[seq_name] + sequence
        
print (FASTA_DICT)

        
fasta_file.close()
        
sequences = [] #initialise sequences list
for m in FASTA_DICT.values(): 
    sequences.append(m) #add all of the sequences from FASTA_dict to the list
    
    
for header in FASTA_DICT.keys(): #take the key from the dictionary FASTA_DICT and store as header variable
    sequence = FASTA_DICT[header] # take the value for the header key in FASTA_DICAT and store sequence variable
    length = len (sequence) #take length of the sequence variable (total sequence length)
    motifs = [] #initialise motifs list
    x = 0
    while x <= length:
        for i in range(length): #iterate over each value of i that is less than the length of the sequence
            if (sequence[i:x]) != '': #if the space between i and x is a value not empty
                motifs.append(sequence[i:x]) #append the motif to the list motifs
        x = x + 1 #increase the final value by 1 until it reache the length

shared_motifs = [] #initialise shared_motifs list
for motif in motifs:
    present = True
    i = 0
    for sequence in sequences:
        if motif not in sequence:
            present == False
            i = i + 1
            break
        elif motif in sequence:
            i = i + 1
            if i == len(sequences):
                if present == True:
                    shared_motifs.append(motif)
                continue
                
print (shared_motifs)

sorted_motifs = sorted(shared_motifs, key=len)
print (sorted_motifs)
print (sorted_motifs[-1])
