#!/bin/bash

scp -rpC TP_Predataset sie@150.244.72.25:/home/sie/JuanCarlos
mkdir ./PSI-BLAST/
cd /home/sie/JuanCarlos/Sequences/
ls *.fasta | parallel psiblast -query {} -db /mnt/disk2/databases/nr_clustered/nr_cluster_seq -evalue 0.001 -num_iterations 3 -outfmt 7 -out ../PSI-BLAST/{.}.tsv