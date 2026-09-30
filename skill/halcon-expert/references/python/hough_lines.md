# hough_lines (Operator)

## Name

`hough_lines` — Detect lines in edge images with the help of the Hough transform and
returns it in HNF.

## Signature

`def hough_lines(region_in: HObject, angle_resolution: int, threshold: int, angle_gap: int, dist_gap: int) -> Tuple[Sequence[float], Sequence[float]]`

## Description

The operator `hough_lines` allows the selection of line-like
structures in a region, whereby it is not necessary that the individual
points of a line are connected. This process is based on the Hough transform.

The parameter *`angle_resolution`* defines the degree of exactness
concerning the determination of the angles. It amounts to 1 /
*`angle_resolution`* degree.
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
short and long lines simultaneously.
The lines are returned in Hessian Normal Form (HNF), that is by the direction
*`angle`* and length *`dist`* of their normal vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_in`** (input_object)  region `→` HObject

Binary edge image in which the lines are to be
detected.

**`angle_resolution`** (input_control)  integer `→` int

Adjusting the resolution in the angle area.

Default:
4

List of values:
1, 2, 4, 8

**`threshold`** (input_control)  integer `→` int

Threshold value in the Hough image.

Default:
100

Value range:
`2
≤
threshold`

**`angle_gap`** (input_control)  integer `→` int

Minimal distance of two maxima in the Hough image
(direction: angle).

Default:
5

Value range:
`0
≤
angle_gap`

**`dist_gap`** (input_control)  integer `→` int

Minimal distance of two maxima in the Hough image
(direction: distance).

Default:
5

Value range:
`0
≤
dist_gap`

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

The operator `hough_lines` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`threshold`,
`skeleton`

## Possible Successors

`select_matching_lines`

## See also

`hough_line_trans`,
`gen_region_hline`,
`hough_circles`

## Module

Foundation
