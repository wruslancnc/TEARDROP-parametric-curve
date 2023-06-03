
// FILE: c_position.c
#include <math.h>

#include "curves/c_position.h"
#include "curves/c_pos_epsilon.h"
#include "curves/c_pos_rho.h"

double const PI_cpos = 3.141592653589793238;

double cu_step;
double chorderror_tolerance;

// ==================================================================
// X-POSITION COMPONENT
// ==============================================
double fxn_cpos_x(double u) 
  {

  // TEARDROP X
  double scaleup = 1.0;
  return (scaleup)*( -150.0*pow(u, 1.0) + 450.0*pow(u, 2.0) - 300.0*pow(u, 3.0) );

// ================================
/*
  // HYPOTROCOID X
  double scaleup = 1.0;     // 1.0 IS GOOD (OTHERS BAD)
  double k = (6.0*PI_cpos);
  double x = (2*cos(k*u) + 5*cos(2*k*u/3));
  return (scaleup)*(x);
*/
// ================================
/*  
  // EPICYCLOID X
  double scaleup = 10.0;
  double k = (2.0 * PI_cpos);
  double small = 1.0e-10; 
  double x =  (5*cos(k*u + small) - cos(5*k*u - small));     // X
  return (scaleup)*(x);
*/
// =================================
/*
 // ASTEPI X = ASTROID X + EPICYCLOID X
  double scaleup = 10.0;
  double k = (2.0 * PI_cpos);
  double small = 1.0e-10;

  double x_ast = +4.0*pow(sin(k*u), 3.0);
  double x_epi = +5.0*cos(k*u + small) - cos(5*k*u - small); 
  double x = x_ast + x_epi;
  return (scaleup)*(x);
*/
// =================================
/*
  // SNAHYP X = SNAILSHELL X + HYPOTROCOID
  double scaleup = 10.0;
  double k = (4.0 * PI_cpos);
  double small = 1.0e-10;
  double x_sna = (4.0)*( sin(2*k*u) / (k*u*k*u + 4.0) );
  double x_hyp = (2*cos(k*u) + 5*cos(2*k*u/3));
  double x = x_sna + x_hyp;
  return (scaleup)*(x);
*/  
// =================================
/* 
  // CIRCLE X
  double scaleup = 11.0;
  double k = (2.0 * PI_cpos);
  double x = sin(k*u);
  return (scaleup)*(x);
*/
// ==================================
/*
  // LINE-POLYU X
  double scaleup = 1.0;
  double polyu_x = ( 150.0*pow(u, 1.0) + 150.0*pow(u, 2.0) );
  return (scaleup)*(polyu_x);
*/
// ==================================
/* 
  // https://en.wikipedia.org/wiki/Astroid
  // ASTROID X
  double scaleup = 10.0;
  double k = (2.0 * PI_cpos);
  double x =   +4.0*pow(sin(k*u), 3.0);
  // double dx_du =  +4.0*(3.0)*k*pow(cos(k*u), 2.0);
  // double d2x_du2 = -4.0*(3.0)*(2.0)*k*k*pow(sin(k*u), 1.0);
  return (scaleup)*(x);
*/
// ===================================
/*
  // SNAILSHELL X
  double scaleup = 100.0;
  double k = (3.0*PI_cpos);
  double x = ( sin(2*k*u) / (k*u*k*u + 4.0) );
  return (scaleup)*(x);
*/
// ===================================
/*  
  // BUTTERFLY X
  double scaleup = 10.0;
  double k = (2.0*PI_cpos);
  double x = ( sin(k*u) * ( exp(cos(k*u))  - 2*cos(4*k*u) - pow(sin(k*u/12), 5.0) ));
  return (scaleup)*(x);
*/

} 
// ==================================================================
// Y-POSITION COMPONENT
// ==================================================================
double fxn_cpos_y (double u)
  {

  // TEARDROP Y
  double scaleup = 1.0;
  return (scaleup)*( -150.0*pow(u, 1.0) + 150.0*pow(u, 2.0) );

  // =================================
/* 
  // HYPOTROCOID Y
  double scaleup = 1.0;    // 1.0 IS GOOD (OTHERS BAD)
  double k = (6.0*PI_cpos);
  double y = (2*sin(k*u) - 5*sin(2*k*u/3));
  return (scaleup)*(y);
*/
  // ==================================  
/*
  // EPICYCLOID Y
  double scaleup = 10.0;
  double k = (2.0*PI_cpos);                      // RANGE
  double small = 1.0e-10;
  double y = ( 5*sin(k*u + small) - sin(5*k*u - small) );    // Y
  return (scaleup)*(y);
*/
// ==================================
/*
// ASTEPI Y = ASTROID Y + EPICYCLOID Y
  double scaleup = 10.0;
  double k = (2.0 * PI_cpos);
  double small = 1.0e-10;

  double y_ast = +4.0*pow(cos(k*u), 3.0);
  double y_epi = +5.0*sin(k*u + small) - sin(5*k*u - small) ;
  double y = y_ast + y_epi;
  return (scaleup)*(y);
*/
// ==================================
/*
  // SNAHYP Y = (10)*SNAILSHELL Y + HYPOTROCOID Y
  double scaleup = 10.0;
  double k = (4.0 * PI_cpos);
  double small = 1.0e-10;
  double y_sna = (10)*(cos(2*k*u) / (k*u*k*u + 4.0));
  double y_hyp = (2*sin(k*u) - 5*sin(2*k*u/3));
  double y = y_sna + y_hyp;
  return (scaleup)*(y);
*/
// ==================================  
/*
 // CIRCLE Y
  double scaleup = 11.0;
  double k = (2.0 * PI_cpos);
  double y = cos(k*u);
  return (scaleup)*(y);
*/
// ==================================
/*
  // LINE-POLYU Y
  double scaleup = 1.0;
  double polyu_y = ( 150.0*pow(u, 1.0) + 150.0*pow(u, 2.0) );
  return (scaleup)*(polyu_y);
*/
// ==================================
/* 
  // ASTROID Y
  double scaleup = 10.0;
  double k = (2.0*PI_cpos);
  double y   = +4.0*pow(cos(k*u), 3.0);
  // double dy_du  = -4.0*(3.0)*k*pow(sin(k*u), 2.0):
  // double d2y_du2 = -4.0*(3.0)*(2.0)*k*k*pow(cos(k*u), 1.0):
  return (scaleup)*(y);
*/
// ===================================
/*
  // SNAILSHELL Y
  double scaleup = 100.0;
  double k = (3.0*PI_cpos);
  double y = (cos(2*k*u) / (k*u*k*u + 4.0));
  return (scaleup)*(y);
*/
// ====================================
/*
  // BUTTERFLY Y
  double scaleup = 10.0;
  double k = (2.0*PI_cpos);
  double y = ( cos(k*u)*( exp(cos(k*u)) -2*cos(4*k*u) - pow(sin(k*u/12), 5.0)));
  return (scaleup)*(y);
*/
  
  }

// ==============================================  
// R-POSITION VECTOR RADIUS OR MAGNITUDE
// ==============================================
double fxn_cpos_r (double u)
  {
  double temp_px = fxn_cpos_x (u);
  double temp_py = fxn_cpos_y (u);
  double temp_pr = sqrt(temp_px*temp_px + temp_py*temp_py);
  
  return ( fabs(temp_pr) ); 
  }


// ==============================================
double fxn_cpos_magn(double u) {
	return (fxn_cpos_r(u));
}


// X-POSITION UNIT VECTOR
// ==============================================
double fxn_cpos_uvect_x(double u) {
	return (fxn_cpos_x(u)/fxn_cpos_r(u));
}

// Y-POSITION UNIT VECTOR
// ==============================================
double fxn_cpos_uvect_y(double u) {
	return (fxn_cpos_y(u)/fxn_cpos_r(u));
}

// ANGLE POSITION VECTOR IN RADIANS COUNTER-CLOCKWISE 
// ==============================================
double fxn_cpos_theta_rad(double u) {
	return (atan(fxn_cpos_y(u)/fxn_cpos_x(u)));
}

// ANGLE POSITION VECTOR IN DEGREES 
// ===============================================
double fxn_cpos_theta_deg(double u) {
	return ( fxn_cpos_theta_rad(u)*(180.0/PI_cpos) );
}

// POSITION CHORD ERROR = EPSILON  
// =================================================
double fxn_cpos_epsilon(double u, double u_next) {

    double the_epsilon = fxn_c_epsilon_for_arc_u_to_u_next(u, u_next, arc_u_points, arc_x_points,  arc_y_points);
	return (the_epsilon);
}

// POSITION RADIUS OF CURVATURE = RHO 
// =================================================
double fxn_cpos_rho(double u) {

    // FUNCTION DEFINED IN cpos_rho.h HEADER FILE
	return (fxn_c_radiuscurvature_rho_at_u(u)); 
}

// POSITION CURVATURE OF THE CURVE = K = (1.0/RHO)
// =================================================
double fxn_cpos_curvature(double u) {

 	return ( 1.0/fxn_cpos_rho(u) );
}

// ==================================================================
double fxn_calc_deltaS_use_rho_eps (double u, double u_next)
// ==================================================================
{
  double deltaS;

  double the_rho = fxn_cpos_rho(u + (u_next/2.0));
  double the_eps = fxn_cpos_epsilon(u, u_next);
  double temp1 = (the_rho*the_rho) - (the_rho - the_eps)*(the_rho - the_eps);
  deltaS = (2.0)*pow(temp1, 0.5);

  return (deltaS); // should be equivalent to chordlength
 } 
// ==================================================================
double fxn_calc_chordlength_use_paramcurve (double u, double u_next)
// ==================================================================
{
  double chordlength;
  double x1, x2, y1, y2;

  // Use param curve and geometry
  x1 = fxn_cpos_x (u);
  y1 = fxn_cpos_y (u);
  x2 = fxn_cpos_x(u+u_next);
  y2 = fxn_cpos_y(u+u_next);

  chordlength = fabs (sqrt (pow ((x2 - x1), 2.0) + pow ((y2 - y1), 2.0)));

  return (chordlength); // should be equivalent to deltaS
}

// ==================================================================
double fxn_calc_eps_use_paramcurve (double u, double u_next)
// ==================================================================
{
   double the_eps;

   // FULL CODES INSIDE:
   // curves/c_position.h and curves/c_pos_epsilon.h

   the_eps = fxn_cpos_epsilon(u, u_next);

   // Manual calculation geometrically using parametric curve.
   // Find position of chord endpoints (x1,y1) and (x2,y2) for parameter
   // at u and u+u_next, respectively.
   // Divide the chord into 20 linear segments of equal length.
   // At each point on the divided segment, construct a perpendicular
   // line to the chord. Find the intersection point of this perpendicular
   // line to the curve (arc). Calculate the distance from the point
   // on the chord to the curve. The value of epsilon is the maximum of
   // the 20 distances calculated.

   return (the_eps);
}

// ==================================================================
double fxn_calc_rho_use_paramcurve (double u, double u_next)
// ==================================================================
{
   double the_rho;

   // FULL CODES INSIDE:
   // curves/c_position.h and curves/c_pos_epsilon.h

   // REF: https://math24.net/curvature-radius.html
   // USING THE FORMULA AT THE REF ABOVE
   the_rho = fxn_cpos_rho(u);

   return (the_rho);

}


// ==================================================================
// ALHAMDULILLAH WRY.
// ==================================================================


