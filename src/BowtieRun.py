import cmd

def bowtieRun(fastq_list):
    pathstring = ''
    for item in fastq_list:
        pathstring = pathstring + ',' + str(item)
    print(pathstring)
