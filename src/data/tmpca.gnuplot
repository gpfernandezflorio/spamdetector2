set terminal png size 400,400
set output "tmpca.png"

set logscale x
set logscale y
set ylabel "Tiempo (segundos)"
set xlabel "Cantidad de Componentes"
set title "PCA"
unset key

plot "dttmpca.dat" w linespoints linetype 1 title "Decision Tree", "dttmpca.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rftmpca.dat" w linespoints linetype 2 title "Random Forest", "rftmpca.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbtmpca.dat" w linespoints linetype 3 title "Naive Bayes", "nbtmpca.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knntmpca.dat" w linespoints linetype 4 title "KNN", "knntmpca.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svctmpca.dat" w linespoints linetype 5 title "SVM", "svctmpca.dat" using 1:2:3 w errorbars linetype 5 title ""
