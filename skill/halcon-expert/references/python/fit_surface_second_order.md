# fit_surface_second_order (Operator)

## Name

`fit_surface_second_order` — Calculate gray value moments and approximation by a second order surface.

## Signature

`def fit_surface_second_order(regions: HObject, image: HObject, algorithm: str, iterations: int, clipping_factor: float) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def fit_surface_second_order_s(regions: HObject, image: HObject, algorithm: str, iterations: int, clipping_factor: float) -> Tuple[float, float, float, float, float, float]`

## Description

The operator `fit_surface_second_order` calculates the gray value
moments and the parameters of the approximation of the gray values
by a second order surface. The calculation is done by minimizing the
distance between the gray values and the surface. A second order surface is
described by the following formula:

$$Image(r,c) = Alpha(r - r_center)^2 \\ + Beta(c - c_center)^2 \\ + Gamma(r - r_center)*(c - c_center) \\ + Delta(r - r_center) \\ + Epsilon(c - c_center) \\ + Zeta$$ ![figure](../assets/85d2e2a3b308eb9e.svg)
$r_{center}$ and $c_{center}$ are the center
coordinates of the intersection of the input region with the full image
domain.
By the minimization process the parameters from *`alpha`* to
*`zeta`* is calculated.

The algorithm used for the fitting can be selected via
*`algorithm`*:

- ***"regression"*** —

  Standard 'least squares' fitting.
- ***"huber"*** —

  Weighted 'least squares' fitting, where the impact of outliers
  is decreased based on the approach of Huber.
- ***"tukey"*** —

  Weighted 'least squares' fitting, where outliers
  are ignored based on the approach of Tukey.

The parameter *`clipping_factor`* (a scaling factor for the standard
deviation) controls the amount of damping outliers: The smaller the
value chosen for *`clipping_factor`* the more outliers are
detected. The detection of outliers is repeated. The parameter
*`iterations`* specifies the number of iterations. If
*"regression"* is set for *`algorithm`* *`iterations`*
is ignored.

## Attention

Note that the operator `fit_surface_second_order` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions to be checked.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / direction / cyclic / real)

Corresponding gray values.

**`algorithm`** (input_control)  string `→` str

Algorithm for the fitting.

Default:
"regression"

List of values:
"huber", "regression", "tukey"

**`iterations`** (input_control)  integer `→` int

Maximum number of iterations (unused for 'regression').

Default:
5

Restriction:
`Iterations >= 0`

**`clipping_factor`** (input_control)  real `→` float

Clipping factor for the elimination of outliers.

Default:
2.0

List of values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`alpha`** (output_control)  real(-array) `→` Sequence[float]

Parameter Alpha of the approximating surface.

**`beta`** (output_control)  real(-array) `→` Sequence[float]

Parameter Beta of the approximating surface.

**`gamma`** (output_control)  real(-array) `→` Sequence[float]

Parameter Gamma of the approximating surface.

**`delta`** (output_control)  real(-array) `→` Sequence[float]

Parameter Delta of the approximating surface.

**`epsilon`** (output_control)  real(-array) `→` Sequence[float]

Parameter Epsilon of the approximating surface.

**`zeta`** (output_control)  real(-array) `→` Sequence[float]

Parameter Zeta of the approximating surface.

## Result

The operator `fit_surface_second_order` returns the
value 2 (
H_MSG_TRUE)
if an
image with the defined gray values (byte) is entered and
the parameters are correct.
If necessary an exception is raised.

## Possible Successors

`gen_image_surface_second_order`

## See also

`moments_gray_plane`,
`fit_surface_first_order`

## Module

Foundation
