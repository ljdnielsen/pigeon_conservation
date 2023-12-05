#!/usr/bin/env python3

import sys
import os
from Bio import SeqIO

def parse_gbk(genbank_file, output_file):
    '''Reads a GENBANK file and writes the protein sequence of every coding sequence to a FASTA file'''
    with open(genbank_file, 'r') as handle, open(output_file, 'a') as fasta_file:
        for record in SeqIO.parse(handle, 'genbank'):
            # Iterating through each feature
            for feature in record.features:
                if feature.type == 'CDS': # CDS = Coding Sequence
                    # Extract protein id, gene name, product and protein sequence
                    protein_id = feature.qualifiers['protein_id'][0]
                    gene = feature.qualifiers.get('gene', ['n/a'])[0]
                    product = feature.qualifiers.get('product', ['n/a'])[0]
                    protein_seq = feature.qualifiers['translation'][0]

                    # Create a FASTA formatted string
                    fasta_formatted_string = f'>{protein_id}|{gene}|{product}\n{protein_seq}'

                    # Write to the output FASTA file
                    fasta_file.write(fasta_formatted_string + '\n')

def process_directory(input_dir, output_dir):
    '''Process each GenBank file in the input directory and write outputs to the output directory'''
    for filename in os.listdir(input_dir):
        if filename.endswith('.gbk') or filename.endswith('.gb'):
            genbank_file = os.path.join(input_dir, filename)
            basename = os.path.splitext(filename)[0]
            output_file = os.path.join(output_dir, basename + '.fasta')
            parse_gbk(genbank_file, output_file)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 extract_proteins.py input_dir output_dir')
    else:
        input_dir = sys.argv[1]
        output_dir = sys.argv[2]
        process_directory(input_dir, output_dir)
