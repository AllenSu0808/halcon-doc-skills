# hough_lines_dir (Operator)

## Name

`hough_lines_dir` — Detect lines in edge images with the help of the Hough transform
using local gradient direction and return them in normal form.

## Signature

`hough_lines_dir(ImageDir : HoughImage, Lines : DirectionUncertainty, AngleResolution, Smoothing, FilterSize, Threshold, AngleGap, DistGap, GenLines : Angle, Dist)`

## Description

The operator `hough_lines_dir` selects line-like
structures in a region based on the Hough transform. The individual
points of a line can be unconnected. The region is given by the domain
of *`ImageDir`*.

In contrast to [`hough_lines`](hough_lines.md), additionally the edge direction in
*`ImageDir`* (e.g., returned by [`sobel_dir`](sobel_dir.md) or
[`edges_image`](edges_image.md)) is taken into account. This results in a more efficient
computation and in a reduction of the noise in the Hough space.

The parameter *`DirectionUncertainty`* describes how much the edge
direction of the individual points within a line is allowed to vary. For
example, with *`DirectionUncertainty`* = *10* a horizontal
line (i.e., edge direction = 0 degrees) may contain points with an edge
direction between -10 and +10 degrees. The higher
*`DirectionUncertainty`* is chosen, the higher the computation time
will be. For *`DirectionUncertainty`* = *180*
`hough_lines_dir` shows the same behavior as
[`hough_lines`](hough_lines.md), i.e., the edge direction is ignored.
*`DirectionUncertainty`* should be chosen at least as high as the
step width of the edge direction stored in *`ImageDir`*. The minimum
step width is 2 degrees (defined by the image type 'direction').

The parameter *`AngleResolution`* defines how accurately the
angles are determined. The accuracy amounts to 1 /
*`AngleResolution`* degrees. A subsequent smoothing of the
Hough space results in an increased stability. The smoothing filter can be
selected by *`Smoothing`*, the degree of smoothing by the
parameter *`FilterSize`* (see [`mean_image`](mean_image.md) or
[`gauss_image`](gauss_image.md) for details).
The parameter *`Threshold`*
determines by how many points of the original region a line's hypothesis
must at least be supported in order to be selected into the output.
The parameters *`AngleGap`* and *`DistGap`* define a
neighborhood of the points in the Hough image in order to determine the
local maxima: *`AngleGap`* describes the minimum distance of two
maxima in the Hough image in angle direction and *`DistGap`* in
distance direction, respectively. Thus, maxima exceeding
*`Threshold`* but lying close to an even higher maximum are eliminated.
If multiple maxima in this neighborhood are equally high, all of them are
returned. This elimination can particularly be helpful when searching for
short and long lines simultaneously. Besides the not smoothed Hough image
*`HoughImage`*, the lines are returned in Hessian Normal Form (HNF),
that is by the direction *`Angle`* and length *`Dist`* of their
normal vectors.
If the parameter *`GenLines`* is set to *'true'*, additionally
those regions in *`ImageDir`* are returned that contributed to the
local maxima in Hough space. They are stored in the parameter
*`Lines`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageDir`** (input_object)  singlechannelimage `→` object (direction)

Image containing the edge direction. The edges are
described by the image domain.

**`HoughImage`** (output_object)  image `→` object (uint2)

Hough transform.

**`Lines`** (output_object)  region-array `→` object

Regions of the input image that contributed to the
local maxima.

**`DirectionUncertainty`** (input_control)  angle.deg `→`  (integer)

Uncertainty of edge direction (in degrees).

Default:
2

Value range:
`2
≤
DirectionUncertainty
≤
180`

Minimum increment:
2

**`AngleResolution`** (input_control)  integer `→`  (integer)

Resolution in the angle area (in 1/degrees).

Default:
4

List of values:
1, 2, 4, 8

**`Smoothing`** (input_control)  string `→`  (string)

Smoothing filter for hough image.

Default:
'mean'

List of values:
'gauss', 'mean', 'none'

**`FilterSize`** (input_control)  integer `→`  (integer)

Required smoothing filter size.

Default:
5

List of values:
3, 5, 7, 9, 11

**`Threshold`** (input_control)  integer `→`  (integer)

Threshold value in the Hough image.

Default:
100

Value range:
`1
≤
Threshold`

**`AngleGap`** (input_control)  integer `→`  (integer)

Minimum distance of two maxima in the Hough image
(direction: angle).

Default:
5

Value range:
`0
≤
AngleGap`

**`DistGap`** (input_control)  integer `→`  (integer)

Minimum distance of two maxima in the Hough image
(direction: distance).

Default:
5

Value range:
`0
≤
DistGap`

**`GenLines`** (input_control)  string `→`  (string)

Create line regions if *'true'*.

Default:
'true'

List of values:
'false', 'true'

**`Angle`** (output_control)  hesseline.angle.rad-array `→`  (real)

Angles (in radians) of the detected lines' normal
vectors.

Value range:
`-1.5707963
≤
Angle
≤
3.1415927`

**`Dist`** (output_control)  hesseline.distance-array `→`  (real)

Distance of the detected lines from the origin.

Number of elements:
Dist == Angle

Value range:
`0
≤
Dist`

## Result

The operator [`hough_lines`](hough_lines.md) returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`edges_image`,
`sobel_dir`,
`threshold`,
`nonmax_suppression_dir`,
`reduce_domain`,
`skeleton`

## Possible Successors

`gen_region_hline`,
`select_matching_lines`

## See also

`hough_line_trans_dir`,
`hough_line_trans`,
`gen_region_hline`,
`hough_circles`

## Module

Foundation
