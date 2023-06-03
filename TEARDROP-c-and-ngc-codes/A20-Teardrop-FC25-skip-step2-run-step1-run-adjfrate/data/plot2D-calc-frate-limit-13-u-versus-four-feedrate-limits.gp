
## File: plot2D-calc-frate-limit-13-u-versus-four-feedrate-limits.gp

clear
set size square
set autoscale
set grid

set xlabel "parameter u"
set ylabel "frate (mm/s)"
set title  "Plot 2D (u,frate) Four constraint components for feedrate limits" 


## set title  "plot2D-calc-frate-limit-13-u-versus-four-feedrate-limits.gp"

# COMMENT RANGES FOR DEFAULT
set xrange [ 0.0 : +1.0]

set yrange [ 0.0 : +60.0] 


## PLOT CHECK (TEMPORARY FRim-1[4] TO FIX)
plot   "data_calc_u_next.txt" using 2:18 with lines      title "limit-1 User Frate Command"
replot "data_calc_frate_limit.txt" using 2:5 with lines  title "limit-2 Max/Min Machine Velocity"
replot "data_calc_frate_limit.txt" using 2:6 with lines  title "limit-3 Error Contour Accuracy"
replot "data_calc_frate_limit.txt" using 2:7 with lines  title "limit-4 Normal Acceleration"


# DATA COLUMNS INDEX = COLUMN NUMBER
# rtime[1], 
# u[2], 
# u_next[3], 
# FRate_limit_1[4], 
# FRate_limit_2[5], 
# FRate_limit_3[6], 
# FRate_limit_4[7], 
# FRate_limit[8], 
# eps_N[9], 
# rho_N[10] 

# DTStamp_FHdata_calc_u_next 2022-06-23 12:23:39 179309410 

# EXECUTION
# gnuplot -p plot2D_calc_u_next_00_u_versus_u_next.gp


