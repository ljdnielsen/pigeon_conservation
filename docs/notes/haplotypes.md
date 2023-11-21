# Tracing Goura Haplotypes Through Time

## Median-Joining Network of Goura Cytochrome B

1. **Extraction of cytochrome b DNA sequences:**
    Cytochrome b DNA sequences were written to the FASTA file '__cytochrome_b.fasta__' with the python executable '__concatenate_genes.py__' using the terms 'CYTB' and 'cob' for input genes as the gene is annotated by either name in the genbank files:
    ~~~bash
    output_file="data/raw/genera/Goura/genes/cytb.fasta"
    > $output_file

    for file in data/raw/*.gb; do
        echo ">$(basename ${file%.gb})" >> $output_file
        python3 src/preprocessing/concatenate_genes.py --genes CYTB cob --input $file >> data/raw/genes_all/cytb.fasta
    done 
    ~~~

    The resulting FASTA file was manually assesed, and it was confirmed that each entry corresponded to the intended gene. 
    
2. **Trimming of sequence ends:**
    The sequences varied in length by 2 terminal bp, and were trimmed from the terminal end down to the length of the shortest sequence in the FASTA file with the script '__trim_length.py__' using the following command:

    ~~~bash
    python3 src/preprocessing/trim_length.py --input data/raw/genera/Goura/genes/cytb.fasta --output data/processed/genera/Goura/trimmed_fasta/cytb.fasta
    ~~~

3. **Renaming the CYTB sequences to reflect sample origin:**
    To enhance the interpretability of our data, the sequences in '__cytb.fasta__' were systematically renamed. This renaming process labels each sequence with details about the specimen collection year, species, geographical origin, and the collector. This procedure is crucial for downstream analyses where such contextual information is needed.
    
    **Procedure:**
    1. **Prepare the mapping table:** Ensure that the '__sample_origins.csv__' file is formatted correctly, with the key (typically the accession number) in the first column.
    2. **Run the renaming script:** Use the '__rename_fasta.py__' script to update the sequence names. The script takes inputs specifying the paths to the mapping table and input FASTA, and the headers of the columns to be used for the new names. The output was passed to a new file, '__data/processed/genera/Goura/renamed_fasta/cytb.fasta__'.

    **Command:**

    ~~~bash
    python3 src/preprocessing/rename_fasta.py data/metadata/sample_origins.csv data/processed/genera/Goura/trimmed_fasta/cytb.fasta COLLECTION_DATE ORGANISM COUNTRY COLLECTED_BY > data/processed/genera/Goura/renamed_fasta/cytb.fasta
    ~~~

4. **Maximum parsimony phylogram of relabeled Cytochrome B sequences:**
    - **Sequence alignment using MAFFT:**
    The CYTB sequences were aligned with MAFFT by executing the following command:

    ~~~bash
    mafft --auto data/processed/genera/Goura/renamed_fasta/cytb.fasta > data/processed/genera/Goura/cytb.aligned.fasta
    ~~~

