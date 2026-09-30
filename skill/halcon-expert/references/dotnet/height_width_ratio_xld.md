# HeightWidthRatioXld (Operator)

## Name

`HeightWidthRatioXld` — Compute the width, height, and aspect ratio of the enclosing
rectangle parallel to the coordinate axes of contours or polygons.

## Signature

`static void HOperatorSet.HeightWidthRatioXld(HObject XLD, out HTuple height, out HTuple width, out HTuple ratio)`

`HTuple HXLD.HeightWidthRatioXld(out HTuple width, out HTuple ratio)`

`double HXLD.HeightWidthRatioXld(out double width, out double ratio)`

## Description

The operator `HeightWidthRatioXld` calculates the enclosing
rectangle (parallel to the coordinate axes) for each input contour
or polygon. The enclosing rectangle is described by the coordinates
of the corner pixels
(`row1`,`column1`,`row2`,`column2`)
(see [`SmallestRectangle1Xld`](smallest_rectangle1_xld.md)). Based on these values,
`HeightWidthRatioXld` computes the width, height, and
aspect ratio of the smallest surrounding rectangle as follows:
$$Width = Column2 - Column1 \\ Height = Row2 - Row1 \\ Ratio = Height/Width$$ ![figure](../assets/5525136d703e84dc.svg)

If more than one contour or polygon is passed, the results are
stored in tuples in the same order as the respective contours or
polygons in *`XLD`*. In case of an empty contour all parameters
have the value 0 if no other behavior was set (see
[`SetSystem`](set_system.md)).

## Attention

If $\texttt{Width}=0$, *`ratio`* is set
to DBL_MAX (1.797e308).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be examined.

**`height`** (output_control)  extent.y(-array) `→` [HTuple](HTuple.md) (*double*)

Height of the enclosing rectangle.

**`width`** (output_control)  extent.x(-array) `→` [HTuple](HTuple.md) (*double*)

Width of the enclosing rectangle.

**`ratio`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Aspect ratio of the enclosing rectangle.

## Complexity

If N is the number of contour points, the runtime complexity is
O(N).

## Result

`HeightWidthRatioXld` returns 2 (
H_MSG_TRUE)
if the input is not
empty. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`

## Possible Successors

`GenPolygonsXld`

## Alternatives

`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`ShapeTransXld`

## See also

`ShapeTransXld`,
`SmallestCircleXld`,
`EllipticAxisXld`,
`AreaCenterXld`

## Module

Foundation
