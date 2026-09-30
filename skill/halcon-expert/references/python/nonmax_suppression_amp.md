# nonmax_suppression_amp (Operator)

## Name

`nonmax_suppression_amp` — Suppress non-maximum points on an edge.

## Signature

`def nonmax_suppression_amp(img_amp: HObject, mode: str) -> HObject`

## Description

`nonmax_suppression_amp` suppresses all points in the
regions of the image *`img_amp`* whose gray values are
not local (directed) maxima. In contrast to
[`nonmax_suppression_dir`](nonmax_suppression_dir.md), a direction image is not needed.
Two modes of operation can be selected:

- ***"hvnms"*** —

  A point is labeled as a local maximum if its gray value
  is larger than or equal to the gray values within a search
  space of pm 5 pixels, either horizontally or vertically.
  Non-maximum points are removed from the region, gray
  values remain unchanged.
- ***"loc_max"*** —

  A point is labeled as a local maximum if its gray value
  is larger than or equal to the gray values of its eight
  neighbors.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`img_amp`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Amplitude (gradient magnitude) image.

**`image_result`** (output_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / real)

Image with thinned edge regions.

**`mode`** (input_control)  string `→` str

Select horizontal/vertical or undirected NMS.

Default:
"hvnms"

List of values:
"hvnms", "loc_max"

## Result

`nonmax_suppression_amp` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`sobel_amp`

## Possible Successors

`threshold`,
`hysteresis_threshold`

## Alternatives

`local_max`,
`nonmax_suppression_dir`

## See also

`skeleton`

## References

S.Lanser: “Detektion von Stufenkanten mittels rekursiver Filter nach
Deriche”; Diplomarbeit; Technische Universität München, Institut
für Informatik, Lehrstuhl Prof. Radig; 1991.
  
J.Canny: “Finding Edges and Lines in Images”; Report, AI-TR-720;
M.I.T. Artificial Intelligence Lab., Cambridge, MA; 1983.

## Module

Foundation
