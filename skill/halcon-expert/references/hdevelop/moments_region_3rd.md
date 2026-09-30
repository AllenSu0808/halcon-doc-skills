# moments_region_3rd (Operator)

## Name

`moments_region_3rd` — Geometric moments of regions.

## Signature

`moments_region_3rd(Regions : : : M21, M12, M03, M30)`

## Description

The operator `moments_region_3rd` calculates the
translation-invariant central moments (*`M21`*, *`M12`*,
*`M03`*, *`M30`*) of order p+q.

- **Calculation:** —

  x and y are the coordinates
  of the center of a region R with the area Z.

  Then the moments $M_{pq}$ are defined by:

  $$M_{pq} = \sum_{i=1}^{M} M Z(x_i, y_i) (x_i - x)^p (y_i - y)^q$$ ![figure](../assets/7ca71497cafff200.svg),

  wherein are $$x = \frac{m_{10}}{m_{00}} \\text{ and } y = \frac{m_{01}}{m_{00}}$$ ![figure](../assets/b2ea43508a7598b2.svg).

If more than one region is passed the results are stored in tuples, the index
of a value in the tuple corresponding to the index of a region in the input.

In case of empty region all parameters have the value 0.0 if no other
behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be examined.

**`M21`** (output_control)  real(-array) `→`  (real)

Moment of 3rd order (line-dependent).

**`M12`** (output_control)  real(-array) `→`  (real)

Moment of 3rd order (column-dependent).

**`M03`** (output_control)  real(-array) `→`  (real)

Moment of 3rd order (column-dependent).

**`M30`** (output_control)  real(-array) `→`  (real)

Moment of 3rd order (line-dependent).

## Complexity

If Z is the area of the region the mean runtime
complexity is O(sqrt(Z)).

## Result

The operator `moments_region_3rd` returns the value 2 (
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
