set terminal png size 300,400
set output "ropca.png"

set logscale x
unset key
set yrange [0:1]
set xlabel "ROC Area Under Curve"

plot "dtropca.dat" w linespoints linetype 1 title "Decision Tree", "dtropca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfropca.dat" w linespoints linetype 2 title "Random Forest", "rfropca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbropca.dat" w linespoints linetype 3 title "Naive Bayes", "nbropca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnropca.dat" w linespoints linetype 4 title "KNN", "knnropca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcropca.dat" w linespoints linetype 5 title "SVM", "svcropca.dat" using 1:2:3 w errorbars linetype 5 title ""
