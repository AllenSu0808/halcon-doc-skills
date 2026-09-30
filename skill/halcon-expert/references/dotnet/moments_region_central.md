# MomentsRegionCentral (Operator)

## Name

`MomentsRegionCentral` — Geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegionCentral(HObject regions, out HTuple i1, out HTuple i2, out HTuple i3, out HTuple i4)`

`HTuple HRegion.MomentsRegionCentral(out HTuple i2, out HTuple i3, out HTuple i4)`

`double HRegion.MomentsRegionCentral(out double i2, out double i3, out double i4)`

## Description

The operator `MomentsRegionCentral` calculates the
central moments (*`i1`*, *`i2`*,
*`i3`*, *`i4`*).

Calculation: Then the moments $I_{i}$ are defined by:
$$I_1 = \mu_{20}\mu_{02} - \mu_{11}^2 I_2 = (\mu_{30}\mu_{03} - \mu_{21}\mu_{12})^2 - 4(\mu_{30}\mu_{12} - \mu_{21}\mu_{03})(\mu_{21}\mu_{03} - \mu_{12}^2) I_3 = \mu_{20}(\mu_{21}\mu_{03} - \mu_{12}^2) - \mu_{11}(\mu_{30}\mu_{03} - \mu_{21}\mu_{12}) + \mu_{02}(\mu_{30}\mu_{12} - \mu_{21}^2) I_4 = \mu_{30}\mu_{02} - 6\mu_{30}\mu_{21}\mu_{11}\mu_{02} + 6\mu_{30}\mu_{12}\mu_{02}(2\mu_{11}^2 - \mu_{20}\mu_{02}) + \mu_{30}\mu_{03}(6\mu_{20}\mu_{11}\mu_{02} - 8\mu_{11}) + 9\mu_{21}\mu_{20}\mu_{02} - 18\mu_{21}\mu_{12}\mu_{20}\mu_{11}\mu_{02} + 6\mu_{21}\mu_{03}\mu_{20}(2\mu_{11}^2 - \mu_{20}\mu_{02}) + 9\mu_{12}\mu_{20}\mu_{02} - 6\mu_{12}\mu_{03}\mu_{11}\mu_{20} + \mu_{03}\mu_{20}^3$$ ![figure](../assets/a00f0e13ad0d4e74.svg)

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

**`i1`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`i2`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`i3`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order.

**`i4`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 3rd order.

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `MomentsRegionCentral` returns the value 2 (
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
