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

The root folder contains a vanilla Kraken model (`model_45807.mlmodel`), 
trained with default settings and without any additional data (e.g. no artificial noised data).

It achieved a C.E.R. of:

- ** 8.1 % ** on validation data (randomly chosen 10% of available data that were not used for training);
- ** 6.53 % ** globally.

### Most frequent confusions

Here are the 12 most frequent confusions:

    Errors	Correct-Generated
    2459	{ 0xa } - {  }
    755	{ SPACE } - {  }
    334	{ ı } - {  }
    248	{ e } - {  }
    219	{ COMBINING ACUTE ACCENT } - {  }
    202	{ n } - {  }
    197	{  } - { SPACE }
    183	{ COMBINING TILDE } - {  }
    166	{ l } - {  }
    162	{ u } - {  }
    159	{ . } - {  }
    155	{ r } - {  }

## List of manuscripts

The data comes from partial allographetic transcription of the following mss.:

- Clermont-Ferrand, archives départementales, 1F2 (XIII 1/3, anglo-norman _praegothica_ script; _Chanson d'Aspremont_); 52 lines.
- Paris, Bibliothèque nationale de France, fr. 854 (XIII 4/4, Venice or Venetian area; gothic _textualis_;  occitan chansonnier _I_); 1112 lines.
- Cologny-Genève, fondation Martin-Bodmer, cod. Bodm. 168 (XIII 3/3, anglo-norman gothic _textualis_; _Chanson d'Otinel_); 1908 lines.
- Oxford, Bodleian Library, Digby 23 (XII 1/2, anglo-norman _praegothica_; _Chanson de Roland_); 564 lines.

For these transcriptions, see: Jean-Baptiste Camps, _La `Chanson d’Otinel’: édition complète du corpus manuscrit et prolégomènes à l’édition critique_, PhD thesis, dir. Dominique Boutet, Paris-Sorbonne, 2016,  DOI: [https://doi.org/10.5281/zenodo.1116735](10.5281/zenodo.1116735).

<!-- TODO: à compléter avec les autres manuscrits: Vatican, Mende, …  -->

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Licence Creative Commons" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Ce(tte) œuvre est mise à disposition selon les termes de la <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Licence Creative Commons Attribution 4.0 International</a>.

## Contribute

If you want to contribute training data or models, you can do so by cloning the
repository and sending us a pull request, or by sending an email 
at _jbcamps at hotmail.com_ .

## Cite this repository

Jean-Baptiste Camps (éd.), _FROC-MSS: Old French and Old Occitan Medieval Manuscripts HTR Data and Models_, Paris: École nationale des chartes (PSL), 2018, [https://github.com/Jean-Baptiste-Camps/FROC-MSS](https://github.com/Jean-Baptiste-Camps/FROC-MSS).

