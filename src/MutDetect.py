import pathlib
import argparse


def main():
    progparser = argparse.ArgumentParser(
        description="This program is designed accept the directory location of fastq files"
                    "and location of the bowtie reference index. Afterwards it will align"
                    "them in bowtie and pass the bam file into a mutation detection "
                    "package in GATK")
    progparser.add_argument("--fastq", help="directory to fastq files")
    progparser.add_argument("--reference", help="directory to reference")


if __name__ == "__main__":
    main()
