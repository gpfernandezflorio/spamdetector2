set terminal png size 400,400
set output "vtm.png"

set style line 1 lc rgb "purple"
set style line 2 lc rgb "#6B8E23"
set style line 3 lc rgb "skyblue"
set style line 4 lc rgb "orange"
set style line 5 lc rgb "yellow"

set style fill solid
set boxwidth 0.13

set ylabel "Tiempo (segundos)"
set xrange [0.5:5.5]
set logscale y
set title "Tiempo de predicción"
unset key

plot "vdttm.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", \
     "vrftm.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", \
     "vnbtm.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes", \
     "vknntm.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", \
     "vsvctm.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM"
