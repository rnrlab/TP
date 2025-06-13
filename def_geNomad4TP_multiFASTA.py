import subprocess
import os

files = [f for f in os.listdir(".") if f.endswith(".fasta")]
for file in files:
  with open(file, "a") as fasta:
    fasta.write("\n")
subprocess.run("cat ./*.fasta > temp_1.fasta", shell=True)
subprocess.run("sudo -s", shell=True)
subprocess.run("conda activate /home/eduardo/miniconda3/envs/seqkit/", shell=True)
subprocess.run("seqkit seq -w 60 temp_1.fasta > temp_2.fasta", shell=True)
subprocess.run("mkdir ../geNomad", shell=True)
subprocess.run("conda deactivate", shell=True)
subprocess.run("cat temp_2.fasta | tr -s '\n' > TP_genomes.fasta", shell=True)
subprocess.run("grep -E 'A>|C>|T>|G>|N>' TP_genomes.fasta", shell=True)
subprocess.run("rm temp_1.fasta", shell=True)
subprocess.run("rm temp_2.fasta", shell=True)
subprocess.run("conda activate /home/eduardo/miniconda3/envs/mge/", shell=True)


print("Starting Annotation!")
# Annotation and Scrutiny
try:
  subprocess.run(f"genomad end-to-end --enable-score-calibration -t 32 ./TP_genomes.fasta ../geNomad/ /mnt/disk2/databases/genomad_db/", shell=True)
except:
  with open("geNomad_ERRORS.txt", "a") as f:
    f.write(f"{fasta}\n")
subprocess.run("conda deactivate", shell=True)
