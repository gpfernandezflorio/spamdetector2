set terminal png
set output "acica.png"

set logscale x

set yrange [0:1]

plot "dtacica.dat" w linespoints linetype 1 title "Decision Tree", "dtacica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfacica.dat" w linespoints linetype 2 title "Random Forest", "rfacica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbacica.dat" w linespoints linetype 3 title "Naive Bayes", "nbacica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnacica.dat" w linespoints linetype 4 title "KNN", "knnacica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcacica.dat" w linespoints linetype 5 title "SVM", "svcacica.dat" using 1:2:3 w errorbars linetype 5 title ""
