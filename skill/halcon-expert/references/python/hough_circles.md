# hough_circles (Operator)

## Name

`hough_circles` — Detect centers of circles for a specific radius using the Hough transform.

## Signature

`def hough_circles(region_in: HObject, radius: MaybeSequence[int], percent: MaybeSequence[int], mode: MaybeSequence[int]) -> HObject`

## Description

`hough_circles` detects the centers of circles in regions
with the help of the Hough transform
for circles with a specific radius.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region_in`** (input_object)  region `→` HObject

Binary edge image in which the circles are to be detected.

**`region_out`** (output_object)  region(-array) `→` HObject

Centers of those circles which are included in the edge image by *`percent`* percent.

Number of elements:
RegionOut == Radius * Percent * Mode

**`radius`** (input_control)  integer(-array) `→` MaybeSequence[int]

Radius of the circle to be searched in the image.

Number of elements:
1 <= Radius <= 500

Default:
12

Value range:
`2
≤
radius
≤
500` (lin)

Minimum increment:
1

Recommended increment:
1

**`percent`** (input_control)  integer(-array) `→` MaybeSequence[int]

Indicates the percentage (approximately) of the (ideal) circle which
must be present in the edge image *`region_in`*.

Number of elements:
1 <= Percent <= 100

Default:
60

Value range:
`10
≤
percent
≤
100` (lin)

Minimum increment:
1

Recommended increment:
5

**`mode`** (input_control)  integer(-array) `→` MaybeSequence[int]

The mode defines the position of the circle in question:  
0 - the radius is equivalent to the outer border of the set pixels.  
1 - the radius is equivalent to the centers of the circle lines' pixels.  
2 - both 0 and 1 (a little more fuzzy, but more reliable in contrast to
circles set slightly differently, necessitates 50 %
more processing capacity compared to 0 or 1 alone).

Number of elements:
1 <= Mode <= 3

List of values:
0, 1, 2

## Result

The operator `hough_circles` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Module

Foundation
