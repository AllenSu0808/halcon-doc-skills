# PartitionRectangle (Operator)

## Name

`PartitionRectangle` — Partition a region into rectangles of approximately equal size.

## Signature

`static void HOperatorSet.PartitionRectangle(HObject region, out HObject partitioned, HTuple width, HTuple height)`

`HRegion HRegion.PartitionRectangle(double width, double height)`

## Description

`PartitionRectangle` partitions the input region into
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

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region to be partitioned.

**`partitioned`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Partitioned region.

**`width`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*double*)

Width of the individual rectangles.

**`height`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*double*)

Height of the individual rectangles.

## Result

`PartitionRectangle` returns 2 (
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

`Threshold`,
`Connection`

## Alternatives

`PartitionDynamic`

## See also

`Intersection`,
`SmallestRectangle1`,
`ShapeTrans`,
`ClipRegion`

## Module

Foundation
