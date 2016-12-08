set terminal png
set output "roica.png"

set logscale x

set yrange [0:1]

plot "dtroica.dat" w linespoints linetype 1 title "Decision Tree", "dtroica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfroica.dat" w linespoints linetype 2 title "Random Forest", "rfroica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbroica.dat" w linespoints linetype 3 title "Naive Bayes", "nbroica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnroica.dat" w linespoints linetype 4 title "KNN", "knnroica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcroica.dat" w linespoints linetype 5 title "SVM", "svcroica.dat" using 1:2:3 w errorbars linetype 5 title ""
