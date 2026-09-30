# HoughLinesDir (Operator)

## Name

`HoughLinesDir` — Detect lines in edge images with the help of the Hough transform
using local gradient direction and return them in normal form.

## Signature

`static void HOperatorSet.HoughLinesDir(HObject imageDir, out HObject houghImage, out HObject lines, HTuple directionUncertainty, HTuple angleResolution, HTuple smoothing, HTuple filterSize, HTuple threshold, HTuple angleGap, HTuple distGap, HTuple genLines, out HTuple angle, out HTuple dist)`

`HImage HImage.HoughLinesDir(out HRegion lines, int directionUncertainty, int angleResolution, string smoothing, int filterSize, int threshold, int angleGap, int distGap, string genLines, out HTuple angle, out HTuple dist)`

## Description

The operator `HoughLinesDir` selects line-like
structures in a region based on the Hough transform. The individual
points of a line can be unconnected. The region is given by the domain
of *`imageDir`*.

In contrast to [`HoughLines`](hough_lines.md), additionally the edge direction in
*`imageDir`* (e.g., returned by [`SobelDir`](sobel_dir.md) or
[`EdgesImage`](edges_image.md)) is taken into account. This results in a more efficient
computation and in a reduction of the noise in the Hough space.

The parameter *`directionUncertainty`* describes how much the edge
direction of the individual points within a line is allowed to vary. For
example, with *`directionUncertainty`* = *10* a horizontal
line (i.e., edge direction = 0 degrees) may contain points with an edge
direction between -10 and +10 degrees. The higher
*`directionUncertainty`* is chosen, the higher the computation time
will be. For *`directionUncertainty`* = *180*
`HoughLinesDir` shows the same behavior as
[`HoughLines`](hough_lines.md), i.e., the edge direction is ignored.
*`directionUncertainty`* should be chosen at least as high as the
step width of the edge direction stored in *`imageDir`*. The minimum
step width is 2 degrees (defined by the image type 'direction').

The parameter *`angleResolution`* defines how accurately the
angles are determined. The accuracy amounts to 1 /
*`angleResolution`* degrees. A subsequent smoothing of the
Hough space results in an increased stability. The smoothing filter can be
selected by *`smoothing`*, the degree of smoothing by the
parameter *`filterSize`* (see [`MeanImage`](mean_image.md) or
[`GaussImage`](gauss_image.md) for details).
The parameter *`threshold`*
determines by how many points of the original region a line's hypothesis
must at least be supported in order to be selected into the output.
The parameters *`angleGap`* and *`distGap`* define a
neighborhood of the points in the Hough image in order to determine the
local maxima: *`angleGap`* describes the minimum distance of two
maxima in the Hough image in angle direction and *`distGap`* in
distance direction, respectively. Thus, maxima exceeding
*`threshold`* but lying close to an even higher maximum are eliminated.
If multiple maxima in this neighborhood are equally high, all of them are
returned. This elimination can particularly be helpful when searching for
short and long lines simultaneously. Besides the not smoothed Hough image
*`houghImage`*, the lines are returned in Hessian Normal Form (HNF),
that is by the direction *`angle`* and length *`dist`* of their
normal vectors.
If the parameter *`genLines`* is set to *"true"*, additionally
those regions in *`imageDir`* are returned that contributed to the
local maxima in Hough space. They are stored in the parameter
*`lines`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageDir`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (direction)

Image containing the edge direction. The edges are
described by the image domain.

**`houghImage`** (output_object)  image `→` [HImage](HImage.md) (uint2)

Hough transform.

**`lines`** (output_object)  region-array `→` [HRegion](HRegion.md)

Regions of the input image that contributed to the
local maxima.

**`directionUncertainty`** (input_control)  angle.deg `→` [HTuple](HTuple.md) (*int* / long)

Uncertainty of edge direction (in degrees).

Default:
2

Value range:
`2
≤
directionUncertainty
≤
180`

Minimum increment:
2

**`angleResolution`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Resolution in the angle area (in 1/degrees).

Default:
4

List of values:
1, 2, 4, 8

**`smoothing`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Smoothing filter for hough image.

Default:
"mean"

List of values:
"gauss", "mean", "none"

**`filterSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Required smoothing filter size.

Default:
5

List of values:
3, 5, 7, 9, 11

**`threshold`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Threshold value in the Hough image.

Default:
100

Value range:
`1
≤
threshold`

**`angleGap`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum distance of two maxima in the Hough image
(direction: angle).

Default:
5

Value range:
`0
≤
angleGap`

**`distGap`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum distance of two maxima in the Hough image
(direction: distance).

Default:
5

Value range:
`0
≤
distGap`

**`genLines`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Create line regions if *"true"*.

Default:
"true"

List of values:
"false", "true"

**`angle`** (output_control)  hesseline.angle.rad-array `→` [HTuple](HTuple.md) (*double*)

Angles (in radians) of the detected lines' normal
vectors.

Value range:
`-1.5707963
≤
angle
≤
3.1415927`

**`dist`** (output_control)  hesseline.distance-array `→` [HTuple](HTuple.md) (*double*)

Distance of the detected lines from the origin.

Number of elements:
Dist == Angle

Value range:
`0
≤
dist`

## Result

The operator [`HoughLines`](hough_lines.md) returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`EdgesImage`,
`SobelDir`,
`Threshold`,
`NonmaxSuppressionDir`,
`ReduceDomain`,
`Skeleton`

## Possible Successors

`GenRegionHline`,
`SelectMatchingLines`

## See also

`HoughLineTransDir`,
`HoughLineTrans`,
`GenRegionHline`,
`HoughCircles`

## Module

Foundation
