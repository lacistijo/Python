# by Laszlo Tatai
# created on 2017.04.16
# function to calculate mean and standard deviation


def strddev(sample, bessel=None, show=None):
    n = len(sample)
    if show == 1: print "Sample length: " + str(n)
    mean = sum(sample)/float(n)
    expdev = [(value - mean)**2 for value in sample]
    if bessel == 1: n -= 1
    variance = sum(expdev)/float(n)
    if show == 1: print "Sample mean: "+str(mean)+"\n"          \
                        "Sample variance: "+str(variance)+"\n"  \

    strdev = variance**0.5
    return mean, strdev