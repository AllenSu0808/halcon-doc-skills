# moments_region_3rd_invar (Operator)

## Name

`moments_region_3rd_invar` — Geometric moments of regions.

## Signature

`def moments_region_3rd_invar(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def moments_region_3rd_invar_s(regions: HObject) -> Tuple[float, float, float, float]`

## Description

The operator `moments_region_3rd_invar` calculates the
scale-invariant moments (*`m21`*, *`m12`*,
*`m03`*, *`m30`*).

- **Calculation:** —

  Then the moments $M_{ij}$ are defined by:

  $$M_{pq} = \frac{\mu_{pq}}{\mu^{3}}$$ ![figure](../assets/3ee849273baed40d.svg),

  wherein
  $p+q>=2$ and $\mu=\mu_{00}=m_{00}$.

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

**`m21`** (output_control)  real(-array) `→` Sequence[float]

Moment of 3rd order (line-dependent).

**`m12`** (output_control)  real(-array) `→` Sequence[float]

Moment of 3rd order (column-dependent).

**`m03`** (output_control)  real(-array) `→` Sequence[float]

Moment of 3rd order (column-dependent).

**`m30`** (output_control)  real(-array) `→` Sequence[float]

Moment of 3rd order (line-dependent).

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `moments_region_3rd_invar` returns the value 2 (
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
