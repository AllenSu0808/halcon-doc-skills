# fit_surface_first_order (Operator)

## Name

`fit_surface_first_order` — Calculate gray value moments and approximation by a first order surface
(plane).

## Signature

`fit_surface_first_order(Regions, Image : : Algorithm, Iterations, ClippingFactor : Alpha, Beta, Gamma)`

## Description

The operator `fit_surface_first_order` calculates the gray value
moments and the parameters of the approximation of the gray values
by a first order surface. The calculation is done by minimizing the
distance between the gray values and the surface. A first order surface is
described by the following formula:

$$Image(r,c) = Alpha(r - r_{center}) + Beta(c - c_{center}) + Gamma$$ ![figure](../assets/681fced13f7f11b2.svg)
$r_{center}$ and $c_{center}$ are the center
coordinates of intersection of the input region with the full image domain.
By the minimization process the parameters from *`Alpha`* to
*`Gamma`* is calculated.

The algorithm used for the fitting can be selected via
*`Algorithm`*:

- **'regression'** —

  Standard 'least squares' line fitting.
- **'huber'** —

  Weighted 'least squares' fitting, where the impact of outliers
  is decreased based on the approach of Huber.
- **'tukey'** —

  Weighted 'least squares' fitting, where outliers
  are ignored based on the approach of Tukey.

The parameter *`ClippingFactor`* (a scaling factor for the standard
deviation) controls the amount of damping outliers: The smaller the
value chosen for *`ClippingFactor`* the more outliers are
detected. The detection of outliers is repeated. The parameter
*`Iterations`* specifies the number of iterations. If
*'regression'* is set for *`Algorithm`* *`Iterations`*
is ignored.

## Attention

Note that the operator `fit_surface_first_order` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions to be checked.

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2 / direction / cyclic / real)

Corresponding gray values.

**`Algorithm`** (input_control)  string `→`  (string)

Algorithm for the fitting.

Default:
'regression'

List of values:
'huber', 'regression', 'tukey'

**`Iterations`** (input_control)  integer `→`  (integer)

Maximum number of iterations (unused for 'regression').

Default:
5

Restriction:
`Iterations >= 0`

**`ClippingFactor`** (input_control)  real `→`  (real)

Clipping factor for the elimination of outliers.

Default:
2.0

List of values:
1.0, 1.5, 2.0, 2.5, 3.0

Restriction:
`ClippingFactor > 0`

**`Alpha`** (output_control)  real(-array) `→`  (real)

Parameter Alpha of the approximating surface.

**`Beta`** (output_control)  real(-array) `→`  (real)

Parameter Beta of the approximating surface.

**`Gamma`** (output_control)  real(-array) `→`  (real)

Parameter Gamma of the approximating surface.

## Result

The operator `fit_surface_first_order` returns the
value 2 (
H_MSG_TRUE)
if an
image with the defined gray values (byte) is entered and
the parameters are correct.
If necessary an exception is raised.

## Possible Successors

`gen_image_surface_first_order`

## See also

`moments_gray_plane`,
`fit_surface_second_order`

## Module

Foundation
