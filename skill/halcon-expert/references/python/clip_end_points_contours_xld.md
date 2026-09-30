# clip_end_points_contours_xld (Operator)

## Name

`clip_end_points_contours_xld` — Clip the end points of an XLD contour.

## Signature

`def clip_end_points_contours_xld(contours: HObject, mode: str, length: Union[int, float]) -> HObject`

## Description

The operator `clip_end_points_contours_xld` clips the end
points of an XLD contour. The parameter *`mode`* determines
the measure used to determine which part of the contour is clipped.

If *`mode`* = *"length"*, the Euclidean length of the
part to be clipped is passed in *`length`*. If *`mode`*
= *"num_points"*, the number of points to be clipped is
passed in *`length`*.

The clipped contour is returned in *`clipped_contours`*. If all
points of the input contour are clipped, no contour is returned.
Therefore, the number of returned contours is less or equal to the
number of input contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input contour

**`clipped_contours`** (output_object)  xld_cont(-array) `→` HObject

Clipped contour

**`mode`** (input_control)  string `→` str

Clipping mode.

Default:
"num_points"

List of values:
"length", "num_points"

**`length`** (input_control)  number `→` Union[int, float]

Clipping length in unit
pixels (*`mode`* = *"length"*) or
number (*`mode`* = *"num_points"*)

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Result

`clip_end_points_contours_xld` returns 2 (
H_MSG_TRUE)
if the input is
not empty. The behavior in case of empty input (no input contour
available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`segment_contours_xld`

## See also

`clip_contours_xld`,
`crop_contours_xld`

## Module

Foundation
