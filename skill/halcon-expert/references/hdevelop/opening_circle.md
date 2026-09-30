# opening_circle (Operator)

## Name

`opening_circle` — Open a region with a circular structuring element.

## Signature

`opening_circle(Region : RegionOpening : Radius : )`

## Description

`opening_circle` is defined as an erosion followed by a
Minkowski addition with a circular structuring element (see example).
[`opening`](opening.md) serves to eliminate small regions (smaller than
the circular structuring element) and to smooth the boundaries of a
region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be opened.

**`RegionOpening`** (output_object)  region(-array) `→` object

Opened regions.

**`Radius`** (input_control)  real `→`  (real / integer)

Radius of the circular structuring element.

Default:
3.5

Suggested values:
1.5, 2.5, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5, 19.5, 25.5, 33.5, 45.5, 60.5, 110.5

Value range:
`0.5
≤
Radius
≤
511.5` (lin)

Minimum increment:
1.0

Recommended increment:
1.0

## Example (HDevelop)

```
* Large regions in an aerial picture (beech trees or meadows):
read_image (Image, 'forest_road')
threshold (Image, Region, 120, 255)
* Close the small gaps.
closing_circle (Region, RegionClosing, 3.5)
* Select the large regions.
opening_circle (RegionClosing, RegionOpening, 19.5)
```

## Complexity

Let F1 be the area of the input region. Then the runtime
complexity for one region is:
$$O\left(4 \cdot \sqrt{F1} \cdot Radius\right) .$$ ![figure](../assets/c413264716510879.svg)

## Result

`opening_circle` returns 2 (
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

`opening`,
`dilation1`,
`minkowski_add1`,
`gen_circle`

## See also

`transpose_region`

## Module

Foundation
