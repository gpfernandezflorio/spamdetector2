set terminal png size 300,400
set output "acpca.png"

set logscale x
unset key
set yrange [0:1]
set title "Accuracy"

plot "dtacpca.dat" w linespoints linetype 1 title "Decision Tree", "dtacpca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfacpca.dat" w linespoints linetype 2 title "Random Forest", "rfacpca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbacpca.dat" w linespoints linetype 3 title "Naive Bayes", "nbacpca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnacpca.dat" w linespoints linetype 4 title "KNN", "knnacpca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcacpca.dat" w linespoints linetype 5 title "SVM", "svcacpca.dat" using 1:2:3 w errorbars linetype 5 title ""
