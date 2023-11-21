# Data Acquisition

## Overview of Genome Selection Methodology
Before detailing the selection criteria, it's important to outline our initial approach to acquiring mitochondrial genomes. For each species, a BLAST search was conducted using the available RefSeq mitochondrial genome. In cases without a RefSeq genome, the longest available genome was used as the query. After filtering for the species in question our selection critieria were applied to the resulting BLAST hits. The below table shows the query genome used for each species:

|Species                 |Query Genome|
|------------------------|------------|
|Ectopistes migratorius  |NC_042502.1 |
|Goura cristata          |NC_031865.1 |
|Goura scheepmakeri      |NC_027947.1 |
|Goura sclaterii         |MG590288.1  |
|Goura victoria          |NC_036613.1 |
|Caloenas nicobarica     |NC_031869.1 |
|Pezophaps solitaria     |KX902238.1  |
|Raphus cucullatus       |NC_031864.1 |
|Didunculus strigirostris|NC_031866.1 |

## Selection Criteria for Mitochondrial Genomes
We selected the mitochondrial genomes based on the following criteria:

- **BLAST Query Coverage**: Included only genomes with BLAST query coverage of at least 99% to the reference genome.

- **Genome Completeness by Length**: Included genomes whose length was at least 95.7% of the reference genome's length.

## Additional BLAST Search Information

During the BLAST searches, we also recorded the percent identities of each genome compared to the reference genome. This data, summarized below, was not used as a selection criteria but was noted for potential future analysis.

|Species                 |Percent Identity| 
|------------------------|----------------|
|Ectopistes migratorius  |99.7%           |
|Goura cristata          |99.7%           |
|Goura scheepmakeri      |99.8%           |
|Goura sclaterii         |99.7%           |
|Goura victoria          |99.7%           |
|Caloenas nicobarica     |99.5%           |
|Pezophaps solitaria     |N/A             |
|Raphus cucullatus       |N/A             |
|Didunculus strigirostris|99.9%           |

For each species, we also noted the length of the shortest mitochondrial genome that lived up to our selection criteria:

## Retrieval of Genome Data from NCBI

To retrieve the mitochondrial genomes, we employed the efetch (v. 20.7) command from Entrez Direct. This process involved:

1. **Creating an Input File**: A text file ('genome_accessions.txt') was prepared, listing the NCBI accession numbers for the targeted genomes.
2. **Executing the Command**: The following command was run, which loops through the accession numbers to download the specified genomes with efetch:
~~~bash
# Loop through each line in the file 'genome_accessions.txt'
while read r; do
    # Fetch the genome from NCBI for each accession number
    # and save it in Genbank format with the accession number as the filename
    efetch -db nucleotide -id $r -format gb > ${r}.gb
done < genome_accessions.txt
~~~


