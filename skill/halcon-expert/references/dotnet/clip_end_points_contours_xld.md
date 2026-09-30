# ClipEndPointsContoursXld (Operator)

## Name

`ClipEndPointsContoursXld` — Clip the end points of an XLD contour.

## Signature

`static void HOperatorSet.ClipEndPointsContoursXld(HObject contours, out HObject clippedContours, HTuple mode, HTuple length)`

`HXLDCont HXLDCont.ClipEndPointsContoursXld(string mode, HTuple length)`

`HXLDCont HXLDCont.ClipEndPointsContoursXld(string mode, double length)`

## Description

The operator `ClipEndPointsContoursXld` clips the end
points of an XLD contour. The parameter *`mode`* determines
the measure used to determine which part of the contour is clipped.

If *`mode`* = *"length"*, the Euclidean length of the
part to be clipped is passed in *`length`*. If *`mode`*
= *"num_points"*, the number of points to be clipped is
passed in *`length`*.

The clipped contour is returned in *`clippedContours`*. If all
points of the input contour are clipped, no contour is returned.
Therefore, the number of returned contours is less or equal to the
number of input contours.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contour

**`clippedContours`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Clipped contour

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Clipping mode.

Default:
"num_points"

List of values:
"length", "num_points"

**`length`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Clipping length in unit
pixels (*`mode`* = *"length"*) or
number (*`mode`* = *"num_points"*)

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Result

`ClipEndPointsContoursXld` returns 2 (
H_MSG_TRUE)
if the input is
not empty. The behavior in case of empty input (no input contour
available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`SegmentContoursXld`

## See also

`ClipContoursXld`,
`CropContoursXld`

## Module

Foundation
