# moments_region_2nd (Operator)

## Name

`moments_region_2nd` — Calculate the geometric moments of regions.

## Signature

`moments_region_2nd(Regions : : : M11, M20, M02, Ia, Ib)`

## Description

`moments_region_2nd` calculates the geometric
moments *`M11`*, *`M20`* and *`M02`* of the input
regions in *`Regions`*. Furthermore the major and minor axis
of the input regions are calculated and returned in *`Ia`*
and *`Ib`*.

The covariance matrix is given by:
$$\begin{bmatrix}M_{20} & M_{11}\\ M_{11} & M_{02}\end{bmatrix}$$ ![figure](../assets/04361c80813cda48.svg)

The row-dependent moment of 2nd order is returned in *`M20`*
and the column-dependent moment of 2nd order is returned in *`M02`*.
The moment *`M11`* represents the covariance between
the row and column coordinates of the region points.

- **Calculation:** —

  $r_{0}$ and $c_{0}$ are the coordinates
  of the center of gravity of a region R.
  Then the moments $M_{ij}$ are defined by:

  $$M_{ij} = \sum_{(r,c) \in R} (r_{0} - r)^{i} (c_{0} - c)^{j}$$ ![figure](../assets/a2a8f0fc70ba0d67.svg)

  wherein r and c run over all pixels of the region R.

  Furthermore the length of the major and minor axes are defined by:

  $$I_a = h + \sqrt{h^2 - M20 * M02 + M12^2}$$ ![figure](../assets/99a69ee1ff7c76b7.svg)
  $$Ib = h - \sqrt{h^2 - M20 * M02 + M112}$$ ![figure](../assets/23a8f8a218ad00df.svg)

  wherein $h$ is defined by:

  $$h = \frac{M20 + M02}{2}$$ ![figure](../assets/0436b2a7996687cc.svg)

The equation for the major and minor axes can be derived from the definition
of the moments by diagonalizing the covariance matrix and reforming the resulting
formula.

If more than one region is passed, the results are returned in tuples.
The index of a tuple element corresponds to the index of the respective
input region.

If an empty region is passed, 0.0 is returned for all parameters, if no other
behavior was set (see [`set_system`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Input regions.

**`M11`** (output_control)  real(-array) `→`  (real)

Product of inertia of the axes through the center
parallel to the coordinate axes.

**`M20`** (output_control)  real(-array) `→`  (real)

Moment of 2nd order (row-dependent).

**`M02`** (output_control)  real(-array) `→`  (real)

Moment of 2nd order (column-dependent).

**`Ia`** (output_control)  real(-array) `→`  (real)

Length of the major axis of the input region.

**`Ib`** (output_control)  real(-array) `→`  (real)

Length of the minor axis of the input region.

## Complexity

If F is the area of the region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `moments_region_2nd` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`connection`

## Alternatives

`moments_region_2nd_invar`

## See also

`elliptic_axis`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 73-75

## Module

Foundation
