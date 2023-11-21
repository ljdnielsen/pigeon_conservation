import csv
import sys
from Bio import SeqIO

def read_mapping_table(filename, headers):
    """Reads the mapping table and returns a dictionary with keys from the first column and new names as values."""
    mapping = {}
    with open(filename, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            key = row[next(iter(row))] # Get the first column value as key
            new_name_parts = [row[header].replace(' ', '_') for header in headers]
            mapping[key] = '|'.join(new_name_parts)
    return mapping

def main(mapping_table, fasta_file, *headers):
    # Read mapping table
    name_mapping = read_mapping_table(mapping_table, headers)

    # Parse the FASTA file and replace names
    for record in SeqIO.parse(fasta_file, 'fasta'):
        record.id = name_mapping.get(record.id, record.id) # Replace name if in table
        record.description = '' # Clear the description field
        SeqIO.write(record, sys.stdout, 'fasta')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python3 rename_fasta.py mapping_table.csv input.fasta header1 header2 ...')
    else:
        main(sys.argv[1], sys.argv[2], *sys.argv[3:])
