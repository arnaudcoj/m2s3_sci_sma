set title 'Evolution du nombre de Fishes et de Shark en fonction du temps'
set xlabel 'Execution time (Ticks)'
set ylabel 'Amount of agents'
set term png
set output 'evolution_1.png'
set datafile separator ','
plot 'evolution.csv' using 2 title 'Fishes' with lines, 'evolution.csv' using 3 title 'Sharks' with lines

set title 'Evolution du rapport Fishes/Shark en fonction du temps'
set xlabel 'Fishes'
set ylabel 'Sharks'
set term png
set output 'evolution_2.png'
set datafile separator ','
plot 'evolution.csv' using 2:3 title 'Fishes/Sharks' with lines
