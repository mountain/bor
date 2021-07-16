# -*- coding: utf-8 -*-

import os
from subprocess import call

from gen.constant import sizes, fontnames


def pdf(texfile, tgtdir):
    call(['xelatex', '-output-directory=%s' % tgtdir, texfile])


if __name__ == '__main__':
    for fntname in fontnames:
        for chridx in range(256):
            for spec, size in sizes.iteritems():
                tgtdir = 'dataset/pdf/%s/%s' % (fntname, spec)
                if not os.path.exists(tgtdir):
                    os.makedirs(tgtdir)

                texdir = 'dataset/tex/%s/%s' % (fntname, spec)
                texname = '%s/%s%03d.tex' % (texdir, fntname, chridx)

                pdf(texname, tgtdir)
