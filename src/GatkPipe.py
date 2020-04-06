import subprocess

def gatkRun(bamfile, output, fname):
    gatk = "/home/sidnite/tools/gatk-4.1.6.0/gatk"
    ref = "/home/sidnite/Documents/reference/h37_1kgmaj.fa"
    vcf_output = fname + ".g.vcf.gz"
    outpath = str(output.joinpath(vcf_output))

    gatkstring = gatk + " HaplotypeCaller " + " -R " + ref + " -I " + bamfile + " -O " + outpath
    subprocess.call(gatkstring, shell=True)

