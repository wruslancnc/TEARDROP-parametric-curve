// FILE: calc04_integration_error.h

#include <stdio.h>


// ===================================

void proc_writeheader_data_calc_intgr_error (FILE *FHdata_calc_intgr_error);

void proc_writefooter_data_calc_intgr_error (FILE *FHdata_calc_intgr_error);

void proc_write_calc_intgr_error (FILE *FHdata_calc_intgr_error, double rtime,
                                  double u, double u_next, double sum_deltaS,
                                  double sum_chordlength);


