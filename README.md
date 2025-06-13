# Identification, Annotation and Structural Characterisation of Viral Terminal Proteins

This repository includes the notebooks and data from a preliminary systematic analysis of viral TPs, conducted as part of Juan Carlos Ramírez Montáns' Master's Thesis, supervised by Modesto Redrejo Rodríguez (Department of Biochemistry, @UAM).

####### Under construction ########

## File summary
* Main workflow notebooks and scripts
  |File|Description|
  |----|-----------|
  |01_Predataset_Clustering.ipynb|Predataset FASTA sequence retrieval and dual clustering (BLAST2seq+K-Means+PCA, CD-Hit). Open it in [Google Colab](https://shorturl.at/SAAsr).|
  |02_Surface_Charge_Density_Distribution.ipynb|Surface charge density distribution asymmetry computation, assessment and scrutiny. Open it in [Google Colab](https://shorturl.at/PADr2).|
  |03_Secondary_Structure.ipynb|Secondary structure composition calculation and assessment of its TP-discriminant potential. Open it in [Google Colab](https://shorturl.at/IQVBk).|
  |04_DNABIND_ConfusionMatrix.ipynb|DNABIND DNA-binding classifier evaluation for TP discrimination. Open it in [Google Colab](https://shorturl.at/i8FQd).|
  |05_FoldSeek.ipynb|Structure-based PSI-BLAST (via RESTful API access) homology search, results processing (sieving, prefiltering, sorting and deduplication) and taxonomic information retrieval. Open it in [Google Colab](https://shorturl.at/w8Xab).|
  |06_PSI_BLAST.ipynb|Sequence based PSI-BLAST homology search, results processing (sieving, prefiltering, sorting and deduplication) and taxonomic information retrieval. Open it in [Google Colab](https://colab.research.google.com/drive/1hdBuwXze26UjM3Lqpvv_SAysUYV3bsis?usp=sharing).|
  |07_taxonomizr_Taxonomic_Inspection.ipynb|taxonomizr-based taxonomic scrutiny of candidate homologs' lineages. Open it in [Google Colab](https://colab.research.google.com/drive/19G4GBwjKjcocVtXdY-rg6mVY8Y7l1ha2?usp=sharing).|
  |08_qTMcluster_processing.ipynb|qTMcluster (structure-based clustering of Foldseek-yielded candidate hits) data processing and evaluation of query coverage impact on qTMcluster co-clustering performance. Open it in [Google Colab](https://colab.research.google.com/drive/1ZBg-8iJSjqOcdCfAR6XWufo99jH0GRnc?usp=sharing).|
  |09_Results_Clustering.ipynb|Compound Foldseek and PSI-BLAST results merger and deduplication, FASTA sequences retrieval and sequence-based CD-Hit clustering. Open it in [Google Colab](https://colab.research.google.com/drive/1WlWEH73eG7CCiHVr2MVsQ9uIh3nQE_q9?usp=sharing).|
  |10_Contig_retrieval_inspection.ipynb|Genome/contig retrieval of IPG-yielded representative proteins. Open it in [Google Colab](https://colab.research.google.com/drive/1G9x2JdJ_0Fu13tbj83f9gHTJU0taNWRT?usp=sharing).|
  |11_Genome_Proteome_Annotation.ipynb|Retrieval of GBK-format representative proteomes, FASTA format conversion, PHROG execution and results scrutiny, geNomad execution and scrutiny, PHROG-geNomad cross-reference and virus-free contig shortlisting. Open it in [Google Colab](https://colab.research.google.com/drive/1QnTQOHzhgSB9GrE-mpjJhfc7QYl5F2cJ?usp=sharing).|
  |12_Roll_back.ipynb|Merger of sequential results dataframes into final results whole-width dataset (FULL_results+GenomeID+Tax+Cluster+BLASTp_Synonyms+IPG+Non-Viral+eggNOG+Pol+COG.csv). Open it in [Google Colab](https://colab.research.google.com/drive/1XrB4UGqyLQk9lJTfU98YsYoxRhodOlpO?usp=sharing).|
  |13_Plots_and_Statistics.ipynb|R scripting for plotting. Open it in [Google Colab](https://colab.research.google.com/drive/1HBqQ1hs0sFcXn1Z1G2lpasaBnWhj7y-P?usp=sharing).|
  |PSI-BLAST.sh|Sequence based PSI-BLAST homology search|
  |BLASTp.sh|Sequence based BLASTp homology search for GenBank homologs|
  |def_geNomad4TP_multiFASTA.py|Python script for running geNomad on multi-FASTA file|
  |PHROG4TP_new.py|Necessary Python scripts for running PHROG|
  |PHROG4TP_hmmbuild.py|Necessary Python scripts for running PHROG|
* Results files
## Useful links:
*   András Szilágyi DNABIND classifier (https://dnabind.szialab.org/)
*   Foldseek RESTful API (https://search.foldseek.com/api/)
*   FoldMason (https://search.foldseek.com/foldmason)
*   ClustalΩ (https://www.ebi.ac.uk/jdispatcher/msa/clustalo)


####### Under construction ########
