# moments_region_central_invar (Operator)

## Name

`moments_region_central_invar` — Geometric moments of regions.

## Signature

`def moments_region_central_invar(regions: HObject) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def moments_region_central_invar_s(regions: HObject) -> Tuple[float, float, float, float]`

## Description

The operator `moments_region_central_invar` calculates the
moments (*`psi1`*, *`psi2`*, *`psi3`*, *`psi4`*)
that are invariant under translation and general linear transformations.

Calculation: Then the moments $\psi_{i}$ are defined by:
$$\psi_1 = \frac{I_1}{\mu^4} \\\n\\psi_2 = \frac{I_2}{\mu^{10}} \\\n\\psi_3 = \frac{I_3}{\mu^7} \\\n\\psi_4 = \frac{I_4}{\mu^{11}}$$ ![figure](../assets/bc6a38f14337126d.svg)

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

**`psi1`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

**`psi2`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

**`psi3`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

**`psi4`** (output_control)  real(-array) `→` Sequence[float]

Moment of 2nd order.

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `moments_region_central_invar` returns the value 2 (
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
