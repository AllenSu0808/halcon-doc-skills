# OpeningCircle (Operator)

## Name

`OpeningCircle` — Open a region with a circular structuring element.

## Signature

`static void HOperatorSet.OpeningCircle(HObject region, out HObject regionOpening, HTuple radius)`

`HRegion HRegion.OpeningCircle(HTuple radius)`

`HRegion HRegion.OpeningCircle(double radius)`

## Description

`OpeningCircle` is defined as an erosion followed by a
Minkowski addition with a circular structuring element (see example).
[`Opening`](opening.md) serves to eliminate small regions (smaller than
the circular structuring element) and to smooth the boundaries of a
region.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be opened.

**`regionOpening`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Opened regions.

**`radius`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circular structuring element.

Default:
3.5

Suggested values:
1.5, 2.5, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5, 19.5, 25.5, 33.5, 45.5, 60.5, 110.5

Value range:
`0.5
≤
radius
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

`OpeningCircle` returns 2 (
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
`Connection`,
`Union1`,
`Watersheds`,
`ClassNdimNorm`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Opening`,
`Dilation1`,
`MinkowskiAdd1`,
`GenCircle`

## See also

`TransposeRegion`

## Module

Foundation
