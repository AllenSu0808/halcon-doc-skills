# select_xld_point (Operator)

## Name

`select_xld_point` — Choose all contours or polygons containing a given point.

## Signature

`def select_xld_point(xlds: HObject, row: Union[float, int], column: Union[float, int]) -> HObject`

## Description

The operator `select_xld_point` selects all contours or polygons from
*`xlds`*
containing the test point (*`row`*,*`column`*).
If the contours or polygons overlap, more than one contour or polygon might
contain the point.
In this case, all these contours or polygons are returned.
If no contour or polygon contains the indicated point, an
empty object is returned.
It is assumed that the contours or polygons are closed. If this is not the
case, `select_xld_point` will artificially close the contours or
polygons.
Nevertheless, it is strongly recommended to pass only meaningful and closed
contours or polygons in *`xlds`* by calling [`select_contours_xld`](select_contours_xld.md)
with the parameter *"closed"* before calling
`select_xld_point`.

## Attention

If the test point is on the border of a contour or polygon,
`select_xld_point` will deliver unpredictable results, i.e., the
contour or polygon may be or may not be added to *`dest_xlds`*,
depending on arbitrary factors such as how
the polygon is oriented with respect to the coordinate system. Note further
that for points in the near proximity of the contour or polygon sides, a
reliable classification is practically impossible because of numerical
inaccuracies.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xlds`** (input_object)  xld(-array) `→` HObject

Contours or polygons to be examined.

**`dest_xlds`** (output_object)  xld(-array) `→` HObject

All contours or polygons containing the test
point.

**`row`** (input_control)  point.y `→` Union[float, int]

Line coordinate of the test point.

Default:
100.0

**`column`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the test point.

Default:
100.0

## Result

The operator `select_xld_point` returns the value 2 (
H_MSG_TRUE)
if the parameters are correct.
The behavior in case of empty input (no input contours or polygons
available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`select_contours_xld`,
`close_contours_xld`,
`threshold_sub_pix`

## Alternatives

`test_xld_point`

## Module

Foundation
