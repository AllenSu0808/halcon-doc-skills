# ShapeTransXld (Operator)

## Name

`ShapeTransXld` — Transform the shape of contours or polygons.

## Signature

`static void HOperatorSet.ShapeTransXld(HObject XLD, out HObject XLDTrans, HTuple type)`

`HXLD HXLD.ShapeTransXld(string type)`

`HXLDCont HXLDCont.ShapeTransXld(string type)`

`HXLDPoly HXLDPoly.ShapeTransXld(string type)`

`HXLDPara HXLDPara.ShapeTransXld(string type)`

`HXLDModPara HXLDModPara.ShapeTransXld(string type)`

`HXLDExtPara HXLDExtPara.ShapeTransXld(string type)`

## Description

[`ShapeTrans`](shape_trans.md) transforms the input contours or polygons
depending on the parameter *`type`*:

- **'convex'** —

  Convex hull.
- **'ellipse'** —

  Ellipse with the same moments and area as the input contour or polygon. The
  closed input contour or polygon must not intersect itself, otherwise the
  resulting ellipse is not meaningful(Whether the input contour or polygon
  intersects itself or not can be determined with
  [`TestSelfIntersectionXld`](test_self_intersection_xld.md)).
- **'outer_circle'** —

  Smallest enclosing circle.
- **'rectangle1'** —

  Smallest enclosing rectangle parallel to the coordinate axes.
- **'rectangle2'** —

  Smallest enclosing rectangle.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`XLD`** (input_object)  xld(-array) `→` [HXLD](HXLD.md)

Contours or polygons to be transformed.

**`XLDTrans`** (output_object)  xld(-array) `→` [HXLD](HXLD.md)

Transformed contours respectively polygons.

**`type`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of transformation.

Default:
"convex"

List of values:
"convex", "ellipse", "outer_circle", "rectangle1", "rectangle2"

## Result

`ShapeTransXld` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no contours given) can be set
via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`GenContoursSkeletonXld`,
`EdgesSubPix`,
`ThresholdSubPix`,
`GenContourPolygonXld`,
`TestSelfIntersectionXld`

## Alternatives

`SmallestCircleXld`,
`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`EllipticAxisXld`

## See also

`SmallestCircleXld`,
`SmallestRectangle1Xld`,
`SmallestRectangle2Xld`,
`EllipticAxisXld`

## Module

Foundation
