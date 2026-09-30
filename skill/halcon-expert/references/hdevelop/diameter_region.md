# diameter_region (Operator)

## Name

`diameter_region` — Maximal distance between two boundary points of a region.

## Signature

`diameter_region(Regions : : : Row1, Column1, Row2, Column2, Diameter)`

## Description

The operator `diameter_region` calculates the
maximal distance between two boundary points of
a region. The coordinates of these two extremes
and the distance between them will be returned.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their diameter.

## Attention

If the region is empty, the results of *`Row1`*, *`Column1`*,
*`Row2`* and *`Column2`* (all of them = 0) may lead to
confusion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`Row1`** (output_control)  line.begin.y(-array) `→`  (integer)

Row index of the first extreme point.

**`Column1`** (output_control)  line.begin.x(-array) `→`  (integer)

Column index of the first extreme point.

**`Row2`** (output_control)  line.end.y(-array) `→`  (integer)

Row index of the second extreme point.

**`Column2`** (output_control)  line.end.x(-array) `→`  (integer)

Column index of the second extreme point.

**`Diameter`** (output_control)  number(-array) `→`  (real)

Distance of the two extreme points.

## Complexity

If F is the area of a region, the runtime
complexity amounts to O(sqrt(F)) on average.

## Result

The operator `diameter_region` returns the value 2 (
H_MSG_TRUE)
, if the input
is not empty. The reaction to empty input (no input regions are
available) may be determined with the help of the operator
`set_system('no_object_result',<Result>)`. The reaction
concerning an empty region (region is the empty set) will be determined
by the operator `set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`,
`runlength_features`

## Possible Successors

`disp_line`

## Alternatives

`smallest_rectangle2`

## Module

Foundation
