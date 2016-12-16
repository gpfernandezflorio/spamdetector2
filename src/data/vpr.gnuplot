set terminal png size 300,400
set output "vpr.png"

set style line 1 lc rgb "purple"
set style line 2 lc rgb "#6B8E23"
set style line 3 lc rgb "skyblue"
set style line 4 lc rgb "orange"
set style line 5 lc rgb "yellow"

set style fill solid
set boxwidth 0.13

set xtics rotate by -30
set xrange [0.5:5.5]
set yrange [0:1]
set title "Precision"
unset key

plot "vdtpr.dat" using 1:3:xtic(2) w boxes ls 1 title "Decision Tree", \
     "vrfpr.dat" using 1:3:xtic(2) w boxes ls 2 title "Random Forest", \
     "vnbpr.dat" using 1:3:xtic(2) w boxes ls 3 title "Naive Bayes", \
     "vknnpr.dat" using 1:3:xtic(2) w boxes ls 4 title "KNN", \
     "vsvcpr.dat" using 1:3:xtic(2) w boxes ls 5 title "SVM"
