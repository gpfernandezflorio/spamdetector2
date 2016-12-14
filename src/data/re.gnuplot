set terminal png size 300,400
set output "re.png"

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
set title "Recall"
unset key

plot "dtre.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", "dtre.dat" using 1:3:4 w errorbars linetype 1 title "", \
     "rfre.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", "rfre.dat" using 1:3:4 w errorbars linetype 2 title "", \
     "nbre.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes|", "nbre.dat" using 1:3:4 w errorbars linetype 3 title "", \
     "knnre.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", "knnre.dat" using 1:3:4 w errorbars linetype 4 title "", \
     "svcre.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM", "svcre.dat" using 1:3:4 w errorbars linetype 5 title ""
