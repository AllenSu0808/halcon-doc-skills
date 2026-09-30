# SmallestRectangle1 (Operator)

## Name

`SmallestRectangle1` — Surrounding rectangle parallel to the coordinate axes.

## Signature

`static void HOperatorSet.SmallestRectangle1(HObject regions, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HRegion.SmallestRectangle1(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HRegion.SmallestRectangle1(out int row1, out int column1, out int row2, out int column2)`

## Description

The operator `SmallestRectangle1` calculates the surrounding
rectangle of all input regions (parallel to the coordinate axes).
The surrounding rectangle is described by the coordinates of the
corner pixels
(*`row1`*,*`column1`*,*`row2`*,*`column2`*).
The calculation of the rectangle is based on the center coordinates
of the region pixels.

![figure](../assets/3c3d4ecee09df07a.svg)

The smallest axis aligned surrounding rectangle of a region. Note
that the calculation is based on the center coordinates of the
region pixels.

If more than one region is passed in *`regions`*, the results
are stored in tuples, the index of a value in the tuple
corresponding to the index of a region in the input. In case of
empty region all parameters have the value 0 if no other behavior
was set (see [`SetSystem`](set_system.md)).

## Attention

In case of empty region the result of
*`row1`*,*`column1`*, *`row2`* and *`column2`*
(all are 0) can lead to confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`row1`** (output_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index of upper left corner point.

**`column1`** (output_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of upper left corner point.

**`row2`** (output_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Line index of lower right corner point.

**`column2`** (output_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column index of lower right corner point.

## Complexity

If F is the area of the region the mean runtime complexity is
O(sqrt(F)).

## Result

The operator `SmallestRectangle1` returns the value 2 (
H_MSG_TRUE)
if
the input is not empty. The behavior in case of empty input (no
input regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`RunlengthFeatures`

## Possible Successors

`DispRectangle1`,
`GenRectangle1`

## Alternatives

`HeightWidthRatio`,
`SmallestRectangle2`,
`AreaCenter`

## See also

`SelectShape`

## Module

Foundation
