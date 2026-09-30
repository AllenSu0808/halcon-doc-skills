# area_center (Operator)

## Name

`area_center` — Area and center of regions.

## Signature

`def area_center(regions: HObject) -> Tuple[Sequence[int], Sequence[float], Sequence[float]]`

`def area_center_s(regions: HObject) -> Tuple[int, float, float]`

## Description

The operator `area_center` calculates the area and the center
of the input regions. The area is defined as the number of
pixels of a region. The center is calculated as the mean value
of the line or column coordinates, respectively, of all pixels.

In the documentation of this chapter ([Regions / Features](toc_regions_features.md)), you can
find an image illustrating regions which vary in their area.

If more than one region is passed the results are stored in tuples,
the index of a value in the tuple corresponding to the index of the
input region. In case of empty region all parameters have the value 0.0
if no other behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Region(s) to be examined.

**`area`** (output_control)  integer(-array) `→` Sequence[int]

Area of the region.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Line index of the center.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column index of the center.

## Complexity

If F is the area of a region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `area_center` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## See also

`select_shape`

## Module

Foundation
