#!/bin/bash -e

FOAM_RUN='/home/hilary/OpenFOAM/hilary*-*/run'
OTHERDIR='/home/hilary/projects/gungHo1/testCases_Sept2012/compareAll'

pdfFiles=(
TC2/l2h.eps
TC2/linfh.eps
TC5/l2h.eps
TC5/linfh.eps
meshes/sphereMeshes/HRbucky/3/0/Urecon.eps
meshes/sphereMeshes/HRbucky/4/0/Urecon.eps
meshes/sphereMeshes/HRbucky/4/constant/meshUnder.eps
meshes/sphereMeshes/localRef/3/constant/mesh1.eps
meshes/sphereMeshes/localRef/3/constant/mesh2.eps
meshes/sphereMeshes/localRef/3/constant/mesh3.eps
)

png1Files=(
)

png2Files=(
)

gifFiles=(
)

cpFiles=(
)

for file in ${pdfFiles[*]}
do
    f=$FOAM_RUN/$file
    if [ ! -e $f ]; then f=$OTHERDIR/$file; fi
    fRoot=`dirname $f`/`basename $f .eps`
    pdfFile=$fRoot.pdf
    fileNew=links/`echo $file |sed 's/\//+/g' | sed 's/\./p/g' | sed 's/peps/\.pdf/g'`

    if [ -e $f ]; then
        if [ ! -e $pdfFile ]; then
            echo converting $file
            echo to  $fileNew
            makebb $f > /dev/null 2>&1
            epstopdf $f
        elif [ `stat -c "%Z" $f` -gt `stat -c "%Z" $pdfFile` ]; then
            echo converting $file
            echo to  $fileNew
            makebb $f > /dev/null 2>&1
            epstopdf $f
    #    else
    #        echo $pdfFile is newer
        fi
        
        if [ ! -e $fileNew ]; then ln -s $pdfFile $fileNew; fi
    else
        echo Error, no $f
        exit
    fi
done

for file in ${png1Files[*]}
do
    f=$FOAM_RUN/$file
    fRoot=`dirname $f`/`basename $f .eps`
    pngFile=$fRoot.png
    fileNew=links/`echo $file |sed 's/\//+/g' | sed 's/\./p/g' | sed 's/peps/\.png/g'`

    if [ -e $f ]; then
        if [ ! -e $pngFile ]; then
            echo converting $file
            echo to  $fileNew
            eps2png $f
        elif [ `stat -c "%Z" $f` -gt `stat -c "%Z" $pngFile` ]; then
            echo converting $file 
            echo to  $fileNew
            eps2png $f
      #  else
     #       echo $pngFile is newer
    #        eps2png $f
        fi
        
        if [ ! -e $fileNew ]; then ln -s $pngFile $fileNew; fi
    else
        echo Error, no $f
        exit
   fi
done

for file in ${png2Files[*]}
do
    f=$FOAM_RUN/$file
    fRoot=`dirname $f`/`basename $f .eps`
    pngFile=$fRoot.png
    fileNew=links/`echo $file |sed 's/\//+/g' | sed 's/\./p/g' | sed 's/peps/\.png/g'`

    if [ -e $f ]; then
        if [ ! -e $pngFile ]; then
            echo converting $file
            echo to  $fileNew
            eps2png2 $f
        elif [ `stat -c "%Z" $f` -gt `stat -c "%Z" $pngFile` ]; then
            echo converting $file 
            echo to  $fileNew
            eps2png2 $f
     #   else
     #       echo $pngFile is newer
    #        eps2png2 $f
        fi
        
        if [ ! -e $fileNew ]; then ln -s $pngFile $fileNew; fi
    else
        echo Error, no $f
        exit
   fi
done

for file in ${gifFiles[*]}
do
    f=$FOAM_RUN/$file
    fRoot=`dirname $f`/`basename $f .gif`
    pngFile=$fRoot.png
    fileNew=links/`echo $file |sed 's/\//+/g' | sed 's/\./p/g' | sed 's/pgif/\.png/g'`

    if [ -e $f ]; then
        if [ ! -e $pngFile ]; then
            echo converting $file
            echo to  $fileNew
            convert -crop 0x0 $f $pngFile
        elif [ `stat -c "%Z" $f` -gt `stat -c "%Z" $pngFile` ]; then
            echo converting $file 
            echo to  $fileNew
            convert -crop 0x0 $f $pngFile
        #else
        #    echo $pngFile is newer
        fi
        
        if [ ! -e $fileNew ]; then ln -s $pngFile $fileNew; fi
    else
        echo Error, no $f
        exit
   fi
done

for file in ${cpFiles[*]}
do
    f=$FOAM_RUN/$file
    fileNew=links/`echo $file | sed 's/\//+/g'`
    if [ -e $f ]; then
        if [ ! -e $fileNew ]; then ln -s $f $fileNew; fi
    else
        echo Error, no $f
        exit
    fi
done

