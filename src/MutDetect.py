from pathlib import Path, PurePath
import argparse
import BowtieRun
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
    list_fastq = list(fastq)
    ref = PurePath(arguments.ref)
    index = arguments.idxname
    bamfilepath, fname = BowtieRun.bowtieRun(list_fastq, ref, index, output)
    GatkPipe.gatkRun(bamfilepath, output, fname)

if __name__ == "__main__":
    main()
