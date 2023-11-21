import argparse
from Bio import SeqIO

# Function to extract and concatenate specified genes
def concatenate_genes(genes, genbank_file):
    sequences = {gene: "" for gene in genes} # Initialize a dictionary for the genes
    for record in SeqIO.parse(genbank_file, "genbank"):
        for feature in record.features:
            if feature.type == "gene" and "gene" in feature.qualifiers:
                gene_name = feature.qualifiers["gene"][0]
                if gene_name in genes:
                    sequences[gene_name] = str(feature.extract(record.seq))
    concatenated_seq = "".join([sequences[gene] for gene in genes]) # Concatenate in the specified order
    return concatenated_seq

# Set up argument parser
parser = argparse.ArgumentParser(description='Concatenate specified genes from a GenBank file.')
parser.add_argument('--genes', nargs='+', help='List of gene names to concatenate', required=True)
parser.add_argument('--input', help='Input Genbank file', required=True)

# Parse arguments
args = parser.parse_args()

# Run the function with the provided arguments
concatenated_sequence = concatenate_genes(args.genes, args.input)
print(concatenated_sequence)