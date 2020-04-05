import cmd


def bowtieRun(fastq_list, refpath, index):
    pathstring = ''
    for item in fastq_list:
        pathstring = pathstring + ',' + str(item)
    fastq_string = pathstring.lstrip(',')
    termcmd = cmd.Cmd()
    termcmd.precmd("bowtie2 -h")