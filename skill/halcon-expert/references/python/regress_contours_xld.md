# regress_contours_xld (Operator)

## Name

`regress_contours_xld` — Calculate the parameters of a regression line to an XLD contour.

## Signature

`def regress_contours_xld(contours: HObject, mode: str, iterations: int) -> HObject`

## Description

`regress_contours_xld` calculates the following parameters
for the input XLD contours *`contours`*, and stores them with
the resulting contours as global attributes:

- the coordinates of the normal vector of the regression line,
  i.e., the least-squares approximating line, of all contour
  points; the normal vector always points from the origin to
  the line (attributes: *"regr_norm_row"*,
  *"regr_norm_col"*),
- the mean of the Euclidean distance of the contour points from
  the regression line (attribute: *"regr_mean_dist"*),
- the standard deviation of these distances to the regression
  line (attribute: *"regr_dev_dist"*),
- the distance of the regression line from the origin
  (attribute: *"regr_dist"*).

See [`get_contour_global_attrib_xld`](get_contour_global_attrib_xld.md) for further information about
global contour attributes.

For *`mode`* = *"no"*, the parameters of the
regression line are calculated for all points of the contour. In
addition, three different kinds of outlier treatment can be
applied. Outliers are contour points which do not lie on the
general contour direction in an “obvious” manner, and thus
“distort” the resulting regression line.

*`mode`* =

- *"drop"*: All contour points further away from the contour
  than the mean distance to the regression line are ignored
  for the calculation of the undistorted regression line.
- *"gauss"*: The distances of the contour points are weighted
  according to their probability of occurrence in a Gaussian
  distribution around the normal regression line.
- *"median"*: Here, also a normal distribution is assumed for the
  distances to the normal regression line, however with the
  outlier-independent standard deviation
  $\frac{M_{d}}{0.6745}$ ![figure](../assets/b33d6cad1acf4987.svg),
  with $M_{d}$:
  median of all distances.
  Again, the distances are weighted,
  and points further away than a certain distance are ignored
  for the undistorted regression line.

The calculation of the undistorted regression line can be iterated
several times (*`iterations`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont-array `→` HObject

Input XLD contours.

**`regress_contours`** (output_object)  xld_cont-array `→` HObject

Resulting XLD contours.

**`mode`** (input_control)  string `→` str

Type of outlier treatment.

Default:
"no"

List of values:
"drop", "gauss", "median", "no"

**`iterations`** (input_control)  integer `→` int

Number of iterations for the outlier treatment.

Default:
1

Suggested values:
1, 2, 3, 5, 10, 20

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`get_regress_params_xld`

## See also

`smooth_contours_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`

## References

H. Suesse, K. Voss: “Adaptive Ausgleichsrechnung und
Ausreißerproblematik für die digitale Bildverarbeitung”;
Proc. 15. DAGM Symposium, Springer Verlag, Lübeck 1993
  
R. Haralick, L. Shapiro: “Computer and Robot Vision” Vol. 2;
Kapitel 14.9, Addison-Wesley 1992

## Module

Foundation
