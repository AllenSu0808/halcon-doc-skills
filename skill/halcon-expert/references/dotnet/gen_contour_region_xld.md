# GenContourRegionXld (Operator)

## Name

`GenContourRegionXld` — Generate XLD contours from regions.

## Signature

`static void HOperatorSet.GenContourRegionXld(HObject regions, out HObject contours, HTuple mode)`

`HXLDCont HRegion.GenContourRegionXld(string mode)`

`public HXLDCont(HRegion regions, string mode)`

## Description

`GenContourRegionXld` generates XLD contours
*`contours`* from the regions given in *`regions`*. This
operator is useful if regions have been obtained from segmentation
operations, but higher level operators, e.g., polygon approximation
and extraction of parallels, are to be performed on their
boundaries. For each connected component of the input regions a
closed contour of the boundary is generated. The parameter
*`mode`* can take on the following values:

- *"center"*: The centers of the border pixels are used
  as contour points.
- *"border"*: The outer border of the border pixels is
  used as contour points.
- *"border_holes"*: In addition to the outer border of the
  input region you get the contours of all holes.

The difference between the modes is demonstrated using the
following region:

![figure](../assets/a8422ce2dbc0f102.svg)

Example region.

Computing the contour with the different values available for
*`mode`* returns the following result contours:

|  |  |  |
| --- | --- | --- |
| ![figure](../assets/ef0505b97a486ef2.svg) | ![figure](../assets/eded99d556de26e7.svg) | ![figure](../assets/85dd11c1bde47084.svg) |
| ( 1) | ( 2) | ( 3) |

Result for *"center"* (1), *"border"* (2), and
*"border_holes"* mode (3).

This means, for example, that contours generated with
*"border"* will in general have a much larger Euclidean
length (see [`LengthXld`](length_xld.md)) than contours generated with
*"center"*. This results from the fact that for diagonal
border elements *"border"* uses two contour segments of
length 1 each, whereas *"center"* uses a single segment of
length $\sqrt{2}$ ![figure](../assets/102cc74656473d95.svg). Other features, e.g., the area (see
[`AreaCenterXld`](area_center_xld.md)), will obviously also have different values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input regions.

**`contours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Resulting contours.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode of contour generation.

Default:
"border"

List of values:
"border", "border_holes", "center"

## Possible Successors

`SmoothContoursXld`,
`GenPolygonsXld`

## Alternatives

`GenContourPolygonXld`,
`GetRegionContour`

## See also

`GenContoursSkeletonXld`

## Module

Foundation
