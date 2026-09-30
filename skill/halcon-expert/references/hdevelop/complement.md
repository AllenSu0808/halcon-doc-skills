# complement (Operator)

## Name

`complement` — Return the complement of a region.

## Signature

`complement(Region : RegionComplement : : )`

## Description

`complement` determines the complement of the input
region(s).

If the system flag *'clip_region'* is *'true'*, which
is the default, the difference of the largest image processed so far
(see [`reset_obj_db`](reset_obj_db.md)) and the input region is returned.

If the system flag *'clip_region'* is *'false'* (see
[`set_system`](set_system.md)), the resulting region would be infinitely large.
To avoid this, the complement is done only virtually by setting
the complement flag of *`Region`* to TRUE. For succeeding
operations the de Morgan laws are applied while calculating results. Using
`complement` with *'clip_region'* set to *'false'* makes
sense only to avoid fringe effects, e.g., if the area of
interest is bigger or smaller than the image. For the latter case, the
clipping would be set explicitly. If there is no reason to use the
operator with *'clip_region'*=*'false'* but you need the flag
for other operations of your program, it is recommended to temporarily set
the system flag to*'true'* and change it back to *'false'*
after applying `complement`. Otherwise, negative regions may result
from succeeding operations.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Input region(s).

**`RegionComplement`** (output_object)  region(-array) `→` object

Complemented regions.

Number of elements:
RegionComplement == Region

## Result

`complement` always returns the value 2 (
H_MSG_TRUE)
. The
behavior in case of empty input (no regions given) can be set via
`set_system('no_object_result',<Result>)`
and the behavior in case of an empty input region via
`set_system('empty_region_result',<Result>)`.
If necessary, an exception is raised.

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`,
`class_ndim_norm`

## Possible Successors

`select_shape`

## See also

`difference`,
`union1`,
`union2`,
`intersection`,
`reset_obj_db`,
`set_system`

## Module

Foundation
