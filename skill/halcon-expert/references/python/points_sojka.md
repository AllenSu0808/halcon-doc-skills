# points_sojka (Operator)

## Name

`points_sojka` — Find corners using the Sojka operator.

## Signature

`def points_sojka(image: HObject, mask_size: int, sigma_w: Union[float, int], sigma_d: Union[float, int], min_grad: Union[int, float], min_apparentness: Union[int, float], min_angle: float, subpix: str) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`points_sojka` defines a corner as the point of intersection of two
straight, non-collinear gray value edges. To decide whether a point of the
input image *`image`* is a corner or not, a neighborhood of
*`mask_size`* x
*`mask_size`* points is inspected. Only those image regions that are
relevant for the decision are considered. Pixels with a magnitude of the
gradient of less than *`min_grad`* are ignored from the outset.

Furthermore, only those of the remaining points are used that belong to one
of the two gray value edges that form the corner.
For this, the so called Apparentness is calculated,
which is an indicator of the probability that the examined point actually
is a corner point. Essentially, it is determined
by the number of relevant points and their gradients. A point can only be
accepted as a corner when its Apparentness is at least
*`min_apparentness`*. Typical values of *`min_apparentness`* should
range in the region of a few multiples of *`min_grad`*.

To calculate the Apparentness, each mask point is
weighted according to two criteria:
First, the influence of a mask point is weighted with a Gaussian of size
*`sigma_w`* according to its distance from the possible corner point.
*`sigma_w`* should be roughly between quarter and half of
*`mask_size`* to obtain a reasonable proportion of the size of the
weighting function to the mask size.
Secondly, the distance of the point from the (assumed) ideal gray value edge
is estimated and the point is weighted with a Gaussian of size
*`sigma_d`* according to that distance. I.e., pixels that (due to the
discretization of the input image) lie farther from the ideal gray value
edge have less influence on the result than pixels with a smaller distance.
Typically, it is not necessary to modify the default value *0.75*
of *`sigma_d`* .

As a further criterion, the angle is calculated, by which
the gray value edges change their direction in the corner point. A point can
only be accepted as a corner when this angle is greater than
*`min_angle`*.

The position of the detected corner points is returned in
(*`row`*, *`column`*). *`row`* and *`column`* are calculated
with subpixel accuracy if *`subpix`* is *"true"*. They are
calculated only with pixel accuracy if *`subpix`* is
*"false"*.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`mask_size`** (input_control)  integer `→` int

Required filter size.

Default:
9

List of values:
5, 7, 9, 11, 13

**`sigma_w`** (input_control)  number `→` Union[float, int]

Sigma of the weight function according to the distance
to the corner candidate.

Default:
2.5

Suggested values:
2.0, 2.2, 2.4, 2.5, 2.6, 2.8, 3.0

Restriction:
`2.0 <= SigmaW && SigmaW <= 3.0`

**`sigma_d`** (input_control)  number `→` Union[float, int]

Sigma of the weight function for the distance
to the ideal gray value edge.

Default:
0.75

Suggested values:
0.6, 0.7, 0.75, 0.8, 0.9, 1.0

Restriction:
`0.6 <= SigmaD && SigmaD <= 1.0`

**`min_grad`** (input_control)  number `→` Union[int, float]

Threshold for the magnitude of the gradient.

Default:
30.0

Suggested values:
20.0, 15.0, 30.0, 35.0, 40.0

**`min_apparentness`** (input_control)  number `→` Union[int, float]

Threshold for Apparentness.

Default:
90.0

Suggested values:
30.0, 60.0, 90.0, 150.0, 300.0, 600.0, 1500.0

**`min_angle`** (input_control)  angle.rad `→` float

Threshold for the direction change in
a corner point (radians).

Default:
0.5

Restriction:
`0.0 <= MinAngle && MinAngle <= pi`

**`subpix`** (input_control)  string `→` str

Subpixel precise calculation of the corner points.

Default:
"false"

List of values:
"false", "true"

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinates of the detected corner points.

**`column`** (output_control)  point.x-array `→` Sequence[float]

Column coordinates of the detected corner points.

## Result

`points_sojka` returns 2 (
H_MSG_TRUE)
if all parameters are correct and
no error occurs during the execution. If the input is empty the
behavior can be set via
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## References

Eduard Sojka: “A New and Efficient Algorithm for Detecting the
Corners in Digital Images”. Pattern Recognition, Luc Van Gool
(Editor), LNCS 2449, pp. 125-132, Springer Verlag, 2002.

## Module

Foundation
