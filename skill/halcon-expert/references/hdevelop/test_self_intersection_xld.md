# test_self_intersection_xld (Operator)

## Name

`test_self_intersection_xld` — Test XLD contours or polygons for self intersection.

## Signature

`test_self_intersection_xld(XLD : : CloseXLD : DoesIntersect)`

## Description

`test_self_intersection_xld` tests whether the input contours
or polygons in *`XLD`* intersect or touch themselves. The output array
*`DoesIntersect`* contains a *1* if the corresponding
input contour or polygon intersects or touches itself and *0*
otherwise.

If the input parameter *`CloseXLD`* is set to *'true'*,
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

**`XLD`** (input_object)  xld(-array) `→` object

Input contours or polygons.

**`CloseXLD`** (input_control)  string `→`  (string)

Should the input contours or polygons be closed
first?

Default:
'true'

List of values:
'false', 'true'

**`DoesIntersect`** (output_control)  number(-array) `→`  (integer)

1 for contours or polygons with self intersection
and 0 otherwise.

## Module

Foundation
