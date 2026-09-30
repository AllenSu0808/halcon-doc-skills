# intersection_region_contour_xld (Operator)

## Name

`intersection_region_contour_xld` — Intersect a contour with a region.

## Signature

`intersection_region_contour_xld(Region, Contour : ContourIntersection : Mode : )`

## Description

The operator `intersection_region_contour_xld` intersects the contour
*`Contour`* with the region *`Region`* and returns the parts
of the contour that are within the region in *`ContourIntersection`*.

The type of intersection can be specified with *`Mode`*.
The following values are possible:

- ***'lines'* (Default):** —

  In *'lines'* mode, each line segment of the input contour is intersected with
  the region with sub-pixel accuracy.
  This mode is usually slower than *'points'* but more accurate.
  Line segments that are only partially within the region are split into
  multiple segments if necessary.
- ***'points'*:** —

  In *'points'* mode, entire line segments from *`Contour`* are
  tested against the region using their start and end point.
  If both the start and end point of a line segment are within the region,
  that line segment is included in the output.
  This mode is faster than *'lines'* but less accurate, especially if the
  contour is coarsely sampled.
  For example, line segments might leave the region between their start and
  end point, but are still included in the output.
  Further, a line segment might be contained in the region for the most part
  but is not included in the output if the start or end point are
  not in the region.

|  |  |
| --- | --- |
| ![figure](../assets/2690a29251a3132c.svg) | ![figure](../assets/ac4888940d8971f8.svg) |
| ( 1) | ( 2) |

Result for *'lines'* (1) and *'points'* mode (2) when
intersecting a contour with a region (green). The red sections of the
contour will be returned as the result.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Region`** (input_object)  region `→` object

Input region.

**`Contour`** (input_object)  xld_cont-array `→` object

Input contour.

**`ContourIntersection`** (output_object)  xld_cont-array `→` object

Selected part of the input contour.

**`Mode`** (input_control)  string `→`  (string)

Intersection mode.

Default:
'lines'

List of values:
'lines', 'points'

## Possible Predecessors

`threshold`,
`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`gen_contour_region_xld`,
`zero_crossing_sub_pix`,
`threshold_sub_pix`

## Alternatives

`intersection_closed_contours_xld`,
`intersection_closed_polygons_xld`

## See also

`intersection_closed_contours_xld`,
`intersection_closed_polygons_xld`,
`gen_region_contour_xld`

## Module

Foundation
