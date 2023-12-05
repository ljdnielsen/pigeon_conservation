# Load necessary packages
library(adegenet)
library(ape)
library(pegas)

# Load Goura Cytochrome B Alignment
cytb <- fasta2DNAbin("/home/laniel/projects/pigeon_conservation/data/processed/genera/Goura/renamed_fasta/cytb_cristata.aligned.fasta")

h <- haplotype(cytb)

haplo_index <- attr(h, "index")
