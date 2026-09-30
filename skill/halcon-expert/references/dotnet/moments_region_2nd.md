# MomentsRegion2nd (Operator)

## Name

`MomentsRegion2nd` — Calculate the geometric moments of regions.

## Signature

`static void HOperatorSet.MomentsRegion2nd(HObject regions, out HTuple m11, out HTuple m20, out HTuple m02, out HTuple ia, out HTuple ib)`

`HTuple HRegion.MomentsRegion2nd(out HTuple m20, out HTuple m02, out HTuple ia, out HTuple ib)`

`double HRegion.MomentsRegion2nd(out double m20, out double m02, out double ia, out double ib)`

## Description

`MomentsRegion2nd` calculates the geometric
moments *`m11`*, *`m20`* and *`m02`* of the input
regions in *`regions`*. Furthermore the major and minor axis
of the input regions are calculated and returned in *`ia`*
and *`ib`*.

The covariance matrix is given by:
$$\begin{bmatrix}M_{20} & M_{11}\\ M_{11} & M_{02}\end{bmatrix}$$ ![figure](../assets/04361c80813cda48.svg)

The row-dependent moment of 2nd order is returned in *`m20`*
and the column-dependent moment of 2nd order is returned in *`m02`*.
The moment *`m11`* represents the covariance between
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
behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions.

**`m11`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Product of inertia of the axes through the center
parallel to the coordinate axes.

**`m20`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order (row-dependent).

**`m02`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Moment of 2nd order (column-dependent).

**`ia`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the major axis of the input region.

**`ib`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Length of the minor axis of the input region.

## Complexity

If F is the area of the region the mean runtime
complexity is O(sqrt(F)).

## Result

The operator `MomentsRegion2nd` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
The behavior in case of empty region (region is the empty set) is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`

## Alternatives

`MomentsRegion2ndInvar`

## See also

`EllipticAxis`

## References

R. Haralick, L. Shapiro
“Computer and Robot Vision”
Addison-Wesley, 1992, pp. 73-75

## Module

Foundation
