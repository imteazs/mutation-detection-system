import subprocess

def PreProcess(bamfile, fname):
    print("Preprocess bam file")
    picard = "java -jar /home/sidnite/bioinfo/picard.jar"
    dup_output = fname + '_mark_dup.bam'
    dup_met = fname + '_metrics.txt'
    mark_dup_cmd = picard + " I=" + bamfile + " O=" + dup_output + " M=" + dup_met
    print("run mark duplicate")
    print(mark_dup_cmd)
    subprocess.call(mark_dup_cmd, shell=True)


