# opening_rectangle1 (Operator)

## Name

`opening_rectangle1` — Open a region with a rectangular structuring element.

## Signature

`def opening_rectangle1(region: HObject, width: int, height: int) -> HObject`

## Description

`opening_rectangle1` behaves as [`opening`](opening.md) with a rectangular
structuring element on the input region *`region`*.
The size of the rectangular structuring element
is determined by the parameters *`width`* and
*`height`*. As is the case for all [`opening`](opening.md)
variants, larger structures are preserved, while small regions like
lines or points are eliminated.

Similar to [`erosion_rectangle1`](erosion_rectangle1.md) and [`dilation_rectangle1`](dilation_rectangle1.md)
`opening_rectangle1` is a very fast operation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be opened.

**`region_opening`** (output_object)  region(-array) `→` HObject

Opened regions.

**`width`** (input_control)  extent.x `→` int

Width of the structuring rectangle.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 25, 33, 45, 60, 110, 150, 200

Value range:
`1
≤
width
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`height`** (input_control)  extent.y `→` int

Height of the structuring rectangle.

Default:
10

Suggested values:
1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 25, 33, 45, 60, 110, 150, 200

Value range:
`1
≤
height
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F1 be the area of an input region and H be the height of the
rectangle. Then the runtime complexity for one region is:
$$O(2 \cdot \sqrt{F1} \cdot ld(H)).$$ ![figure](../assets/b45eb24134c87f29.svg)

## Result

`opening_rectangle1` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`opening`,
`gen_rectangle1`,
`dilation_rectangle1`,
`erosion_rectangle1`

## Module

Foundation
