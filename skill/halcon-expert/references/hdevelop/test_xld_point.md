# test_xld_point (Operator)

## Name

`test_xld_point` — Test whether one or more contours or polygons enclose the given point(s).

## Signature

`test_xld_point(XLD : : Row, Column : IsInside)`

## Description

`test_xld_point` tests whether a test point (*`Row`*,
*`Column`*) is enclosed by a contour or polygon *`XLD`* and
returns the result in *`IsInside`*. If the input point is enclosed by
the contour or polygon, the return value is *1*, otherwise
*0*.
In the case of a single test point and multiple contours or polygons, the
(i-1)-th element of the resulting tuple *`IsInside`* indicates, whether
the point is enclosed by the i-th contour or polygon.
In the case of multiple test points and a single contour or polygon, the
i-th element of the resulting tuple *`IsInside`* indicates, whether the
i-th point is enclosed by the contour or polygon.
In the case of multiple test points and multiple contours or polygons, the
(i-1)-th element of the resulting tuple *`IsInside`* indicates, whether
the (i-1)-th point is enclosed by the i-th contour or polygon (the
subscription differs, because the indexing of the results tuple starts
with 0 in contrast to the indexing of object tuples).
In this case the
number of input points must be equal to the number of contours or polygons.
It is assumed that the contours or polygons are closed. If this is not the
case `test_xld_point` will artificially close the contour.
Nevertheless it is strongly recommended to pass only meaningful and closed
contours or polygons in *`XLD`*.

## Attention

If a test point is on the border of the contour or polygon,
`test_xld_point` will deliver unpredictable results, i.e. the result
may be *0* or *1* depending on arbitrary factors such as how
the polygon is oriented with respect to the coordinate system. Note further
that for points in the near proximity of the contour or polygon sides, a
reliable classification is practically impossible because of numerical
inaccuracies.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be tested.

**`Row`** (input_control)  point.y(-array) `→`  (real)

Row coordinates of the points to be tested.

**`Column`** (input_control)  point.x(-array) `→`  (real)

Column coordinates of the points to be tested.

Number of elements:
Column == Row

**`IsInside`** (output_control)  integer(-array) `→`  (integer)

Tuple with Boolean numbers.

## Result

`test_xld_point` returns 2 (
H_MSG_TRUE)
if the input is not empty.
If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If
necessary, an exception is raised.

## Possible Predecessors

`select_contours_xld`,
`close_contours_xld`,
`threshold_sub_pix`

## Module

Foundation
