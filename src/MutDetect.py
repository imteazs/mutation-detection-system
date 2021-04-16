from pathlib import Path, PurePath
import argparse
import BowtieRun
import PreProcess
import GatkPipe


def main():
    progparser = argparse.ArgumentParser(
        description="This program is designed accept the directory location of fastq files"
                    " and location of the bowtie reference index. Afterwards it will align"
                    "them in bowtie and pass the bam file into a mutation detection "
                    "package in GATK")

    progparser.add_argument("--fastq", help="directory to fastq files, note: This is where the bam file will be kept")
    progparser.add_argument("--ref", help="directory to prebuilt bowtie2 index")
    progparser.add_argument("--idxname", help="Name of bowtie index")

    arguments = progparser.parse_args()
    output = Path(arguments.fastq)
    fastq = Path(arguments.fastq).glob("*.fastq.gz")
    read1 = Path()
    read2 = Path()
    for fastname in fastq:
        name = fastname.name
        if '1.fastq.gz' in name:
            read1 = fastname
        elif '2.fastq.gz' in name:
            read2 = fastname
    ref = PurePath(arguments.ref)
    index = arguments.idxname
    bamfilepath, fname = BowtieRun.bowtieRun(read1, read2, ref, index, output)
    bam_dup_recal = PreProcess(bamfilepath, fname)
    #GatkPipe.gatkRun(bamfilepath, output, fname)

if __name__ == "__main__":
    main()
