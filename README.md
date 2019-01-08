# FROC-MSS: Old French and Old Occitan Medieval Manuscripts HTR Data and Models

This repository contains:

- training and evaluation data from allographetic transcriptions of various
Old French and Old Occitan manuscripts, in various states of correctness, in Kraken
training format;
- HTR models trained and tested using this data.

If you plan of using this data or the provided model for a publication, please
cite it, as:

Jean-Baptiste Camps (éd.), _FROC-MSS: Old French and Old Occitan Medieval Manuscripts HTR Data and Models_, Paris: École nationale des chartes (PSL), 2018, [https://github.com/Jean-Baptiste-Camps/FROC-MSS](https://github.com/Jean-Baptiste-Camps/FROC-MSS).

## Data format

The data is as following:
- each line image in a `.png` file;
- each transcription in a `.gt.txt` file.

Unicode NFD normalisation has been applied on the ground-truth text.

## Models

### Summary and C.E.R.

The root folder contains a vanilla Kraken model (`model_froc.mlmodel`), 
trained with default settings and without any additional data (e.g. no artificial noised data).

Data was randomly divided in 80\% for training (`train.txt`), 10\% for in-training 
validation (`val.txt`) and 10\% for final testing of the model (`test.txt`).

It achieved a C.E.R. of:

- ** 8.11 % ** on validation data (7.03% ignoring spaces);
- ** 7.83 % ** on test data (6.92% ignoring spaces).

### Errors and most frequent confusions on test data

There were 13540 characters and 1061 errors on test data.

Globally, the error are as follow: 

- 536 characters from the ground truth were not predicted by the model;
- 132 characters absent from the ground truth were wrongly predicted;
- 393 character substitutions.


The most frequent confusions concerned spacing.

The 20 most frequent confusions are:

    Errors	Ground Truth-Prediction
    70	{ SPACE } - {  }
    54	{  } - { SPACE }
    48	{ ı } - {  }
    43	{ n } - {  }
    43	{ COMBINING ACUTE ACCENT } - {  }
    27	{ e } - {  }
    24	{ l } - {  }
    24	{ u } - {  }
    21	{ . } - {  }
    20	{ u } - { n }
    18	{ ſ } - {  }
    18	{ a } - {  }
    17	{ r } - {  }
    14	{ t } - {  }
    13	{ COMBINING TILDE } - {  }
    13	{  } - { ı }
    12	{ o } - { e }
    12	{ o } - {  }
    12	{ ı } - { m }
    11	{ e } - { c }


## List of manuscripts

The data comes from partial allographetic transcription of the following mss:

- Clermont-Ferrand, archives départementales, 1F2 (XIII 1/3, anglo-norman _praegothica_ script; _Chanson d'Aspremont_); 52 lines.
- Paris, Bibliothèque nationale de France, fr. 854 (XIII 4/4, Venice or Venetian area; gothic _textualis_;  occitan chansonnier _I_); 1112 lines.
- Cologny-Genève, fondation Martin-Bodmer, cod. Bodm. 168 (XIII 3/3, anglo-norman gothic _textualis_; _Chanson d'Otinel_); 1908 lines.
- Oxford, Bodleian Library, Digby 23 (XII 1/2, anglo-norman _praegothica_; _Chanson de Roland_); 564 lines.

For these transcriptions, see: Jean-Baptiste Camps, _La `Chanson d’Otinel’: édition complète du corpus manuscrit et prolégomènes à l’édition critique_, PhD thesis, dir. Dominique Boutet, Paris-Sorbonne, 2016,  DOI: [https://doi.org/10.5281/zenodo.1116735](10.5281/zenodo.1116735).

<!-- TODO: à compléter avec les autres manuscrits: Vatican, Mende, …  -->

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Cette œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Licence Creative Commons Attribution 4.0 International</a>.

## Contribute

If you want to contribute training data or models, you can do so by cloning the
repository and sending us a pull request, or by sending an email 
at _jbcamps at hotmail.com_ .

## Cite this repository

Jean-Baptiste Camps (éd.), _FROC-MSS: Old French and Old Occitan Medieval Manuscripts HTR Data and Models_, Paris: École nationale des chartes (PSL), 2018, [https://github.com/Jean-Baptiste-Camps/FROC-MSS](https://github.com/Jean-Baptiste-Camps/FROC-MSS).

