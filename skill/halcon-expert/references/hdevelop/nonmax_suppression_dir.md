# nonmax_suppression_dir (Operator)

## Name

`nonmax_suppression_dir` — Suppress non-maximum points on an edge using a direction image.

## Signature

`nonmax_suppression_dir(ImgAmp, ImgDir : ImageResult : Mode : )`

## Description

`nonmax_suppression_dir` suppresses all points in the
regions of the image *`ImgAmp`* whose gray values are
not local (directed) maxima. *`ImgDir`* is a direction image
giving the direction perpendicular to the local maximum (Unit:
2 degrees, i.e., 50 degrees are coded as 25 in the image). Such
images are returned, for example, by [`edges_image`](edges_image.md). Two modes
of operation can be selected:

- ***'nms'*** —

  Each point in the image is tested whether its gray value
  is a local maximum perpendicular to its direction. In
  this mode only the two neighbors closest to the given
  direction are examined. If one of the two gray values is
  greater than the gray value of the point to be tested, it is
  suppressed (i.e., removed from the input region. The corresponding
  gray value remains unchanged).
- ***'inms'*** —

  Like *'nms'*. However, the two gray values for the test
  are obtained by interpolation from four adjacent points.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`ImgAmp`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / real)

Amplitude (gradient magnitude) image.

**`ImgDir`** (input_object)  singlechannelimage(-array) `→` object (direction)

Direction image.

**`ImageResult`** (output_object)  image(-array) `→` object (byte / uint2 / real)

Image with thinned edge regions.

**`Mode`** (input_control)  string `→`  (string)

Select non-maximum-suppression or interpolating NMS.

Default:
'nms'

List of values:
'inms', 'nms'

## Result

`nonmax_suppression_dir` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`edges_image`,
`sobel_dir`,
`frei_dir`

## Possible Successors

`threshold`,
`hysteresis_threshold`

## Alternatives

`nonmax_suppression_amp`

## See also

`skeleton`

## References

S.Lanser: “Detektion von Stufenkanten mittels rekursiver Filter nach
Deriche”; Diplomarbeit; Technische Universität München, Institut
für Informatik, Lehrstuhl Prof. Radig; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge; 1983.

## Module

Foundation
