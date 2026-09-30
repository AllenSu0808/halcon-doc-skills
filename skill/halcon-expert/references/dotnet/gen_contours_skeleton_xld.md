# GenContoursSkeletonXld (Operator)

## Name

`GenContoursSkeletonXld` — Convert a skeleton into XLD contours.

## Signature

`static void HOperatorSet.GenContoursSkeletonXld(HObject skeleton, out HObject contours, HTuple length, HTuple mode)`

`HXLDCont HRegion.GenContoursSkeletonXld(int length, string mode)`

## Description

`GenContoursSkeletonXld` converts the input skeleton
(e.g., edges) *`skeleton`*, which is assumed to contain
mostly one pixel wide regions (see [`Skeleton`](skeleton.md)), into XLD
contours.

The algorithm first attempts to transform the regions to contain only line
segments in 8-neighborhood. In a second step, the junction points are
labeled. After this, `GenContoursSkeletonXld` tries to generate
contours which end in junction or end points, in particular for junction
points of the following configurations (in all four possible
rotations):
1 0 1 1 0 1 1 0 0 1 0 0 0 1 0 0 1 0
0 2 0 0 2 0 0 2 1 0 2 1 0 2 1 1 2 1
0 0 1 1 0 1 0 1 0 1 0 0 0 1 0 0 1 0
where 0 = background, 1 = foreground, and 2 = junction point.

After this, all contours having at least *`length`* points
are returned.
Since contours are split at junction points, possibly long contours
may be split into several short segments because of short adjacent
lines, even if they are longer than *`length`* points, if
*`mode`* = *"filter"* was selected. This can be avoided by setting
*`mode`* = *"generalize1"*. In this case, the contours are
generated as if the segments shorter than *`length`* were not
contained in the input region. In order to preserve line segments,
which are split into very short segments by the crossing of short
lines, *`mode`* = *"generalize2"* can be selected. In this
case, line segments are preserved if they end in two junction
points, even if they are shorter than *`length`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`skeleton`** (input_object)  region `→` [HRegion](HRegion.md)

Skeleton of which the contours are to be determined.

**`contours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Resulting contours.

**`length`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum number of points a contour has to have.

Default:
1

Suggested values:
1, 2, 3, 5, 10, 20

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Contour filter mode.

Default:
"filter"

List of values:
"filter", "generalize1", "generalize2"

## Possible Predecessors

`Skeleton`

## Possible Successors

`SmoothContoursXld`,
`GetContourXld`,
`GenPolygonsXld`

## See also

`EdgesImage`,
`Threshold`,
`GetRegionContour`

## Module

Foundation
