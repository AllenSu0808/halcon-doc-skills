# moments_region_2nd_rel_invar (Operator)

## Name

`moments_region_2nd_rel_invar` — Geometric moments of regions.

## Signature

`def moments_region_2nd_rel_invar(regions: HObject) -> Tuple[Sequence[float], Sequence[float]]`

`def moments_region_2nd_rel_invar_s(regions: HObject) -> Tuple[float, float]`

## Description

The operator `moments_region_2nd_rel_invar` calculates the
scaled relative moments (*`phi1`*, *`phi2`*).

- **Calculation:** —

  The moments PHI1 and PHI2 are defined by:
  $$PHI_{1}=M_{20}+M_{02}PHI_{2}=(M_{20}-M_{02})^{2}+4M_{11}^{2}$$

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be examined.

**`phi1`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

**`phi2`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

## Result

The operator `moments_region_2nd_rel_invar` returns the value 2 (
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

## Alternatives

`moments_region_2nd`

## See also

`elliptic_axis`

## Module

Foundation
