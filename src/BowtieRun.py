import subprocess
import datetime


def bowtieRun(read1, read2, refpath, index, output):
    read1 = str(read1)
    read2 = str(read2)
    indexpath = str(refpath.joinpath(index))
    date = datetime.date.today()
    fname = str(date) + "_output"
    fname_sam = fname + ".sam"
    sam_output = str(output.joinpath(fname_sam))
    fname_bam = fname + ".bam"
    bam_output = str(output.joinpath(fname_bam))
    print('run bowtie2')
    bowtie_run = "bowtie2 -x " + indexpath + " -1 " + read1 + " -2 " + read2 + " -S " + sam_output
    print(bowtie_run)
    subprocess.call(bowtie_run, shell=True)
    print('run samtools')
    sam_command_string = "samtools view -Sb " + sam_output + " > " + bam_output
    print(sam_command_string)
    subprocess.call(sam_command_string, shell=True)
    return bam_output, fname
