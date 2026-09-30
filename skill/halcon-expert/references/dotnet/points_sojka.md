# PointsSojka (Operator)

## Name

`PointsSojka` — Find corners using the Sojka operator.

## Signature

`static void HOperatorSet.PointsSojka(HObject image, HTuple maskSize, HTuple sigmaW, HTuple sigmaD, HTuple minGrad, HTuple minApparentness, HTuple minAngle, HTuple subpix, out HTuple row, out HTuple column)`

`void HImage.PointsSojka(int maskSize, HTuple sigmaW, HTuple sigmaD, HTuple minGrad, HTuple minApparentness, double minAngle, string subpix, out HTuple row, out HTuple column)`

`void HImage.PointsSojka(int maskSize, double sigmaW, double sigmaD, double minGrad, double minApparentness, double minAngle, string subpix, out HTuple row, out HTuple column)`

## Description

`PointsSojka` defines a corner as the point of intersection of two
straight, non-collinear gray value edges. To decide whether a point of the
input image *`image`* is a corner or not, a neighborhood of
*`maskSize`* x
*`maskSize`* points is inspected. Only those image regions that are
relevant for the decision are considered. Pixels with a magnitude of the
gradient of less than *`minGrad`* are ignored from the outset.

Furthermore, only those of the remaining points are used that belong to one
of the two gray value edges that form the corner.
For this, the so called Apparentness is calculated,
which is an indicator of the probability that the examined point actually
is a corner point. Essentially, it is determined
by the number of relevant points and their gradients. A point can only be
accepted as a corner when its Apparentness is at least
*`minApparentness`*. Typical values of *`minApparentness`* should
range in the region of a few multiples of *`minGrad`*.

To calculate the Apparentness, each mask point is
weighted according to two criteria:
First, the influence of a mask point is weighted with a Gaussian of size
*`sigmaW`* according to its distance from the possible corner point.
*`sigmaW`* should be roughly between quarter and half of
*`maskSize`* to obtain a reasonable proportion of the size of the
weighting function to the mask size.
Secondly, the distance of the point from the (assumed) ideal gray value edge
is estimated and the point is weighted with a Gaussian of size
*`sigmaD`* according to that distance. I.e., pixels that (due to the
discretization of the input image) lie farther from the ideal gray value
edge have less influence on the result than pixels with a smaller distance.
Typically, it is not necessary to modify the default value *0.75*
of *`sigmaD`* .

As a further criterion, the angle is calculated, by which
the gray value edges change their direction in the corner point. A point can
only be accepted as a corner when this angle is greater than
*`minAngle`*.

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

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / int1 / int2 / uint2 / int4 / real)

Input image.

**`maskSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Required filter size.

Default:
9

List of values:
5, 7, 9, 11, 13

**`sigmaW`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Sigma of the weight function according to the distance
to the corner candidate.

Default:
2.5

Suggested values:
2.0, 2.2, 2.4, 2.5, 2.6, 2.8, 3.0

Restriction:
`2.0 <= SigmaW && SigmaW <= 3.0`

**`sigmaD`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Sigma of the weight function for the distance
to the ideal gray value edge.

Default:
0.75

Suggested values:
0.6, 0.7, 0.75, 0.8, 0.9, 1.0

Restriction:
`0.6 <= SigmaD && SigmaD <= 1.0`

**`minGrad`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Threshold for the magnitude of the gradient.

Default:
30.0

Suggested values:
20.0, 15.0, 30.0, 35.0, 40.0

**`minApparentness`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Threshold for Apparentness.

Default:
90.0

Suggested values:
30.0, 60.0, 90.0, 150.0, 300.0, 600.0, 1500.0

**`minAngle`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Threshold for the direction change in
a corner point (radians).

Default:
0.5

Restriction:
`0.0 <= MinAngle && MinAngle <= pi`

**`subpix`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Subpixel precise calculation of the corner points.

Default:
"false"

List of values:
"false", "true"

**`row`** (output_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the detected corner points.

**`column`** (output_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the detected corner points.

## Result

`PointsSojka` returns 2 (
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
