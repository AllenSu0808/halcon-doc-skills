# DiameterXld (Operator)

## Name

`DiameterXld` — Maximum distance between two contour or polygon points.

## Signature

`static void HOperatorSet.DiameterXld(HObject XLD, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2, out HTuple diameter)`

`void HXLD.DiameterXld(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2, out HTuple diameter)`

`void HXLD.DiameterXld(out double row1, out double column1, out double row2, out double column2, out double diameter)`

## Description

The operator `DiameterXld` calculates the
maximum distance between two points of each input contour or polygon.
The coordinates of these two extremes
and the distance between them will be returned. The input contour or polygon
must not intersect itself, otherwise the resulting parameters are not
meaningful (Whether the input contour or polygon intersects itself or not
can be determined with [`TestSelfIntersectionXld`](test_self_intersection_xld.md)). If
the input contour or polygon is not closed it will be closed automatically.
If more than one contour or polygon is passed, the results are stored
in tuples in the same order as the respective contours or polygons in
*`XLD`*.

## Attention

If the contour or polygon is empty, the results of *`row1`*,
*`column1`*, *`row2`* and *`column2`* (all of them = 0) may
lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`row1`** (output_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the first extreme point of the
contours or polygons.

**`column1`** (output_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the first extreme point of the
contours or polygons.

**`row2`** (output_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the second extreme point of the
contour or polygons.

**`column2`** (output_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the second extreme point of the
contours or polygons.

**`diameter`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Distance of the two extreme points of the contours or
polygons.

## Result

The operator `DiameterXld` returns the value 2 (
H_MSG_TRUE)
, if the input
is not empty. The reaction to empty input (no input contours are
available) may be determined with the help of the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`SmallestRectangle2Xld`

## See also

`AreaCenterXld`

## Module

Foundation
