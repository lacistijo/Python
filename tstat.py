# by Laszlo Tatai
# created on 2017.04.16
# function to calculate t-statistic based on a sample and population mean

def tstat(sample, pmean):
    n = len(sample)
    (smean, sstrdev) = strddev(sample, bessel=1)
    tvalue = (smean - pmean) / (sstrdev / n**0.5)
    return tvalue