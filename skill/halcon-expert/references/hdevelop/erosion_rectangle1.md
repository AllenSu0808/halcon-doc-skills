# erosion_rectangle1 (Operator)

## Name

`erosion_rectangle1` — Erode a region with a rectangular structuring element.

## Signature

`erosion_rectangle1(Region : RegionErosion : Width, Height : )`

## Description

`erosion_rectangle1` applies an erosion with a rectangular
structuring element to the input regions *`Region`*. The size
of the structuring rectangle is *`Width`* x
*`Height`*. The operator results in reduced regions, and the
areas smaller than the rectangular mask are eliminated.

`erosion_rectangle1` is a very fast operation because the
height of the rectangle enters only logarithmically into the runtime
complexity, while the width does not enter at all. This leads to
excellent runtime efficiency, even in the case of very large
rectangles (edge length > 100).

Regions containing small connecting strips between large areas are
separated only seemingly. They remain logically one region.

## Attention

To reduce a region by the same amount in all directions,
*`Width`* and *`Height`* must be odd. If this is not the
case, the region is eroded by a smaller amount at the right or at the
bottom, respectively, than at the left or at the top.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be eroded.

**`RegionErosion`** (output_object)  region(-array) `→` object

Eroded regions.

**`Width`** (input_control)  extent.x `→`  (integer)

Width of the structuring rectangle.

Default:
11

Suggested values:
1, 2, 3, 4, 5, 11, 15, 21, 31, 51, 71, 101, 151, 201

Value range:
`1
≤
Width
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Height`** (input_control)  extent.y `→`  (integer)

Height of the structuring rectangle.

Default:
11

Suggested values:
1, 2, 3, 4, 5, 11, 15, 21, 31, 51, 71, 101, 151, 201

Value range:
`1
≤
Height
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F1 be the area of an input region and H be the height of the
rectangle. Then the runtime complexity for one region is:
$$O\left(\sqrt{F1 \cdot id(H)}\right) .$$ ![figure](../assets/064fbbe19d75b278.svg)

## Result

`erosion_rectangle1` returns 2 (
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

`erosion1`,
`minkowski_sub1`

## See also

`gen_rectangle1`

## Module

Foundation
