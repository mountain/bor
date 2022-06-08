import argparse

import os.path as pth


text = '''\\documentclass{article}
\\usepackage[paperwidth=1.618in, paperheight=1in]{geometry}
\\newfont{\\bongbaletter}{nimei}
\\newcommand{\\nimei}{{\\bongbaletter nimei}}

\\begin{document}
\\thispagestyle{empty}
\\hspace{0pt}\\vfill
\\begin{center}
\\nimei\\
\\end{center}
\\vfill\hspace{0pt}
\\end{document}'''

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--output-directory", type=str, default='.', help="output directory")
parser.add_argument("input_file")
opt = parser.parse_args()

outfile = pth.basename(opt.input_file).replace('600pk', 'tex')
outdir = opt.output_directory
outfile = pth.join(outdir, outfile)

if __name__ == '__main__':
    with open(outfile, 'w') as f:
        f.write(text)
        f.flush()
