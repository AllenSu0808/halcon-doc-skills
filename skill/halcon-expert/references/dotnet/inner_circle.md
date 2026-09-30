# InnerCircle (Operator)

## Name

`InnerCircle` — Largest inner circle of a region.

## Signature

`static void HOperatorSet.InnerCircle(HObject regions, out HTuple row, out HTuple column, out HTuple radius)`

`void HRegion.InnerCircle(out HTuple row, out HTuple column, out HTuple radius)`

`void HRegion.InnerCircle(out double row, out double column, out double radius)`

## Description

The operator `InnerCircle` determines the largest inner circle
of a region.
This is the biggest discrete circle region that completely fits into
the region.
For this circle the center (*`row`*, *`column`*) and the
radius (*`radius`*) are calculated.
If the position of the circle is ambiguous, the "first possible"
position (as far upper left as possible) is returned.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions with varying inner circles.

The output of the operator is chosen in such a way that it can be
used as an input for the operators [`DispCircle`](disp_circle.md),
[`GenCircle`](gen_circle.md), and [`GenEllipseContourXld`](gen_ellipse_contour_xld.md).

If several regions are passed in *`regions`* corresponding tuples
are returned as output parameters.
In case of an empty input region all parameters have the value
*0.0* if no other behavior was set with [`SetSystem`](set_system.md).

## Attention

If several inner circles are present at a region
only the most upper left solution is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`row`** (output_control)  circle.center.y(-array) `→` [HTuple](HTuple.md) (*double*)

Line index of the center.

**`column`** (output_control)  circle.center.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column index of the center.

**`radius`** (output_control)  circle.radius(-array) `→` [HTuple](HTuple.md) (*double*)

Radius of the inner circle.

Assertion:
`Radius >= 0`

## Example (HDevelop)

```
read_image(Image,'fabrik')
regiongrowing(Image,Seg,5,5,6,100)
select_shape(Seg,H,'area','and',100,2000)
inner_circle(H,Row,Column,Radius)
gen_circle(Circles,Row,Column,Radius)
dev_set_draw('margin')
dev_display(Circles)
```

## Complexity

If F is the area of the region and R is the radius of the
inner circle the runtime complexity is O(sqrt(F) * R).

## Result

The operator `InnerCircle` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`RunlengthFeatures`

## Possible Successors

`GenCircle`,
`DispCircle`

## Alternatives

`ErosionCircle`,
`InnerRectangle1`

## See also

`SetShape`,
`SelectShape`,
`SmallestCircle`

## Module

Foundation
