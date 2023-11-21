import argparse
import os
from Bio import SeqIO

# Function for extracting annotations and qualifiers to csv file
def extract(directory, annotations, qualifiers):
    # Print the header
    headers = ['Accession'] + annotations + qualifiers
    print(';'.join(header.upper() for header in headers))
    
    # Process each GenBank file
    for filename in os.listdir(directory):
        if filename.endswith('.gbk') or filename.endswith('.gb'): # Check for GenBank files
            file_path = os.path.join(directory, filename)
            for record in SeqIO.parse(file_path, 'genbank'):
                data_row = [record.id]

                # Extract annotations
                for annotation in annotations:
                    data_row.append(record.annotations.get(annotation, 'n/a'))

                # Extract qualifiers
                for qualifier in qualifiers:
                    value = 'n/a'
                    for feature in record.features:
                        if feature.type == 'source':
                            value = feature.qualifiers.get(qualifier, ['n/a'])[0]
                            break
                    data_row.append(value)
                
                # Print the row
                print(';'.join(str(item) for item in data_row))


# Set up argument Parser
parser = argparse.ArgumentParser(description='Extract annotations or qualifiers from GenBank files in specified folder')
parser.add_argument('--directory', help='input directory with GenBank files')
parser.add_argument('--annotations', nargs='+', help='list of annotations to extract')
parser.add_argument('--qualifiers', nargs='+', help='list of qualifiers to extract')

# Parse arguments
args = parser.parse_args()

# Run the function with the provided arguments
extract(args.directory, args.annotations, args.qualifiers)