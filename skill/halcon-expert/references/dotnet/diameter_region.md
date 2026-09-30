# DiameterRegion (Operator)

## Name

`DiameterRegion` — Maximal distance between two boundary points of a region.

## Signature

`static void HOperatorSet.DiameterRegion(HObject regions, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2, out HTuple diameter)`

`void HRegion.DiameterRegion(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2, out HTuple diameter)`

`void HRegion.DiameterRegion(out int row1, out int column1, out int row2, out int column2, out double diameter)`

## Description

The operator `DiameterRegion` calculates the
maximal distance between two boundary points of
a region. The coordinates of these two extremes
and the distance between them will be returned.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their diameter.

## Attention

If the region is empty, the results of *`row1`*, *`column1`*,
*`row2`* and *`column2`* (all of them = 0) may lead to
confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`row1`** (output_control)  line.begin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of the first extreme point.

**`column1`** (output_control)  line.begin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of the first extreme point.

**`row2`** (output_control)  line.end.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row index of the second extreme point.

**`column2`** (output_control)  line.end.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of the second extreme point.

**`diameter`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Distance of the two extreme points.

## Complexity

If F is the area of a region, the runtime
complexity amounts to O(sqrt(F)) on average.

## Result

The operator `DiameterRegion` returns the value 2 (
H_MSG_TRUE)
, if the input
is not empty. The reaction to empty input (no input regions are
available) may be determined with the help of the operator
`set_system('no_object_result',<Result>)`. The reaction
concerning an empty region (region is the empty set) will be determined
by the operator `set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`RunlengthFeatures`

## Possible Successors

`DispLine`

## Alternatives

`SmallestRectangle2`

## Module

Foundation
