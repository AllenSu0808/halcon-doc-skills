# MomentsRegionCentralInvar (Operator)

## Name

`MomentsRegionCentralInvar` — Geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegionCentralInvar(HObject regions, out HTuple PSI1, out HTuple PSI2, out HTuple PSI3, out HTuple PSI4)`

`HTuple HRegion.MomentsRegionCentralInvar(out HTuple PSI2, out HTuple PSI3, out HTuple PSI4)`

`double HRegion.MomentsRegionCentralInvar(out double PSI2, out double PSI3, out double PSI4)`

## Description

The operator `MomentsRegionCentralInvar` calculates the
moments (*`PSI1`*, *`PSI2`*, *`PSI3`*, *`PSI4`*)
that are invariant under translation and general linear transformations.

Calculation: Then the moments $\psi_{i}$ are defined by:
$$\psi_1 = \frac{I_1}{\mu^4} \\\n\\psi_2 = \frac{I_2}{\mu^{10}} \\\n\\psi_3 = \frac{I_3}{\mu^7} \\\n\\psi_4 = \frac{I_4}{\mu^{11}}$$ ![figure](../assets/bc6a38f14337126d.svg)

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`PSI1`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`PSI2`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`PSI3`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`PSI4`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `MomentsRegionCentralInvar` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`MomentsRegion2nd`

## See also

`EllipticAxis`

## Module

Foundation
