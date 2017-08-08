gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$2  -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages     -dCompressFonts=true -r90 -sOutputFile=$3 $1

du -sh $1
du -sh $3
