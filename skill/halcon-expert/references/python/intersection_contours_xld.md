# intersection_contours_xld (Operator)

## Name

`intersection_contours_xld` — Calculate the intersection points of two XLD contours

## Signature

`def intersection_contours_xld(contour_1: HObject, contour_2: HObject, intersection_type: str) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_contours_xld_s(contour_1: HObject, contour_2: HObject, intersection_type: str) -> Tuple[float, float, int]`

## Description

`intersection_contours_xld` calculates the intersection points of the
XLD *`contour_1`* and XLD *`contour_2`* which, if any, are returned
in (*`row`*,*`column`*). The value in
*`intersection_type`* defines the way to calculate the
intersections points. By setting
*`intersection_type`* = *"self"*, only the self intersections
within both contours are returned, i.e., the intersections within
*`contour_1`* and XLD *`contour_2`*. For
*`intersection_type`* = *"mutual"*, only the intersections
between both contours are taken into account. The default value is
*`intersection_type`* = *"all"*. In this case both, the self
and the mutual intersections are returned in *`row`*,*`column`*).
If parts of the contours overlap in more than one point
*`is_overlapping`* returns the value 1, otherwise 0 is returned.
*`is_overlapping`* is set with regard to both the self and mutual
overlap, regardless of the setting in *`intersection_type`*.
In case of a mutual overlap, the endpoints of the mutual segment are
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour_1`** (input_object)  xld_cont `→` HObject

First XLD contour.

**`contour_2`** (input_object)  xld_cont `→` HObject

Second XLD contour.

**`intersection_type`** (input_control)  string `→` str

Intersection points to be returned.

Default:
"all"

List of values:
"all", "mutual", "self"

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the intersection points.

**`is_overlapping`** (output_control)  integer `→` int

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
