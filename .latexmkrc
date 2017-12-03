# This shows how to use xelatex (http://en.wikipedia.org/wiki/XeTeX)
# with latexmk.  Xelatex uses Unicode and "supporting modern font
# technologies such as OpenType or Apple Advanced Typography.
#
#   WARNING: latexmk.pl is changing, and plans to have more internal
#     support for xelatex.
#
# Since xelatex only produces pdf files, it is a replacement for
# pdflatex.  To make it your default typesetting engine within latexmk
# you will not only need to set the $pdflatex variable to require the
# use of xelatex, but also to turn on production of pdf files and to
# turn off the production of dvi and ps files, as in the following
# code: 


$latex = 'xelatex --no-pdf -parse-first-line -synctex=1 %O %S && cp %R.xdv %D';
$pdf_mode = 3;
$postscript_mode = $dvi_mode = 0;
$dvipdf = 'xdvipdfmx -z1 %O -o %D %S';
$clean_full_ext .= ' xdv';
$pdf_previewer = 'mupdf %R.pdf';
$pdf_update_method = 4;
$pdf_update_command = 'xdotool search --name %R.pdf key r; notify-send -i info "%R.pdf updated!"';
