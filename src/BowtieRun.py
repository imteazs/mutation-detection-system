import subprocess
import datetime


def bowtieRun(fastq_list, refpath, index, output):
    pathstring = ''
    for item in fastq_list:
        pathstring = pathstring + ',' + str(item)
    fastq_string = pathstring.lstrip(',')
    indexpath = str(refpath.joinpath(index))
    date = datetime.date.today()
    fname = str(date) + "_output"
    fname_sam = fname + ".sam"
    sam_output = str(output.joinpath(fname_sam))
    fname_bam = fname + ".bam"
    bam_output = str(output.joinpath(fname_bam))
    #subprocess.call(["bowtie2", "-x", indexpath, "-U", fastq_string, "-S", sam_output])
    sam_command_string = "samtools view -Sb " + sam_output + " > " + bam_output
    #subprocess.call(sam_command_string, shell=True)
    return bam_output, fname
