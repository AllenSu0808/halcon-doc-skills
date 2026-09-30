# NonmaxSuppressionDir (Operator)

## Name

`NonmaxSuppressionDir` — Suppress non-maximum points on an edge using a direction image.

## Signature

`static void HOperatorSet.NonmaxSuppressionDir(HObject imgAmp, HObject imgDir, out HObject imageResult, HTuple mode)`

`HImage HImage.NonmaxSuppressionDir(HImage imgDir, string mode)`

## Description

`NonmaxSuppressionDir` suppresses all points in the
regions of the image *`imgAmp`* whose gray values are
not local (directed) maxima. *`imgDir`* is a direction image
giving the direction perpendicular to the local maximum (Unit:
2 degrees, i.e., 50 degrees are coded as 25 in the image). Such
images are returned, for example, by [`EdgesImage`](edges_image.md). Two modes
of operation can be selected:

- ***"nms"*** —

  Each point in the image is tested whether its gray value
  is a local maximum perpendicular to its direction. In
  this mode only the two neighbors closest to the given
  direction are examined. If one of the two gray values is
  greater than the gray value of the point to be tested, it is
  suppressed (i.e., removed from the input region. The corresponding
  gray value remains unchanged).
- ***"inms"*** —

  Like *"nms"*. However, the two gray values for the test
  are obtained by interpolation from four adjacent points.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`imgAmp`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Amplitude (gradient magnitude) image.

**`imgDir`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (direction)

Direction image.

**`imageResult`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / uint2 / real)

Image with thinned edge regions.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Select non-maximum-suppression or interpolating NMS.

Default:
"nms"

List of values:
"inms", "nms"

## Result

`NonmaxSuppressionDir` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`EdgesImage`,
`SobelDir`,
`FreiDir`

## Possible Successors

`Threshold`,
`HysteresisThreshold`

## Alternatives

`NonmaxSuppressionAmp`

## See also

`Skeleton`

## References

S.Lanser: “Detektion von Stufenkanten mittels rekursiver Filter nach
Deriche”; Diplomarbeit; Technische Universität München, Institut
für Informatik, Lehrstuhl Prof. Radig; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge; 1983.

## Module

Foundation
