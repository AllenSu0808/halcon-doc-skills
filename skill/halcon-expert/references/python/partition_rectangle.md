# partition_rectangle (Operator)

## Name

`partition_rectangle` — Partition a region into rectangles of approximately equal size.

## Signature

`def partition_rectangle(region: HObject, width: float, height: float) -> HObject`

## Description

`partition_rectangle` partitions the input region into
rectangles having an extent of *`width`* times
*`height`*. The rectangles are returned in *`partitioned`*.
The region is always split into rectangles of
approximately equal size. If this is not possible with the requested
rectangle size, then *`width`* and *`height`* are adapted so that
the size of the resulting rectangles is approximately equal. If the region is
smaller than the given size, its output remains unchanged. A partition is
only done if the size of the region is at least 1.5 times the size of the
rectangle given by the parameters.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region to be partitioned.

**`partitioned`** (output_object)  region(-array) `→` HObject

Partitioned region.

**`width`** (input_control)  extent.x `→` float

Width of the individual rectangles.

**`height`** (input_control)  extent.y `→` float

Height of the individual rectangles.

## Result

`partition_rectangle` returns 2 (
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

`partition_dynamic`

## See also

`intersection`,
`smallest_rectangle1`,
`shape_trans`,
`clip_region`

## Module

Foundation
