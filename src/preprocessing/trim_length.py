import argparse
import os
from Bio import SeqIO

def trim_fasta_sequences(input_file, output_file):
    # Read sequences
    sequences = list(SeqIO.parse(input_file, "fasta"))

    # Find the length of the shortest sequence
    min_length = min(len(seq.seq) for seq in sequences)

    # Trim sequences
    trimmed_sequences = [seq[:min_length] for seq in sequences]

    # Write trimmed sequences to a new_file
    with open(output_file, "w") as output_handle:
        SeqIO.write(trimmed_sequences, output_handle, "fasta")

# Set up argument parser
parser = argparse.ArgumentParser(description='Trim sequences of FASTA file to the length of the shortets')
parser.add_argument('--input', help='input FASTA file')
parser.add_argument('--output', help='output FASTA file')

# Parse arguments
args = parser.parse_args()

trim_fasta_sequences(args.input, args.output)