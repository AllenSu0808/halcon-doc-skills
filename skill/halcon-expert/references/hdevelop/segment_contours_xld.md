# segment_contours_xld (Operator)

## Name

`segment_contours_xld` — Segment XLD contours into line segments and circular or elliptic arcs.

## Signature

`segment_contours_xld(Contours : ContoursSplit : Mode, SmoothCont, MaxLineDist1, MaxLineDist2 : )`

## Description

`segment_contours_xld` segments the input contours
*`Contours`* into lines if
*`Mode`*=*'lines'*, into lines and circular arcs if
*`Mode`*=*'lines_circles'*, or into lines and elliptic
arcs if *`Mode`*=*'lines_ellipses'*. The segmented
contours are returned in *`ContoursSplit`*. The information on
whether an output contour represents a line or a circular or
elliptic arc is done via the global contour attribute
*'cont_approx'* (see [`get_contour_global_attrib_xld`](get_contour_global_attrib_xld.md)
for further information).

`segment_contours_xld` first approximates
the input contours by polygons. With this, the contours are oversegmented
in curved areas. After this, the contours are approximated according to
the modes *`Mode`* given below. If *`SmoothCont`* is set to a
value > 0, the input contours are first smoothed (see
[`smooth_contours_xld`](smooth_contours_xld.md)). This can be necessary to prevent very
short segments in the polygonal approximation and to achieve a more
robust fit with circular or elliptic arcs, because the smoothing
suppresses outliers on the contours.

The calculation of the segmentation depends on the respective selected
method in *`Mode`*:

- ***'lines'*** —

  The Ramer algorithm is used to perform a polygon approximation with
  a maximum distance of *`MaxLineDist1`* (see [`gen_polygons_xld`](gen_polygons_xld.md)).
  If *`Mode`*=*'lines'*, the parameter
  *`MaxLineDist2`* is ignored.
- ***'lines_circles'* or *'lines_ellipses'*** —

  The initial polygonal approximation is done by using the Ramer
  algorithm (see [`gen_polygons_xld`](gen_polygons_xld.md)) with a maximum distance of
  *`MaxLineDist1`*. If the maximum distance of the
  resulting arc to the contour is smaller than the maximum distance of
  the two line segments, the two line segments are replaced with the
  arc. This procedure is iterated until no more changes occur.
  After this, the parts of the contour that are still approximated by
  line segments are again segmented with a polygonal approximation
  with maximum distance *`MaxLineDist2`*, and the newly created
  line segments are merged to circular or elliptical arcs where
  possible. This changes the output only if *`MaxLineDist2`*
  differs from *`MaxLineDist1`*.
  This two-step approach is more efficient than a one-step approach with
  *`MaxLineDist2`*, since fewer line segments are generated in
  the first step, and hence the circle or ellipse fit has to be
  performed less often. Therefore, parts of the input contours that
  can be approximated by long arcs can be found more efficiently. In
  the second step, parts of the input contours that can be
  approximated by short arcs are found and the end parts of long
  arcs are refined.
  In order to benefit from this two-step approach it is recommended to set
  *`MaxLineDist2`* < *`MaxLineDist1`*.

The resulting contours are at least 3 pixel long and contain at
least 6 successive points of the input contour. All input contours
with a length less than 3 pixel or with less than 6 contour points
are copied to the output contours without modifications.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Contours to be segmented.

**`ContoursSplit`** (output_object)  xld_cont-array `→` object

Segmented contours.

**`Mode`** (input_control)  string `→`  (string)

Mode for the segmentation of the contours.

Default:
'lines_circles'

List of values:
'lines', 'lines_circles', 'lines_ellipses'

**`SmoothCont`** (input_control)  integer `→`  (integer)

Number of points used for smoothing the contours.

Default:
5

Suggested values:
0, 3, 5, 7, 9

Restriction:
`SmoothCont == 0 || SmoothCont >= 3 && odd(SmoothCont)`

**`MaxLineDist1`** (input_control)  real `→`  (real)

Maximum distance between a contour and the approximating
line (first iteration).

Default:
4.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0, 3.5

Restriction:
`MaxLineDist1 >= 0.0`

**`MaxLineDist2`** (input_control)  real `→`  (real)

Maximum distance between a contour and the approximating
line (second iteration).

Default:
2.0

Suggested values:
1.0, 1.5, 2.0, 2.5, 3.0, 3.5

Restriction:
`MaxLineDist2 >= 0.0`

## Example (HDevelop)

```
read_image (Image, 'pumpe')
edges_sub_pix (Image, Edges, 'canny', 1.5, 15, 40)
segment_contours_xld (Edges, ContoursSplit, 'lines_circles', 5, 4, 2)
count_obj (ContoursSplit, Number)
gen_empty_obj (Lines)
gen_empty_obj (Circles)
for I := 1 to Number by 1
  select_obj (ContoursSplit, Contour, I)
  get_contour_global_attrib_xld (Contour, 'cont_approx', Type)
  if (Type == -1)
      concat_obj (Lines, Contour, Lines)
  else
      concat_obj (Circles, Contour, Circles)
  endif
endfor
fit_line_contour_xld (Lines, 'tukey', -1, 0, 5, 2, RowBegin, ColBegin, \
                      RowEnd, ColEnd, Nr, Nc, Dist)
fit_circle_contour_xld (Circles, 'atukey', -1, 2, 0, 3, 2, Row, Column, \
                        Radius, StartPhi, EndPhi, PointOrder)
```

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`edges_sub_pix`

## Possible Successors

`fit_line_contour_xld`,
`fit_ellipse_contour_xld`,
`fit_circle_contour_xld`,
`get_contour_global_attrib_xld`

## See also

`split_contours_xld`,
`get_contour_global_attrib_xld`,
`smooth_contours_xld`,
`gen_polygons_xld`

## Module

Foundation
