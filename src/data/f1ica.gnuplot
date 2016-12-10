set terminal png size 300,400
set output "f1ica.png"

set logscale x
unset key
set yrange [0:1]
set xlabel "F1"

plot "dtf1ica.dat" w linespoints linetype 1 title "Decision Tree", "dtf1ica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rff1ica.dat" w linespoints linetype 2 title "Random Forest", "rff1ica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbf1ica.dat" w linespoints linetype 3 title "Naive Bayes", "nbf1ica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnf1ica.dat" w linespoints linetype 4 title "KNN", "knnf1ica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcf1ica.dat" w linespoints linetype 5 title "SVM", "svcf1ica.dat" using 1:2:3 w errorbars linetype 5 title ""
