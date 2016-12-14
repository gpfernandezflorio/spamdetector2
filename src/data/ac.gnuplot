set terminal png size 300,400
set output "ac.png"

set style line 1 lc rgb "purple"
set style line 2 lc rgb "#6B8E23"
set style line 3 lc rgb "skyblue"
set style line 4 lc rgb "orange"
set style line 5 lc rgb "yellow"

set style fill solid
set boxwidth 0.5

set xtics rotate by -45
set xrange [0:6]
set yrange [0:1]
unset xtics
set title "Accuracy"
unset key

plot "dtac.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", "dtac.dat" using 1:3:4 w errorbars linetype 1 title "", \
     "rfac.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", "rfac.dat" using 1:3:4 w errorbars linetype 2 title "", \
     "nbac.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes|", "nbac.dat" using 1:3:4 w errorbars linetype 3 title "", \
     "knnac.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", "knnac.dat" using 1:3:4 w errorbars linetype 4 title "", \
     "svcac.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM", "svcac.dat" using 1:3:4 w errorbars linetype 5 title ""
