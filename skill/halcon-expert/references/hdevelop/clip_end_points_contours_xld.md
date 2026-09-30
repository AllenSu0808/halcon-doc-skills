# clip_end_points_contours_xld (Operator)

## Name

`clip_end_points_contours_xld` — Clip the end points of an XLD contour.

## Signature

`clip_end_points_contours_xld(Contours : ClippedContours : Mode, Length : )`

## Description

The operator `clip_end_points_contours_xld` clips the end
points of an XLD contour. The parameter *`Mode`* determines
the measure used to determine which part of the contour is clipped.

If *`Mode`* = *'length'*, the Euclidean length of the
part to be clipped is passed in *`Length`*. If *`Mode`*
= *'num_points'*, the number of points to be clipped is
passed in *`Length`*.

The clipped contour is returned in *`ClippedContours`*. If all
points of the input contour are clipped, no contour is returned.
Therefore, the number of returned contours is less or equal to the
number of input contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Contours`** (input_object)  xld_cont(-array) `→` object

Input contour

**`ClippedContours`** (output_object)  xld_cont(-array) `→` object

Clipped contour

**`Mode`** (input_control)  string `→`  (string)

Clipping mode.

Default:
'num_points'

List of values:
'length', 'num_points'

**`Length`** (input_control)  number `→`  (real / integer)

Clipping length in unit
pixels (*`Mode`* = *'length'*) or
number (*`Mode`* = *'num_points'*)

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
