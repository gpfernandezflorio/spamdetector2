set terminal png size 300,400
set output "repca.png"

set logscale x
unset key
set yrange [0:1]
set xlabel "Recall"

plot "dtrepca.dat" w linespoints linetype 1 title "Decision Tree", "dtrepca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfrepca.dat" w linespoints linetype 2 title "Random Forest", "rfrepca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbrepca.dat" w linespoints linetype 3 title "Naive Bayes", "nbrepca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnrepca.dat" w linespoints linetype 4 title "KNN", "knnrepca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcrepca.dat" w linespoints linetype 5 title "SVM", "svcrepca.dat" using 1:2:3 w errorbars linetype 5 title ""
