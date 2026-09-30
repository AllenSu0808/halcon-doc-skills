# connect_grid_points (Operator)

## Name

`connect_grid_points` — Establish connections between the grid points of the rectification grid.

## Signature

`def connect_grid_points(image: HObject, row: Sequence[float], column: Sequence[float], sigma: MaybeSequence[Union[float, int]], max_dist: Union[float, int]) -> HObject`

## Description

`connect_grid_points` searches for connecting lines between the grid
points (*`row`*,*`column`*) of the rectification grid. The
connecting lines are extracted from the input image *`image`* by a
combination of an edge detector, a smoothing filter, and a line detector,
each of size $\sigma$.
The $\sigma$ to be used is determined as follows:
When a single value is passed in *`sigma`*, this value is used.
When a tuple of three values (*"sigma_min"*, *"sigma_max"*,
*"sigma_step"*) is passed, `connect_grid_points` tests every
$\sigma$ within a range from *"sigma_min"* to
*"sigma_max"* with a step width of *"sigma_step"* and chooses the
$\sigma$ that causes the greatest number of connecting lines.
The same happens when a tuple of only two values *"sigma_min"* and
*"sigma_max"* is passed. However, in this case a fixed step width of
*0.05* is used.

Then, the extracted connecting lines are split at the grid
points and those line segments are selected that start as well as end at a
grid point. Note that edge detectors typically don't work very accurately
in the proximity of edge junctions, and thus in general the connecting lines
will not hit the grid points. Therefore, actually those connecting lines are
split and selected that start at, end at, or pass a grid point at a maximum
distance of *`max_dist`*. The connecting lines are modified in order to
start and end exactly in the corresponding grid points, and
are returned in *`connecting_lines`* as XLD contours.

Additionally, `connect_grid_points` calculates for each output XLD
contour its type of transition and stores it in its global attribute
*"bright_dark"*. The attribute is set to *1.0*, if the
connecting line forms a bright-dark transition (left to right, viewed from
start point to end point), otherwise it is set to *0.0*. For further
information about global contour attributes see
[`get_contour_global_attrib_xld`](get_contour_global_attrib_xld.md).

## Attention

For a reliable determination of the type of bright-dark transition as well
as for the following rectification, it is necessary that each connecting
line has at least three contour points. Therefore, connecting lines with
only two contour points are not returned. Note, that the parameter
*`max_dist`* has a substantial influence on the length of the returned
connecting lines, because all contour points of a possible connecting
line that are closer than *`max_dist`* to a grid point are replaced by
one single contour point. If *`max_dist`* is too big, some of the
connecting lines might get lost.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image.

**`connecting_lines`** (output_object)  xld-array `→` HObject

Output contours.

**`row`** (input_control)  point.y-array `→` Sequence[float]

Row coordinates of the grid points.

**`column`** (input_control)  point.x-array `→` Sequence[float]

Column coordinates of the grid points.

Restriction:
`number(Column) == number(Row)`

**`sigma`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Size of the applied Gaussians.

Number of elements:
1 <= Sigma && Sigma <= 3

Default:
0.9

Suggested values:
0.7, 0.9, 1.1, 1.3, 1.5

Restriction:
`0.7 <= Sigma`

**`max_dist`** (input_control)  number `→` Union[float, int]

Maximum distance of the connecting lines from the
grid points.

Default:
5.5

Suggested values:
1.5, 3.5, 5.5, 7.5, 9.5

Restriction:
`0.0 <= MaxDist`

## Result

`connect_grid_points` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`saddle_points_sub_pix`

## Possible Successors

`gen_grid_rectification_map`

## Module

Calibration
