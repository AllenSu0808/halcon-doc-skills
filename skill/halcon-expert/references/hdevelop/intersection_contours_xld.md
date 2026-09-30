# intersection_contours_xld (Operator)

## Name

`intersection_contours_xld` — Calculate the intersection points of two XLD contours

## Signature

`intersection_contours_xld(Contour1, Contour2 : : IntersectionType : Row, Column, IsOverlapping)`

## Description

`intersection_contours_xld` calculates the intersection points of the
XLD *`Contour1`* and XLD *`Contour2`* which, if any, are returned
in (*`Row`*,*`Column`*). The value in
*`IntersectionType`* defines the way to calculate the
intersections points. By setting
*`IntersectionType`* = *'self'*, only the self intersections
within both contours are returned, i.e., the intersections within
*`Contour1`* and XLD *`Contour2`*. For
*`IntersectionType`* = *'mutual'*, only the intersections
between both contours are taken into account. The default value is
*`IntersectionType`* = *'all'*. In this case both, the self
and the mutual intersections are returned in *`Row`*,*`Column`*).
If parts of the contours overlap in more than one point
*`IsOverlapping`* returns the value 1, otherwise 0 is returned.
*`IsOverlapping`* is set with regard to both the self and mutual
overlap, regardless of the setting in *`IntersectionType`*.
In case of a mutual overlap, the endpoints of the mutual segment are
returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour1`** (input_object)  xld_cont `→` object

First XLD contour.

**`Contour2`** (input_object)  xld_cont `→` object

Second XLD contour.

**`IntersectionType`** (input_control)  string `→`  (string)

Intersection points to be returned.

Default:
'all'

List of values:
'all', 'mutual', 'self'

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the intersection points.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the intersection points.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

Does a part of a contour lie above another contour part?

## Result

If the parameters are valid, the operator `intersection_contours_xld`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_segments`,
`intersection_segment_contour_xld`

## See also

`intersection_segment_line`,
`intersection_lines`,
`intersection_line_contour_xld`

## Module

Foundation
