#!/bin/bash -e

FOAM_RUN='/home/hilary/OpenFOAM/hilary*-*/run/shallowWaterSphere'

pdfFiles=(
WilliSteady/HRbucky/plots/perpError.eps
WilliSteady/HRbucky/3/0/UrError.eps
WilliMountain/legends/hError200_hError.eps
WilliMountain/bisect/4/0/mesh.eps
WilliMountain/Lloyd/4x2/0/mesh.eps
WilliMountain/Walko/4x2/0/mesh.eps
WilliMountain/PMA/4x2/0/mesh.eps
)

png1Files=(
WilliMountain/bisect/4/save/dt1800_asymmetricH_CLUSTPV_CLUSTh/1296000/hError200.eps
WilliMountain/Lloyd/4x2/save/dt1800_asymmetricH_CLUSTPV_CLUSTh/1296000/hError200.eps
WilliMountain/Walko/4x2/save/dt1800_asymmetricH_CLUSTPV_CLUSTh/1296000/hError200.eps
WilliMountain/PMA/4x2/save/dt1800_asymmetricH_CLUSTPV_CLUSTh/1296000/hError200.eps
baroJet/HRbucky/legends/vorticity_v.eps
baroJet/HRbucky/legends/vorticity.eps
baroJet/HRbucky/8/save/dt300_asymmetricH_CLUSTPV_CLUSTh/518400/vorticity.eps
baroJet/cube/288x288_eq/save/dt100_asymmetricH_CLUSTPV_CLUSTh/518400/vorticity.eps
baroJet/diamondCube/144x144_eq/save/dt120_asymmetricH_CLUSTPV_CLUSTh/518400/vorticity.eps
baroJet/HRbucky/8/ref/518400/vorticity.eps
)

png2Files=(
)

gifFiles=(
)

cpFiles=(
)

lnFiles=(
/home/hilary/projects/gungHo1/testCases_Sept2012/compareAll/TC2/l2h.pdf
/home/hilary/projects/gungHo1/testCases_Sept2012/compareAll/TC2/linfh.pdf
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

for file in ${lnFiles[*]}
do
    #f=$FOAM_RUN/$file
    f=$file
    dir=`dirname $file`; dir=`basename $dir`
    fileNew=links/$dir+`basename $file`
    if [ -e $f ]; then
        if [ ! -e $fileNew ]; then ln -s $f $fileNew; fi
    else
        echo Error, no $f
        exit
    fi
done

