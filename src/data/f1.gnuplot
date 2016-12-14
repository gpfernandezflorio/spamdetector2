set terminal png size 300,400
set output "f1.png"

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
set title "F1"
unset key

plot "dtf1.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", "dtf1.dat" using 1:3:4 w errorbars linetype 1 title "", \
     "rff1.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", "rff1.dat" using 1:3:4 w errorbars linetype 2 title "", \
     "nbf1.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes|", "nbf1.dat" using 1:3:4 w errorbars linetype 3 title "", \
     "knnf1.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", "knnf1.dat" using 1:3:4 w errorbars linetype 4 title "", \
     "svcf1.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM", "svcf1.dat" using 1:3:4 w errorbars linetype 5 title ""
