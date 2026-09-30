# shape_trans_xld (Operator)

## Name

`shape_trans_xld` — Transform the shape of contours or polygons.

## Signature

`shape_trans_xld(XLD : XLDTrans : Type : )`

## Description

[`shape_trans`](shape_trans.md) transforms the input contours or polygons
depending on the parameter *`Type`*:

- **'convex'** —

  Convex hull.
- **'ellipse'** —

  Ellipse with the same moments and area as the input contour or polygon. The
  closed input contour or polygon must not intersect itself, otherwise the
  resulting ellipse is not meaningful(Whether the input contour or polygon
  intersects itself or not can be determined with
  [`test_self_intersection_xld`](test_self_intersection_xld.md)).
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

**`XLD`** (input_object)  xld(-array) `→` object

Contours or polygons to be transformed.

**`XLDTrans`** (output_object)  xld(-array) `→` object

Transformed contours respectively polygons.

**`Type`** (input_control)  string `→`  (string)

Type of transformation.

Default:
'convex'

List of values:
'convex', 'ellipse', 'outer_circle', 'rectangle1', 'rectangle2'

## Result

`shape_trans_xld` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty input (no contours given) can be set
via `set_system('no_object_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`edges_sub_pix`,
`threshold_sub_pix`,
`gen_contour_polygon_xld`,
`test_self_intersection_xld`

## Alternatives

`smallest_circle_xld`,
`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`elliptic_axis_xld`

## See also

`smallest_circle_xld`,
`smallest_rectangle1_xld`,
`smallest_rectangle2_xld`,
`elliptic_axis_xld`

## Module

Foundation
