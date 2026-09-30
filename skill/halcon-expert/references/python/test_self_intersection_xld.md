# test_self_intersection_xld (Operator)

## Name

`test_self_intersection_xld` — Test XLD contours or polygons for self intersection.

## Signature

`def test_self_intersection_xld(xld: HObject, close_xld: str) -> Sequence[int]`

`def test_self_intersection_xld_s(xld: HObject, close_xld: str) -> int`

## Description

`test_self_intersection_xld` tests whether the input contours
or polygons in *`xld`* intersect or touch themselves. The output array
*`does_intersect`* contains a *1* if the corresponding
input contour or polygon intersects or touches itself and *0*
otherwise.

If the input parameter *`close_xld`* is set to *"true"*,
open contours or polygons are closed before the check is performed
by simply connecting the first and the last contour or polygon point
with a line segment.

## Attention

A contour or polygon touches itself if a contour or polygon point
lies exactly on a contour or polygon segment. However, whether a
point lies exactly on a contour or polygon segment or not can
practically not be decided because of numerical reasons.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

Input contours or polygons.

**`close_xld`** (input_control)  string `→` str

Should the input contours or polygons be closed
first?

Default:
"true"

List of values:
"false", "true"

**`does_intersect`** (output_control)  number(-array) `→` Sequence[int]

1 for contours or polygons with self intersection
and 0 otherwise.

## Module

Foundation
