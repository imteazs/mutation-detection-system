from pathlib import Path, PurePath
import argparse
import BowtieRun

def main():
    progparser = argparse.ArgumentParser(
        description="This program is designed accept the directory location of fastq files"
                    " and location of the bowtie reference index. Afterwards it will align"
                    "them in bowtie and pass the bam file into a mutation detection "
                    "package in GATK")

    progparser.add_argument("--fastq", help="directory to fastq files")
    progparser.add_argument("--ref", help="directory to reference")
    progparser.add_argument("--idxname", help="Name of bowtie index")

    arguments = progparser.parse_args()
    fastq = Path(arguments.fastq).glob("*.fastq.gz")
    list_fastq = list(fastq)
    ref = PurePath(arguments.ref)
    index = arguments.idxname
    BowtieRun.bowtieRun(list_fastq, ref, index)

if __name__ == "__main__":
    main()
