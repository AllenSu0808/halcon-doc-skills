# MomentsRegion3rd (Operator)

## Name

`MomentsRegion3rd` — Geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegion3rd(HObject regions, out HTuple m21, out HTuple m12, out HTuple m03, out HTuple m30)`

`HTuple HRegion.MomentsRegion3rd(out HTuple m12, out HTuple m03, out HTuple m30)`

`double HRegion.MomentsRegion3rd(out double m12, out double m03, out double m30)`

## Description

The operator `MomentsRegion3rd` calculates the
translation-invariant central moments (*`m21`*, *`m12`*,
*`m03`*, *`m30`*) of order p+q.

- **Calculation:** —

  x and y are the coordinates
  of the center of a region R with the area Z.

  Then the moments $M_{pq}$ are defined by:

  $$M_{pq} = \sum_{i=1}^{M} M Z(x_i, y_i) (x_i - x)^p (y_i - y)^q$$ ![figure](../assets/7ca71497cafff200.svg),

  wherein are $$x = \frac{m_{10}}{m_{00}} \\text{ and } y = \frac{m_{01}}{m_{00}}$$ ![figure](../assets/b2ea43508a7598b2.svg).

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

**`m21`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 3rd order (line-dependent).

**`m12`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 3rd order (column-dependent).

**`m03`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 3rd order (column-dependent).

**`m30`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 3rd order (line-dependent).

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `MomentsRegion3rd` returns the value 2 (
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
