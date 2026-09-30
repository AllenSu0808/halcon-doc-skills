# closing_rectangle1 (Operator)

## Name

`closing_rectangle1` — Close a region with a rectangular structuring element.

## Signature

`def closing_rectangle1(region: HObject, width: int, height: int) -> HObject`

## Description

`closing_rectangle1` behaves as [`closing`](closing.md) with a rectangular
structuring element on the input region *`region`*.
The size of the rectangular structuring element
is determined by the parameters *`width`* and
*`height`*. As is the case for all [`closing`](closing.md)
variants, regions' boundaries are smoothed and holes within a region
which are smaller than the rectangular structuring element are
closed.

Similar to [`erosion_rectangle1`](erosion_rectangle1.md) and [`dilation_rectangle1`](dilation_rectangle1.md)
`closing_rectangle1` is a very fast operation.

## Attention

`closing_rectangle1` is applied to each input region
separately. If gaps between different regions are to be closed,
[`union1`](union1.md) or [`union2`](union2.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be closed.

**`region_closing`** (output_object)  region(-array) `→` HObject

Closed regions.

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
$$O\Bigl(2\cdot\sqrt{F}1\cdot\log\_2(H)\Bigr) .$$ ![figure](../assets/df4b53e82b7edcc9.svg)

## Result

`closing_rectangle1` returns 2 (
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
`connection`,
`union1`,
`watersheds`,
`class_ndim_norm`

## Possible Successors

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`closing`

## See also

`dilation_rectangle1`,
`erosion_rectangle1`,
`opening_rectangle1`,
`gen_rectangle1`

## Module

Foundation
