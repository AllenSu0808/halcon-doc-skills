# get_contour_global_attrib_xld (Operator)

## Name

`get_contour_global_attrib_xld` — Return global attributes values of an XLD contour.

## Signature

`def get_contour_global_attrib_xld(contour: HObject, name: MaybeSequence[str]) -> Sequence[float]`

## Description

`get_contour_global_attrib_xld` returns the values of the
global attribute *`name`* of the XLD contour *`contour`*
in *`attrib`*. Global attributes are additional values defined
for each contour.
[`query_contour_global_attribs_xld`](query_contour_global_attribs_xld.md) can be used to query which global
attributes are set for a particular contour.

The following list contains information about the different global contour
attributes and the operators that add them to XLD contours:

- ***"bright_dark"*** —

  The type of transition for each output XLD contour is stored in the
  attribute *"bright_dark"*. It is set to *1.0*, if the
  connecting line forms a bright-dark transition (left to right, viewed
  from start point to end point), otherwise it is set to *0.0*.

  The attribute *"bright_dark"* is added by the following
  operator:

  [`connect_grid_points`](connect_grid_points.md)

  ![figure](../assets/426497a60eac416f.svg)

  Exemplary XLD contours (red and green) along the edges of a
  rectification grid (direction from start to end point
  indicated by arrow head).
  The transition type, stored in the attribute
  *"bright_dark"*, is *1.0* for red contours and
  *0.0* for green contours.
- ***"cont_approx"*** —

  The best way to approximate a contour is stated by the attribute
  *"cont_approx"*:
  for *"cont_approx"*=*-1.0*, the contour is best
  approximated by a line segment, for *"cont_approx"*=*0.0*,
  by an elliptic arc, and for *"cont_approx"*=*1.0*,
  by a circular arc.

  The attribute *"cont_approx"* is added by the following
  operator:

  [`segment_contours_xld`](segment_contours_xld.md)
- ***"is_hole"*** —

  For boundaries that enclose holes, the global contour attribute
  *"is_hole"* is set to *1.0*, otherwise, it is set to
  *0.0*.

  The attribute *"is_hole"* is added by the following operators:

  [`symm_difference_closed_contours_xld`](symm_difference_closed_contours_xld.md),
  [`difference_closed_contours_xld`](difference_closed_contours_xld.md),
  [`intersection_closed_contours_xld`](intersection_closed_contours_xld.md),
  [`union2_closed_contours_xld`](union2_closed_contours_xld.md)

  ![figure](../assets/a5ddf019a3f3aa5e.svg)

  Applying different set operations to XLD contours or contour sets
  adds the global attribute *"is_hole"* to the resulting
  contour(s). In the example above, for two sets (red and green) of
  closed contours different set operations are performed.
  If a resulting boundary encloses a hole (blue contours),
  *"is_hole"* is set to *1.0*, otherwise the value of
  *"is_hole"* is *0.0* (orange contours).
- ***"regr_dev_dist"*** —

  *"regr_dev_dist"* [px] gives the standard deviation of the
  (Euclidean) distances between the contour points and the regression
  line (see image below).

  The attribute *"regr_dev_dist"* is added by the following
  operator:

  [`regress_contours_xld`](regress_contours_xld.md)
- ***"regr_dist"*** —

  *"regr_dist"* [px] gives the minimal distance of the regression
  line from the origin of the
  image coordinate system (see image below).

  The attribute *"regr_dist"* is added by the following
  operator:

  [`regress_contours_xld`](regress_contours_xld.md)
- ***"regr_mean_dist"*** —

  The attribute *"regr_mean_dist"* [px] contains the mean of the
  Euclidean distances between each contour point and the regression line
  (see image below).

  The attribute *"regr_mean_dist"* is added by the following
  operator:

  [`regress_contours_xld`](regress_contours_xld.md)
- ***"regr_norm_col"*** —

  *"regr_norm_col"* [px] is the column coordinate of the unit
  normal vector of the regression line with the normal vector pointing
  from the origin to the line (see image below).

  The attribute *"regr_norm_col"* is added by the following
  operator:

  [`regress_contours_xld`](regress_contours_xld.md)
- ***"regr_norm_row"*** —

  *"regr_norm_row"* [px] is the row coordinate of the unit normal
  vector of the regression line with the normal vector pointing from
  the origin to the line (see image below).

  The attribute *"regr_norm_row"* is added by the following
  operator:

  [`regress_contours_xld`](regress_contours_xld.md)

  ![figure](../assets/2b5a5f7d68db25d3.svg)

  Sketch of the attributes
  *"regr_dist"*, *"regr_norm_col"*,
  *"regr_norm_row"* for the
  regression of an XLD contour (red). *"regr_mean_dist"* and
  *"regr_dev_dist"*
  are computed from the distances (black arrows) between the contour
  points and the regression line (solid black line).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input XLD contour.

**`name`** (input_control)  string(-array) `→` MaybeSequence[str]

Name of the attribute.

Default:
"regr_norm_row"

Suggested values:
"regr_norm_row", "regr_norm_col", "regr_mean_dist", "regr_dev_dist", "cont_approx", "bright_dark", "is_hole"

**`attrib`** (output_control)  real-array `→` Sequence[float]

Attribute values.

## Possible Predecessors

`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`segment_contours_xld`

## Possible Successors

`fit_circle_contour_xld`,
`fit_ellipse_contour_xld`,
`fit_line_contour_xld`,
`fit_rectangle2_contour_xld`

## See also

`query_contour_global_attribs_xld`,
`get_contour_attrib_xld`,
`query_contour_attribs_xld`

## Module

Foundation
