set terminal png size 300,400
set output "vac.png"

set style line 1 lc rgb "purple"
set style line 2 lc rgb "#6B8E23"
set style line 3 lc rgb "skyblue"
set style line 4 lc rgb "orange"
set style line 5 lc rgb "yellow"

set style fill solid
set boxwidth 0.13

set xrange [0.5:3.5]
set yrange [0:1]
set title "Accuracy"
unset key

plot "vdtac.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", \
     "vrfac.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", \
     "vnbac.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes", \
     "vknnac.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", \
     "vsvcac.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM"
