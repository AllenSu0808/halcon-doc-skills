# hough_lines (Operator)

## Name

`hough_lines` — Detect lines in edge images with the help of the Hough transform and
returns it in HNF.

## Signature

`hough_lines(RegionIn : : AngleResolution, Threshold, AngleGap, DistGap : Angle, Dist)`

## Description

The operator `hough_lines` allows the selection of line-like
structures in a region, whereby it is not necessary that the individual
points of a line are connected. This process is based on the Hough transform.

The parameter *`AngleResolution`* defines the degree of exactness
concerning the determination of the angles. It amounts to 1 /
*`AngleResolution`* degree.
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
short and long lines simultaneously.
The lines are returned in Hessian Normal Form (HNF), that is by the direction
*`Angle`* and length *`Dist`* of their normal vectors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`RegionIn`** (input_object)  region `→` object

Binary edge image in which the lines are to be
detected.

**`AngleResolution`** (input_control)  integer `→`  (integer)

Adjusting the resolution in the angle area.

Default:
4

List of values:
1, 2, 4, 8

**`Threshold`** (input_control)  integer `→`  (integer)

Threshold value in the Hough image.

Default:
100

Value range:
`2
≤
Threshold`

**`AngleGap`** (input_control)  integer `→`  (integer)

Minimal distance of two maxima in the Hough image
(direction: angle).

Default:
5

Value range:
`0
≤
AngleGap`

**`DistGap`** (input_control)  integer `→`  (integer)

Minimal distance of two maxima in the Hough image
(direction: distance).

Default:
5

Value range:
`0
≤
DistGap`

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
