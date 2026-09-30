# Complement (Operator)

## Name

`Complement` — Return the complement of a region.

## Signature

`static void HOperatorSet.Complement(HObject region, out HObject regionComplement)`

`HRegion HRegion.Complement()`

## Description

`Complement` determines the complement of the input
region(s).

If the system flag *"clip_region"* is *"true"*, which
is the default, the difference of the largest image processed so far
(see [`ResetObjDb`](reset_obj_db.md)) and the input region is returned.

If the system flag *"clip_region"* is *"false"* (see
[`SetSystem`](set_system.md)), the resulting region would be infinitely large.
To avoid this, the complement is done only virtually by setting
the complement flag of *`region`* to TRUE. For succeeding
operations the de Morgan laws are applied while calculating results. Using
`Complement` with *"clip_region"* set to *"false"* makes
sense only to avoid fringe effects, e.g., if the area of
interest is bigger or smaller than the image. For the latter case, the
clipping would be set explicitly. If there is no reason to use the
operator with *"clip_region"*=*"false"* but you need the flag
for other operations of your program, it is recommended to temporarily set
the system flag to*"true"* and change it back to *"false"*
after applying `Complement`. Otherwise, negative regions may result
from succeeding operations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region(s).

**`regionComplement`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Complemented regions.

Number of elements:
RegionComplement == Region

## Result

`Complement` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`,
`ClassNdimNorm`

## Possible Successors

`SelectShape`

## See also

`Difference`,
`Union1`,
`Union2`,
`Intersection`,
`ResetObjDb`,
`SetSystem`

## Module

Foundation
