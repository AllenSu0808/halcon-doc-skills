# smallest_circle (Operator)

## Name

`smallest_circle` — Smallest surrounding circle of a region.

## Signature

`smallest_circle(Regions : : : Row, Column, Radius)`

## Description

The operator `smallest_circle` determines the smallest
surrounding circle of a region, i.e., the circle with the smallest
area of all circles containing the region. For this circle the
center (*`Row`*,*`Column`*) and the radius
(*`Radius`*) are calculated. The operator is applied when,
for example, the location and size of circular objects (e.g.,
coins) which, however, are not homogeneous inside or have broken
edges due to bad segmentation, has to be determined. The output of
the operator is selected in such a way that it can be used as input
for the operators [`disp_circle`](disp_circle.md) and
[`gen_circle`](gen_circle.md).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions with varying outer and inner radii.

If several regions are passed in *`Regions`* corresponding
tuples are returned as output parameter. In case of empty region
all parameters have the value 0.0 if no other behavior was set (see
[`set_system`](set_system.md)).

## Attention

Internally, the calculation is based on the center coordinates of
the region pixels. To take into account that pixels are not just
infinitely small points but have a certain area, the calculated
radius is enlarged by 0.5 before it is returned in
*`Radius`*. This, in most cases, gives acceptable results.
However, in the worst case (pixel diagonal) this enlargement is not
sufficient. If one wants to ensure that the border of the input
region completely lies within the circle, one had to enlarge the
radius by $1/\sqrt{2}$ ![figure](../assets/a055c991f65a51f2.svg) instead of 0.5. Consequently,
the value returned in *`Radius`* must be corrected by
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

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Row`** (output_control)  circle.center.y(-array) `→`  (real)

Line index of the center.

**`Column`** (output_control)  circle.center.x(-array) `→`  (real)

Column index of the center.

**`Radius`** (output_control)  circle.radius(-array) `→`  (real)

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

The operator `smallest_circle` returns the value 2 (
H_MSG_TRUE)
if the input is not empty. The behavior in case of empty input (no input regions available)
is set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Possible Successors

`gen_circle`,
`disp_circle`

## Alternatives

`elliptic_axis`,
`smallest_rectangle1`,
`smallest_rectangle2`

## See also

`set_shape`,
`select_shape`,
`inner_circle`

## Module

Foundation
