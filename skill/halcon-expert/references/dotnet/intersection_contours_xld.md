# IntersectionContoursXld (Operator)

## Name

`IntersectionContoursXld` — Calculate the intersection points of two XLD contours

## Signature

`static void HOperatorSet.IntersectionContoursXld(HObject contour1, HObject contour2, HTuple intersectionType, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionContoursXld` calculates the intersection points of the
XLD *`contour1`* and XLD *`contour2`* which, if any, are returned
in (*`row`*,*`column`*). The value in
*`intersectionType`* defines the way to calculate the
intersections points. By setting
*`intersectionType`* = *"self"*, only the self intersections
within both contours are returned, i.e., the intersections within
*`contour1`* and XLD *`contour2`*. For
*`intersectionType`* = *"mutual"*, only the intersections
between both contours are taken into account. The default value is
*`intersectionType`* = *"all"*. In this case both, the self
and the mutual intersections are returned in *`row`*,*`column`*).
If parts of the contours overlap in more than one point
*`isOverlapping`* returns the value 1, otherwise 0 is returned.
*`isOverlapping`* is set with regard to both the self and mutual
overlap, regardless of the setting in *`intersectionType`*.
In case of a mutual overlap, the endpoints of the mutual segment are
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour1`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

First XLD contour.

**`contour2`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Second XLD contour.

**`intersectionType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Intersection points to be returned.

Default:
"all"

List of values:
"all", "mutual", "self"

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Does a part of a contour lie above another contour part?

## Result

If the parameters are valid, the operator `IntersectionContoursXld`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionSegments`,
`IntersectionSegmentContourXld`

## See also

`IntersectionSegmentLine`,
`IntersectionLines`,
`IntersectionLineContourXld`

## Module

Foundation
