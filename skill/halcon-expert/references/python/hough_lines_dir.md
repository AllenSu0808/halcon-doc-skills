# hough_lines_dir (Operator)

## Name

`hough_lines_dir` — Detect lines in edge images with the help of the Hough transform
using local gradient direction and return them in normal form.

## Signature

`def hough_lines_dir(image_dir: HObject, direction_uncertainty: int, angle_resolution: int, smoothing: str, filter_size: int, threshold: int, angle_gap: int, dist_gap: int, gen_lines: str) -> Tuple[HObject, HObject, Sequence[float], Sequence[float]]`

## Description

The operator `hough_lines_dir` selects line-like
structures in a region based on the Hough transform. The individual
points of a line can be unconnected. The region is given by the domain
of *`image_dir`*.

In contrast to [`hough_lines`](hough_lines.md), additionally the edge direction in
*`image_dir`* (e.g., returned by [`sobel_dir`](sobel_dir.md) or
[`edges_image`](edges_image.md)) is taken into account. This results in a more efficient
computation and in a reduction of the noise in the Hough space.

The parameter *`direction_uncertainty`* describes how much the edge
direction of the individual points within a line is allowed to vary. For
example, with *`direction_uncertainty`* = *10* a horizontal
line (i.e., edge direction = 0 degrees) may contain points with an edge
direction between -10 and +10 degrees. The higher
*`direction_uncertainty`* is chosen, the higher the computation time
will be. For *`direction_uncertainty`* = *180*
`hough_lines_dir` shows the same behavior as
[`hough_lines`](hough_lines.md), i.e., the edge direction is ignored.
*`direction_uncertainty`* should be chosen at least as high as the
step width of the edge direction stored in *`image_dir`*. The minimum
step width is 2 degrees (defined by the image type 'direction').

The parameter *`angle_resolution`* defines how accurately the
angles are determined. The accuracy amounts to 1 /
*`angle_resolution`* degrees. A subsequent smoothing of the
Hough space results in an increased stability. The smoothing filter can be
selected by *`smoothing`*, the degree of smoothing by the
parameter *`filter_size`* (see [`mean_image`](mean_image.md) or
[`gauss_image`](gauss_image.md) for details).
The parameter *`threshold`*
determines by how many points of the original region a line's hypothesis
must at least be supported in order to be selected into the output.
The parameters *`angle_gap`* and *`dist_gap`* define a
neighborhood of the points in the Hough image in order to determine the
local maxima: *`angle_gap`* describes the minimum distance of two
maxima in the Hough image in angle direction and *`dist_gap`* in
distance direction, respectively. Thus, maxima exceeding
*`threshold`* but lying close to an even higher maximum are eliminated.
If multiple maxima in this neighborhood are equally high, all of them are
returned. This elimination can particularly be helpful when searching for
short and long lines simultaneously. Besides the not smoothed Hough image
*`hough_image`*, the lines are returned in Hessian Normal Form (HNF),
that is by the direction *`angle`* and length *`dist`* of their
normal vectors.
If the parameter *`gen_lines`* is set to *"true"*, additionally
those regions in *`image_dir`* are returned that contributed to the
local maxima in Hough space. They are stored in the parameter
*`lines`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_dir`** (input_object)  singlechannelimage `→` HObject (direction)

Image containing the edge direction. The edges are
described by the image domain.

**`hough_image`** (output_object)  image `→` HObject (uint2)

Hough transform.

**`lines`** (output_object)  region-array `→` HObject

Regions of the input image that contributed to the
local maxima.

**`direction_uncertainty`** (input_control)  angle.deg `→` int

Uncertainty of edge direction (in degrees).

Default:
2

Value range:
`2
≤
direction_uncertainty
≤
180`

Minimum increment:
2

**`angle_resolution`** (input_control)  integer `→` int

Resolution in the angle area (in 1/degrees).

Default:
4

List of values:
1, 2, 4, 8

**`smoothing`** (input_control)  string `→` str

Smoothing filter for hough image.

Default:
"mean"

List of values:
"gauss", "mean", "none"

**`filter_size`** (input_control)  integer `→` int

Required smoothing filter size.

Default:
5

List of values:
3, 5, 7, 9, 11

**`threshold`** (input_control)  integer `→` int

Threshold value in the Hough image.

Default:
100

Value range:
`1
≤
threshold`

**`angle_gap`** (input_control)  integer `→` int

Minimum distance of two maxima in the Hough image
(direction: angle).

Default:
5

Value range:
`0
≤
angle_gap`

**`dist_gap`** (input_control)  integer `→` int

Minimum distance of two maxima in the Hough image
(direction: distance).

Default:
5

Value range:
`0
≤
dist_gap`

**`gen_lines`** (input_control)  string `→` str

Create line regions if *"true"*.

Default:
"true"

List of values:
"false", "true"

**`angle`** (output_control)  hesseline.angle.rad-array `→` Sequence[float]

Angles (in radians) of the detected lines' normal
vectors.

Value range:
`-1.5707963
≤
angle
≤
3.1415927`

**`dist`** (output_control)  hesseline.distance-array `→` Sequence[float]

Distance of the detected lines from the origin.

Number of elements:
Dist == Angle

Value range:
`0
≤
dist`

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
