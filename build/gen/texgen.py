# -*- coding: utf-8 -*-

import os

from gen.constant import sizes, fontnames


template = '''
\\documentclass[48pt]{article}
\\usepackage{pifont}
\\usepackage{mathptmx}
\\usepackage{anyfontsize}
\\usepackage{t1enc}
\\usepackage[paperwidth=1.5in, paperheight=1.5in]{geometry}

\\DeclareFontFamily{U}{astrosym}{}
\\DeclareFontShape{U}{astrosym}{m}{n}{<-> astrosym}{}
\\begin{document}
\\begin{center}
{\\fontsize{%i}{0} \\Pisymbol{%s}{%i}}
\\end{center}
\\thispagestyle{empty}
\\end{document}
'''


def content(fontname, charindex, fontsize):
    return template % (fontsize, fontname, charindex)


def tex(texfile, fntname, chridx, size):
    with open(texfile, 'w') as f:
        f.write(content(fntname, chridx, size))
