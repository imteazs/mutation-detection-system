import subprocess

def gatkRun(bamfile):
    gatk = "/home/sidnite/tools/gatk-4.1.6.0/gatk"
    gatkstring = gatk + " HaplotypeCaller "
    subprocess.call(gatkstring, shell=True)