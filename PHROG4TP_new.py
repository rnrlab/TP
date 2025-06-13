import subprocess
import os

fastas = [f for f in os.listdir() if f.endswith(".fasta")]
for fasta in fastas:
  try:
    subprocess.run(f"hmmsearch -E 1E-3 --cpu 30 --domtblout {fasta.split('.')[0]}.domtblout /mnt/disk2/wGRR_pipolins-MGEs_victor/MGE_pipolin_clustering_filtering/Gene_annotation/PHROG/PHROGS_func.hmm ./{fasta}", shell=True)
    phrog_results = "GeneID\tPHROG_hit\tE-value\tScore\tCoverage\tPosition\n"
    with open(f"{fasta.split('.')[0]}.domtblout", "r") as f:
      for line in f:
        if line[0] != "#":
          cds_id = line.split()[0]
          tlen = line.split()[2]
          phrog_name = line.split()[3]
          E_val = eval(line.split()[6])
          score = eval(line.split()[7])
          qcov = (eval(line.split()[18])-eval(line.split()[17]))/eval(tlen)
          position = line.split()[-5]
          if qcov >= 0.5 and E_val <= 0.01: # Filtering at E-val = 0.01
            phrog_results += "\t".join([cds_id,phrog_name,str(E_val),str(score),str(round(qcov,5)),position])+"\n"
    with open(f"{fasta.split('.')[0]}_PHROG_results.tsv", "w") as f:
      f.write(phrog_results)
  except:
    with open("PHROG_ERRORS.txt", "a") as f:
      f.write(f"{fasta}\n")

subprocess.run("tar -czvf PHROG_results.tar.gz *_PHROG_results.tsv", shell=True)
