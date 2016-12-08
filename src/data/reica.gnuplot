set terminal png
set output "reica.png"

set logscale x

set yrange [0:1]

plot "dtreica.dat" w linespoints linetype 1 title "Decision Tree", "dtreica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfreica.dat" w linespoints linetype 2 title "Random Forest", "rfreica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbreica.dat" w linespoints linetype 3 title "Naive Bayes", "nbreica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnreica.dat" w linespoints linetype 4 title "KNN", "knnreica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcreica.dat" w linespoints linetype 5 title "SVM", "svcreica.dat" using 1:2:3 w errorbars linetype 5 title ""
