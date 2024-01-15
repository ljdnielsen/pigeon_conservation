# Origins of Mitochondrial Genomes

## Overview

This document details the process and findings related to the origins of the biological samples used in our bioinformatic analysis. It includes details on the extraction of source qualifiers from GenBank files of MtDNA samples, observations from the data, and contextual historical information relevant to the samples.

## Extraction of Source Qualifiers from MtDNA GenBank Files
We utilized the script ['extract_qualifers.py'](../../src/preprocessing/extract_qualifiers.py) to extract relevant sample information from each GenBank file. The targeted data included 'organism', 'country', 'collection_date', 'collected_by', and 'specimen_voucher'. The extraction was executed with the following command and saved to ['sample_origins.csv'](../../data/metadata/sample_origins.csv):

~~~bash
python3 src/preprocessing/extract_qualifiers.py --directory data/raw --annotations organism --qualifiers country collection_date collected_by specimen_voucher > data/metadata/sample_origins.csv
~~~

## Scope of Extracted Metadata

Post-extraction, the data was organized in Excel. Key findings include:

- Collection dates were available for 34 Goura specimens (all four species), one Didunculus strigirostris, and one Caloenas nicobarica.
- Geographic origins of the samples, where recorded, were as follows:
    - 22 from Indonesia
    - 18 from Papua New Guinea
    - 1 (Didunculus strigirostris) from Samoa

## Sampling Location & Dates by Species

### Sample Locations of Species Through Time

To visualize the geographical and temporal extent of the collected specimen we plotted them according to collection date and species. This was done with the jupyter notebook [metadata_plot.ipynb](../../src/analysis/metadata_plot.ipynb).
This resulted in the following plot:

![Specimen Collections Over Years by Location](../../results/figures/specimen_by_year_location.png)

<!--Is the Goura cristata minor genetically a cristata and where is Salawatt?-->
The four Goura locations were marked on a map of New Guinea and Raja Ampat, shown below, with the jupyter notebook [new_guinea_raja_ampat.ipynb](../../src/analysis/new_guinea_raja_ampat.ipynb):

![Sampling Locations on & Around New Guinea](../../results/figures/new_guinea_raja_ampat.png)

### Interpretation of Geographical Distribution Pattern

The distinct geographical distributions of the four Goura species as described by [^1], is also reflected here showing a distribution of *Goura sclaterii* confined to mainland New Guinea; *Goura cristata* distributed in the Indonesian side of New Guinea and on the Raja Ampat Islands; *Goura scheepmakeri* confined to the Papua New Guinean side of New Guinea; and *Goura victoria* distributed across both halfs of mainland New Guinea and the Geelvink Bay Islands.

In our study, the most recent mitochondrial genome sequences for Goura species in three out of their four locations were from specimens collected several decades ago: Papua New Guinea (1966), the Raja Ampat Islands (1925), and the Geelvink Bay Islands (1896). These dates represent the latest point at which our genetic analysis can be applied to Goura populations in these areas. However, records from the Global Biodiversity Information Facility (GBIF) suggest ongoing presence of these species beyond these dates: a *Goura victoria* was observed on the Geelvink Bay Islands in 1994 ([GBIF: *Goura victoria*](https://www.gbif.org/occurrence/2843598506)), and many *Goura cristata* sightings occured on the Raja Ampat Islands in 2023 ([GBIF: *Goura cristata*](https://www.gbif.org/occurrence/4130233618)). This indicates the potential for acquiring more recent DNA samples, which could significantly enhance our understanding of their current genetic structure and diversity.  

### Detailed Sampling Locations of *Goura cristata* in Western New Guinea and Raja Ampat

To more clearly visualize the geographical distribution of *Goura cristata* we plottet the particular sampling locations as shown on the map below of western New Guinea and the Raja Ampat Islands made using the notebook [g_cristata_sampling_sites.ipynb](../../src/analysis/g_cristata_sampling_sites.ipynb).

![Raja Ampat and Birdshead Peninsula, G. cristata Sites](../../results/figures/g_cristata_sampling_sites.png)

## Historical Context of the First Goura Specimen

The first Goura specimen - a *Goura cristata* - was, as specified in the GenBank file of the MtDNA genome, collected by Charles Martin Allen, assistant to Alfred Russel Wallace, during an 1860 expedition to Misool Island, Indonesia. This prompted a review of the literature, specifically *In Alfred Russel Wallace's Shadow: His Forgotten Assistant, Charles Allen (1839-1892)* by Kees Rookmaaker and John van Wyhe, for further insights.

### Excerpts from Wallace's Correspondences and Notebooks
In their paper, Rookmaaker and van Wyhe cite several colorful descriptions from Wallace's letters and notebooks of his and Allen's experiences. Wallace's initial character assessment of Allen, who was brought along as field assistant at only 16 years of age, is mentioned in a letter to Wallace's mother, from July 1854 when camping in the jungle near Malacca, Malaysia:

>So far both I and Charles have enjoyed excellent health. He can now shoot
pretty well, and is so fond of it that I can hardly get him to do anything else.
He will soon be very useful, if I can cure him of his incorrigible carelessness.
At present I cannot trust him to do the smallest thing without watching that
he does it properly, so that I might generally as well do it myself.

Wallace growing reliance on Allen (Charley or Charles) is exemplified by a paragraph from one of Wallace's notebooks. Here he recalls, when one afternoon at Simunjan, Borneo Allen allerted him of an orangutan (a mias) sighted nearby:

>One afternoon I had just come home from an Entomologizing excursion &
was preparing for a bathe when Charley rushed in, out of breath with
running & excitement & exclaimed by jerks. ‘Get the gun sir—be quick—
such a large mias—oh!’—‘Where’ said I, ‘Close by’—he can’t get away.’ So
the gun was got out & one barrel being ready loaded with ball I started off
calling upon two Dyaks who happened to be in the house at the time to
accompany me & ordering Charles to bring all the ammunition after me as
quick as possible.

The vast contribution that Allen made to specimen collection is made clear by Rookmaaker's and van Wyhe's recounting that he in a two-and-a-half month period between 4 August and 18 October 1855 collected 6198 insects<!--TODO: Add information about the rate at which Allen collected birds-->, corresponding to more than a hundred individuals per day, only a year after arriving in the Malay Archipelago.[^2]

Return to [README](../../README.md).

[^1]: Bruxaux, Jade et al. (2018), ["Recovering the evolutionary history of crowned pigeons (Columbidae: Goura): Implications for the biogeography and conservation of New Guinean lowland birds"](https://www.sciencedirect.com/science/article/abs/pii/S1055790317308679) *Molecular Phylogenetics and Evolution*, 2018: vol. 120, pp. 248-258.

[^2]: Rookmaaker, Kees & van Wyhe, John. (2012), ["In Alfred Russel Wallace's Shadow: His Forgotten Assistant, Charles Allen (1839-1892)"](https://www.jstor.org/stable/24894190) *Journal of the Malaysian Branch of the Royal Asiatic Society*, 2012: vol. 85, Issue 2, pp. 17-54




