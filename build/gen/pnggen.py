# -*- coding: utf-8 -*-

import os
from subprocess import call

from gen.constant import sizes, fontnames


def png(pdffile, pngfile):
    call(['convert', '-density', '300', '-trim', '-monochrome', '-white-threshold', '50%', '-black-threshold', '50%', pdffile, '-quality', '100', pngfile])


if __name__ == '__main__':
    for fntname in fontnames:
        for chridx in range(256):
            for spec, size in sizes.iteritems():
                tgtdir = 'dataset/png/%s/%s' % (fntname, spec)
                if not os.path.exists(tgtdir):
                    os.makedirs(tgtdir)

                pdfdir = 'dataset/pdf/%s/%s' % (fntname, spec)
                pdffile = '%s/%s%03d.pdf' % (pdfdir, fntname, chridx)
                pngfile = '%s/%s%03d.png' % (tgtdir, fntname, chridx)

                png(pdffile, pngfile)
