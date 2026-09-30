# MomentsRegion2ndInvar (Operator)

## Name

`MomentsRegion2ndInvar` — Geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegion2ndInvar(HObject regions, out HTuple m11, out HTuple m20, out HTuple m02)`

`HTuple HRegion.MomentsRegion2ndInvar(out HTuple m20, out HTuple m02)`

`double HRegion.MomentsRegion2ndInvar(out double m20, out double m02)`

## Description

The operator `MomentsRegion2ndInvar` calculates the
scaled moments (*`m20`*, *`m02`*)
and the product of inertia of the axes through the center parallel to the
coordinate axes (*`m11`*).

- **Calculation:** —

  $Z_{0}$ and $S_{0}$ are the coordinates
  of the center of a region R with the area F.
  Then the moments $M_{ij}$ are defined by:

  $$M_{ij} = \frac{1}{F^2} \sum_{(Z,S) \in R} (Z_0 - Z)^i (S_0 - S)^j$$ ![figure](../assets/7f07777bb19b7aa0.svg),

  wherein Z and S run through all pixels of the region
  R.

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

**`m11`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Product of inertia of the axes through the center
parallel to the coordinate axes.

**`m20`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order (line-dependent).

**`m02`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order (column-dependent).

## Complexity

If F is the area of the region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `MomentsRegion2ndInvar` returns the value 2 (
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
