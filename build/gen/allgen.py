# -*- coding: utf-8 -*-

import os
import os.path as path

from gen.constant import sizes, fontnames
from gen.texgen import tex
from gen.pdfgen import pdf
from gen.pnggen import png


def allgen():
    for fntname in fontnames:
        baseext = path.basename(fntname)
        base, ext = path.splitext(baseext)

        for chridx in range(256):
            for spec, size in sizes.items():
                dntex = 'temp/tex/%s/%s' % (base, spec)
                fntex = '%s/%s%03d.tex' % (dntex, base, chridx)
                dnpdf = 'temp/pdf/%s/%s' % (base, spec)
                fnpdf = '%s/%s%03d.pdf' % (dnpdf, base, chridx)
                dnpng = 'glyph/%s/%s' % (base, spec)
                fnpng = '%s/%s%03d.png' % (dnpng, base, chridx)

                if not os.path.exists(dntex):
                    os.makedirs(dntex)
                    os.makedirs(dnpdf)
                    os.makedirs(dnpng)

                tex(fntex, fntname, chridx, size)
                pdf(fntex, dnpdf)
                png(fnpdf, fnpng)

                if os.path.exists(fntex):
                    os.remove(fntex)
                if os.path.exists(fnpdf):
                    os.remove(fnpdf)
                if os.path.exists(fnpng):
                    if os.stat(fnpng).st_size < 400:
                        os.remove(fnpng)


if __name__ == '__main__':
    allgen()