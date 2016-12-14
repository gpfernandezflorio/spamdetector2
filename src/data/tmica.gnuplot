set terminal png size 400,400
set output "tmica.png"

#set logscale x
#set logscale y
set ylabel "Tiempo (segundos)"
set xlabel "Cantidad de Componentes"
set title "ICA"
unset key

plot "dttmica.dat" w linespoints linetype 1 title "Decision Tree", "dttmica.dat" using 1:2:3 w errorbars linetype 1 title "", \
     "rftmica.dat" w linespoints linetype 2 title "Random Forest", "rftmica.dat" using 1:2:3 w errorbars linetype 2 title "", \
     "nbtmica.dat" w linespoints linetype 3 title "Naive Bayes", "nbtmica.dat" using 1:2:3 w errorbars linetype 3 title "", \
     "knntmica.dat" w linespoints linetype 4 title "KNN", "knntmica.dat" using 1:2:3 w errorbars linetype 4 title "", \
     "svctmica.dat" w linespoints linetype 5 title "SVM", "svctmica.dat" using 1:2:3 w errorbars linetype 5 title ""
