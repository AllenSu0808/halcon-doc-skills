# OpeningRectangle1 (Operator)

## Name

`OpeningRectangle1` — Open a region with a rectangular structuring element.

## Signature

`static void HOperatorSet.OpeningRectangle1(HObject region, out HObject regionOpening, HTuple width, HTuple height)`

`HRegion HRegion.OpeningRectangle1(int width, int height)`

## Description

`OpeningRectangle1` behaves as [`Opening`](opening.md) with a rectangular
structuring element on the input region *`region`*.
The size of the rectangular structuring element
is determined by the parameters *`width`* and
*`height`*. As is the case for all [`Opening`](opening.md)
variants, larger structures are preserved, while small regions like
lines or points are eliminated.

Similar to [`ErosionRectangle1`](erosion_rectangle1.md) and [`DilationRectangle1`](dilation_rectangle1.md)
`OpeningRectangle1` is a very fast operation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be opened.

**`regionOpening`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Opened regions.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

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

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

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

`OpeningRectangle1` returns 2 (
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

`Threshold`,
`Regiongrowing`,
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Opening`,
`GenRectangle1`,
`DilationRectangle1`,
`ErosionRectangle1`

## Module

Foundation
