set title 'Execution time for various particles quantities'
set ylabel 'Execution time'
set xlabel 'Amount of particles'
set term png
set output 'particles.png'
set datafile separator ','
plot 'particles.csv' with linespoints
