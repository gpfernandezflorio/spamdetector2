set terminal png size 200,1000
set output "tm.png"

set style line 1 lc rgb "purple"
set style line 2 lc rgb "#6B8E23"
set style line 3 lc rgb "skyblue"
set style line 4 lc rgb "orange"
set style line 5 lc rgb "yellow"

set style fill solid
set boxwidth 0.5

set logscale y
unset xtics
set xrange [0:6]
set ylabel "Tiempo (segundos)"
set ytics rotate by 90
unset key

plot "dttm.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", "dttm.dat" using 1:3:4 w errorbars linetype 1 title "", \
     "rftm.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", "rftm.dat" using 1:3:4 w errorbars linetype 2 title "", \
     "nbtm.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes", "nbtm.dat" using 1:3:4 w errorbars linetype 3 title "", \
     "knntm.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", "knntm.dat" using 1:3:4 w errorbars linetype 4 title "", \
     "svctm.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM", "svctm.dat" using 1:3:4 w errorbars linetype 5 title ""
