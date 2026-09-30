# InnerRectangle1 (Operator)

## Name

`InnerRectangle1` — Largest inner rectangle of a region.

## Signature

`static void HOperatorSet.InnerRectangle1(HObject regions, out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HRegion.InnerRectangle1(out HTuple row1, out HTuple column1, out HTuple row2, out HTuple column2)`

`void HRegion.InnerRectangle1(out int row1, out int column1, out int row2, out int column2)`

## Description

The operator `InnerRectangle1` determines the largest
axis-parallel rectangle that fits into a region. The rectangle is
described by the coordinates of the corner pixels (*`row1`*,
*`column1`*, *`row2`*, *`column2`*).

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in the width and height
of their inner rectangle.

If more than one region is passed in *`regions`* the results
are stored in tuples, the index of a value in the tuple
corresponding to the index of the input region. For empty regions
all parameters have the value 0 if no other behavior was set (see
[`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be examined.

**`row1`** (output_control)  rectangle.origin.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the upper left corner point.

**`column1`** (output_control)  rectangle.origin.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the upper left corner point.

**`row2`** (output_control)  rectangle.corner.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the lower right corner point.

**`column2`** (output_control)  rectangle.corner.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the lower right corner point.

## Result

The operator `InnerRectangle1` returns the value 2 (
H_MSG_TRUE)
if the
input is not empty. The behavior in case of empty input (no input
regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Possible Successors

`DispRectangle1`,
`GenRectangle1`

## Alternatives

`InnerCircle`

## See also

`SmallestRectangle1`,
`SelectShape`

## Module

Foundation
