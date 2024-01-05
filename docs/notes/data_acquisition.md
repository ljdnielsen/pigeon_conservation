# Data Acquisition

## Overview of Genome Selection Methodology
All NCBI-available mitogenomes of a given species that lived up to our quality criteria were included in the analysis. The genomes were found by running NCBI-BLAST with the RefSeq mitogenome of that species. In cases without a RefSeq genome, the longest available mitogenome was used as the query. We included mitogenomes that had a coverage of at least 99% of the query genome and a length of at least 95.7% of the query genome. The below table shows the query genome used for each species:

<!--Add column indicating if the genome is refseq or not-->
|Species                 |Query genome|
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

During the BLAST searches, we also recorded the percent identity of the least similar genome compared to the reference genome. This data, summarized below, was not used as a selection criteria but was noted for potential future reference.

|Species                 |Percent identity| 
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

## Retrieval of Genome Data from NCBI

To retrieve the mitochondrial genomes, we employed the efetch (v. 20.7) command from Entrez Direct with a list of the chosen genomes. This process involved:

1. **Creating an Input File**: We first prepared a text file ('genome_accessions.txt') listing the NCBI accession numbers of all the genomes we intended to download.
2. **Executing the Command**: We then executed the following command which loops through the accession numbers downloading each genome with efetch to the current directory:
~~~bash
# Loop through each line in the file 'genome_accessions.txt'
while read r; do
    # Fetch the genome from NCBI for each accession number
    # and save it in Genbank format with the accession number as the filename
    efetch -db nucleotide -id $r -format gb > ${r}.gb
done < genome_accessions.txt
~~~

The number of mitogenomes retrieved per species, including the reference genome, is listed in alphabetical order in the table below:

|Species                 |# of mitogenomes  |
|------------------------|------------------|
|Caloenas nicobarica     |2                 |
|Didunculus strigirostris|2                 |
|Ectopistes migratorius  |42                |
|Goura cristata          |11                |
|Goura scheepmakeri      |6                 |
|Goura sclaterii         |7                 |
|Goura victoria          |16                |
|Pezophaps solitaria     |1                 |
|Raphus cucullatus       |1                 |


Return to [README](../../README.md).

