# Origins of Mitochondrial Genomes

## Overview

This document details the process and findings related to the origins of the biological samples used in our bioinformatic analysis. It includes details on the extraction of source qualifiers from GenBank files of MtDNA samples, observations from the data, and contextual historical information relevant to the samples.

## Extraction of Source Qualifiers from MtDNA GenBank Files
We utilized the script '__extract_qualifers.py__' to extract relevant sample information from each GenBank file. The targeted data included 'organism', 'country', 'collection_date', 'collected_by', and 'specimen_voucher'. The extraction was executed with the following command:

~~~bash
python3 src/preprocessing/extract_qualifiers.py --directory data/raw --annotations organism --qualifiers country collection_date collected_by specimen_voucher > data/metadata/sample_origins.csv
~~~

## Analysis of Extracted Data

Post-extraction, the data was organized in Excel. Key findings include:

- Collection dates were available for 34 Goura specimens (all four species), one Didunculus strigirostris, and one Caloenas nicobarica.
- Geographic origins of the samples, where recorded, were as follows:
    - 22 from Indonesia
    - 18 from Papua New Guinea
    - 1 (Didunculus strigirostris) from Samoa

## Historical Context of the First Goura Specimen

The first Goura specimen (a Goura cristata) was seemingly collected by Charles Martin Allen, assistant to Alfred Russel Wallace, during an 1860 expedition to Misool Island, Indonesia. This prompted a review of the literature, specifically *In Alfred Russel Wallace's Shadow: His Forgotten Assistant, Charles Allen (1839-1892)* by Kees Rookmaaker and John van Wyhe, for further insights.

### Excerpts from Wallace's Correspondences and Notebooks
In their paper, Rookmaaker and van Wyhe cite several entertaining paragraphs about Wallace's and Allen's experiences. Wallace's character assessment of Allen is mentioned in a letter to his mother, from July 1854 when camping in the jungle near Malacca:

>So far both I and Charles have enjoyed excellent health. He can now shoot
pretty well, and is so fond of it that I can hardly get him to do anything else.
He will soon be very useful, if I can cure him of his incorrigible carelessness.
At present I cannot trust him to do the smallest thing without watching that
he does it properly, so that I might generally as well do it myself.

Wallace growing reliance on Allen is exemplified by a paragraph from one of Wallace's notebooks. Here he recalls, when one afternoon at Simunjan, Allen allerted him of an orangutan sighted nearby:

>One afternoon I had just come home from an Entomologizing excursion &
was preparing for a bathe when Charley rushed in, out of breath with
running & excitement & exclaimed by jerks. ‘Get the gun sir—be quick—
such a large mias—oh!’—‘Where’ said I, ‘Close by’—he can’t get away.’ So
the gun was got out & one barrel being ready loaded with ball I started off
calling upon two Dyaks who happened to be in the house at the time to
accompany me & ordering Charles to bring all the ammunition after me as
quick as possible.

The vast contribution that Allen have made to specimen collection is made clear by Rookmaaker's and van Wyhe's recounting that he collected 6198 insects, correspongin to more then a hundred individuals per day, in a two-and-a-half month period between 4 August and 18 October 1855, only a year after arriving in the Malay Archipelago. [^1]


[^1]: Rookmaaker, Kees & van Wyhe, John. (2012), ["In Alfred Russel Wallace's Shadow: His Forgotten Assistant, Charles Allen (1839-1892)"](https://www.jstor.org/stable/24894190) *Journal of the Malaysian Branch of the Royal Asiatic Society*, 2012: vol. 85, Issue 2, pp. 17-54



