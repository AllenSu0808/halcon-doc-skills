# SmallestCircle (Operator)

## Name

`SmallestCircle` — Smallest surrounding circle of a region.

## Signature

`static void HOperatorSet.SmallestCircle(HObject regions, out HTuple row, out HTuple column, out HTuple radius)`

`void HRegion.SmallestCircle(out HTuple row, out HTuple column, out HTuple radius)`

`void HRegion.SmallestCircle(out double row, out double column, out double radius)`

## Description

The operator `SmallestCircle` determines the smallest
surrounding circle of a region, i.e., the circle with the smallest
area of all circles containing the region. For this circle the
center (*`row`*,*`column`*) and the radius
(*`radius`*) are calculated. The operator is applied when,
for example, the location and size of circular objects (e.g.,
coins) which, however, are not homogeneous inside or have broken
edges due to bad segmentation, has to be determined. The output of
the operator is selected in such a way that it can be used as input
for the operators [`DispCircle`](disp_circle.md) and
[`GenCircle`](gen_circle.md).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions with varying outer and inner radii.

If several regions are passed in *`regions`* corresponding
tuples are returned as output parameter. In case of empty region
all parameters have the value 0.0 if no other behavior was set (see
[`SetSystem`](set_system.md)).

## Attention

Internally, the calculation is based on the center coordinates of
the region pixels. To take into account that pixels are not just
infinitely small points but have a certain area, the calculated
radius is enlarged by 0.5 before it is returned in
*`radius`*. This, in most cases, gives acceptable results.
However, in the worst case (pixel diagonal) this enlargement is not
sufficient. If one wants to ensure that the border of the input
region completely lies within the circle, one had to enlarge the
radius by $1/\sqrt{2}$ ![figure](../assets/a055c991f65a51f2.svg) instead of 0.5. Consequently,
the value returned in *`radius`* must be corrected by
$1/\sqrt{2} - 0.5$ ![figure](../assets/9c06aa8d3354d23d.svg). However, this would also be only
an upper bound, i.e., the circle with the corrected radius would be
slightly too big in most cases.

![figure](../assets/49431d1fcf4d557d.svg)

The smallest surrounding circle of a region. Note that the
calculation is based on the center coordinates of the region pixels
and that 0.5 is added to the resulting radius.

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

Radius of the surrounding circle.

Assertion:
`Radius >= 0`

## Example (HDevelop)

```
read_image(Image,'fabrik')
regiongrowing(Image,Regions,5,5,6,100)
select_shape(Regions,SelectedRegions,'area','and',100,2000)
smallest_circle(SelectedRegions,Row,Column,Radius)
gen_circle(Circles,Row,Column,Radius)
dev_display (Circles)
```

## Complexity

If F is the area of the region, then the mean runtime complexity
is O(sqrt(F).

## Result

The operator `SmallestCircle` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input regions available)
is set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
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

`EllipticAxis`,
`SmallestRectangle1`,
`SmallestRectangle2`

## See also

`SetShape`,
`SelectShape`,
`InnerCircle`

## Module

Foundation
