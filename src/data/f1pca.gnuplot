set terminal png
set output "f1pca.png"

set logscale x

set yrange [0:1]

plot "dtf1pca.dat" w linespoints linetype 1 title "Decision Tree", "dtf1pca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rff1pca.dat" w linespoints linetype 2 title "Random Forest", "rff1pca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbf1pca.dat" w linespoints linetype 3 title "Naive Bayes", "nbf1pca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knnf1pca.dat" w linespoints linetype 4 title "KNN", "knnf1pca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svcf1pca.dat" w linespoints linetype 5 title "SVM", "svcf1pca.dat" using 1:2:3 w errorbars linetype 5 title ""
