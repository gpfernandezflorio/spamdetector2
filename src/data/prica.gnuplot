set terminal png size 300,400
set output "prica.png"

set logscale x
unset key
set yrange [0:1]
set title "Precision"

plot "dtprica.dat" w linespoints linetype 1 title "Decision Tree", "dtprica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfprica.dat" w linespoints linetype 2 title "Random Forest", "rfprica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbprica.dat" w linespoints linetype 3 title "Naive Bayes", "nbprica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnprica.dat" w linespoints linetype 4 title "KNN", "knnprica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcprica.dat" w linespoints linetype 5 title "SVM", "svcprica.dat" using 1:2:3 w errorbars linetype 5 title ""
