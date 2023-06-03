
## File: plot2D-calc-u-next-06-u-versus-rpos.gp

clear
set size square
set autoscale
set grid

set xlabel "parameter u"
set ylabel "radial position r"
set title  "Plot 2D (u,r) Radial position from (0,0) origin for parametric curve" 

## set title  "plot2D-calc-u-next-06-u-versus-rpos.gp"

# COMMENT RANGES FOR DEFAULT
# set xrange [ 0.0 : +1.0]
# set yrange [ 1.30E-4 : 1.40E-4]

## PLOT CHECK
plot   "data_calc_u_next.txt" using 2:10 with lines title "(u,r) point"
## replot "data_calc_u_next.txt" using 2:9 with lines 


# DATA COLUMNS INDEX = COLUMN NUMBER
# rtime[1] 
# u[2] 
# u_next[3] 
# t_interpol[4] 
# first_order[5] 
# second_order[6] 
# diff[7] 
# pos_x[8]
# pos_y[9]
# pos_r[10] 
# eps[11]
# rho[12] 
# curr_tang_accn[13] 
# curr_frate[14] 
# frate_limit[15] 
# x_frate[16] 
# y_frate17]

# DTStamp_FHdata_calc_u_next 2022-06-23 12:23:39 179309410 

# EXECUTION
# gnuplot -p plot2D_calc_u_next_00_u_versus_u_next.gp


