# partition_dynamic (Operator)

## Name

`partition_dynamic` — Partition a region horizontally at positions of small vertical extent.

## Signature

`partition_dynamic(Region : Partitioned : Distance, Percent : )`

## Description

`partition_dynamic` partitions the input *`Region`* horizontally
into regions that have an approximate width of *`Distance`*. The input
region is split at positions where it has a relatively small vertical extent.

The positions where the input region is split are determined by the
following approach: First, initial split positions are determined such that
they are equally distributed over the horizontal extent of the input region,
i.e., such that all the resulting parts would have the same width. For
this, the number n of resulting parts is determined by dividing the width
of the input region by *`Distance`* and rounding the result to the
closest integer value. The distance between the initial split positions is
now calculated by dividing the width of the input region by n. Note that
the distance between these initial split positions is typically not
identical to *`Distance`*. Then, the final split positions are
determined in the neighborhood of the initial split positions such that the
input region is split at positions where it has the least vertical extent
within this neighborhood. The maximum deviation of the final split position
from the initial split position is *`Distance`***`Percent`**0.01.

The resulting regions are returned in *`Partitioned`*. Note that the
input region is only partitioned if its width is larger than 1.5 times
*`Distance`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region to be partitioned.

**`Partitioned`** (output_object)  region-array `→` object

Partitioned region.

**`Distance`** (input_control)  real `→`  (real)

Approximate width of the resulting region parts.

**`Percent`** (input_control)  real `→`  (real)

Maximum percental shift of the split position.

Default:
20

Suggested values:
0.0, 10.0, 20.0, 30.0, 40.0, 50.0, 70.0, 90.0, 100.0

Value range:
`0
≤
Percent
≤
100`

## Result

`partition_dynamic` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty input (no regions given) can
be set via `set_system('no_object_result',<Result>)`,
the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`,
and the behavior in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`

## Alternatives

`partition_rectangle`

## See also

`intersection`,
`smallest_rectangle1`,
`shape_trans`,
`clip_region`

## Module

Foundation
