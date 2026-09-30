# gen_contours_skeleton_xld (Operator)

## Name

`gen_contours_skeleton_xld` — Convert a skeleton into XLD contours.

## Signature

`gen_contours_skeleton_xld(Skeleton : Contours : Length, Mode : )`

## Description

`gen_contours_skeleton_xld` converts the input skeleton
(e.g., edges) *`Skeleton`*, which is assumed to contain
mostly one pixel wide regions (see [`skeleton`](skeleton.md)), into XLD
contours.

The algorithm first attempts to transform the regions to contain only line
segments in 8-neighborhood. In a second step, the junction points are
labeled. After this, `gen_contours_skeleton_xld` tries to generate
contours which end in junction or end points, in particular for junction
points of the following configurations (in all four possible
rotations):
1 0 1 1 0 1 1 0 0 1 0 0 0 1 0 0 1 0
0 2 0 0 2 0 0 2 1 0 2 1 0 2 1 1 2 1
0 0 1 1 0 1 0 1 0 1 0 0 0 1 0 0 1 0
where 0 = background, 1 = foreground, and 2 = junction point.

After this, all contours having at least *`Length`* points
are returned.
Since contours are split at junction points, possibly long contours
may be split into several short segments because of short adjacent
lines, even if they are longer than *`Length`* points, if
*`Mode`* = *'filter'* was selected. This can be avoided by setting
*`Mode`* = *'generalize1'*. In this case, the contours are
generated as if the segments shorter than *`Length`* were not
contained in the input region. In order to preserve line segments,
which are split into very short segments by the crossing of short
lines, *`Mode`* = *'generalize2'* can be selected. In this
case, line segments are preserved if they end in two junction
points, even if they are shorter than *`Length`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Skeleton`** (input_object)  region `→` object

Skeleton of which the contours are to be determined.

**`Contours`** (output_object)  xld_cont-array `→` object

Resulting contours.

**`Length`** (input_control)  integer `→`  (integer)

Minimum number of points a contour has to have.

Default:
1

Suggested values:
1, 2, 3, 5, 10, 20

**`Mode`** (input_control)  string `→`  (string)

Contour filter mode.

Default:
'filter'

List of values:
'filter', 'generalize1', 'generalize2'

## Possible Predecessors

`skeleton`

## Possible Successors

`smooth_contours_xld`,
`get_contour_xld`,
`gen_polygons_xld`

## See also

`edges_image`,
`threshold`,
`get_region_contour`

## Module

Foundation
