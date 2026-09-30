# MomentsRegion2ndRelInvar (Operator)

## Name

`MomentsRegion2ndRelInvar` — Geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegion2ndRelInvar(HObject regions, out HTuple PHI1, out HTuple PHI2)`

`HTuple HRegion.MomentsRegion2ndRelInvar(out HTuple PHI2)`

`double HRegion.MomentsRegion2ndRelInvar(out double PHI2)`

## Description

The operator `MomentsRegion2ndRelInvar` calculates the
scaled relative moments (*`PHI1`*, *`PHI2`*).

- **Calculation:** —

  The moments PHI1 and PHI2 are defined by:
  $$PHI_{1}=M_{20}+M_{02}PHI_{2}=(M_{20}-M_{02})^{2}+4M_{11}^{2}$$

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

**`PHI1`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`PHI2`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

## Result

The operator `MomentsRegion2ndRelInvar` returns the value 2 (
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
