set title 'Execution time by particles quantities'
set ylabel 'Execution time (ticks/s)'
set xlabel 'Amount of particles (particles)'
set term png
set output 'particles.png'
set datafile separator ','
plot 'particles.csv' with linespoints
