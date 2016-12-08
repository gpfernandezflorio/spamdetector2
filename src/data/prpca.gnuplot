set terminal png
set output "prpca.png"

set logscale x

set yrange [0:1]

plot "dtprpca.dat" w linespoints linetype 1 title "Decision Tree", "dtprpca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rfprpca.dat" w linespoints linetype 2 title "Random Forest", "rfprpca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbprpca.dat" w linespoints linetype 3 title "Naive Bayes", "nbprpca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnprpca.dat" w linespoints linetype 4 title "KNN", "knnprpca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcprpca.dat" w linespoints linetype 5 title "SVM", "svcprpca.dat" using 1:2:3 w errorbars linetype 5 title ""
