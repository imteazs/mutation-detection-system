import subprocess


def bowtieRun(fastq_list, refpath, index):
    pathstring = ''
    for item in fastq_list:
        pathstring = pathstring + ',' + str(item)
    fastq_string = pathstring.lstrip(',')
    indexpath = str(refpath.joinpath(index))
    print(indexpath)
    #subprocess.call(["bowtie2", "-x", refpath, index, "-U"])
