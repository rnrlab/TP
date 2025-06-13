#!/bin/bash

cd JuanCarlos/
mkdir ./BLASTp
mkdir ./JuanCarlos/Sequences/UniProt2GenBank
mv Main_Hit_Dataset_updated.tar.gz JuanCarlos/Sequences/UniProt2GenBank
mv ToBlast_ids.txt JuanCarlos/Sequences/UniProt2GenBank
vi JuanCarlos/Sequences/UniProt2GenBank/select_fasta.sh
cd JuanCarlos/Sequences/UniProt2GenBank
chmod +x select_fasta.sh
bash select_fasta.sh
screen -S UniProt2GenBank
ls *.fasta | parallel blastp -query {} -db /mnt/disk2/databases/nr_clustered/nr_cluster_seq -evalue 0.00001 -out ../../BLASTp/{.}.tsv -max_target_seqs 5000 -outfmt 7

cd ../../BLASTp/
tar -czvf BLASTp_results.tar.gz *.tsv