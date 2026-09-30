# hough_circle_trans (Operator)

## Name

`hough_circle_trans` — Return the Hough-Transform for circles with a given radius.

## Signature

`def hough_circle_trans(region: HObject, radius: MaybeSequence[int]) -> HObject`

## Description

The operator `hough_circle_trans` calculates the Hough transform for circles
with a certain *`radius`* in the regions passed by *`region`*. Hereby the
centers of all possible circles in the parameter space (the Hough or accumulator space
respectively) will be accumulated for each point in the image space.
Circle hypotheses supported by many points in the input region thereby
generate a maximum in the area showing the circle's center in the output image
(*`hough_image`*). The circles' centers in the image space can be deduced from the
coordinates of these maximums by subtracting the *`radius`*. If more than one radius is
transmitted, all Hough images will be shifted according to the maximal radius.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` HObject

Binary edge image in which the circles are to be detected.

**`hough_image`** (output_object)  image(-array) `→` HObject (int2)

Hough transform for circles with a given radius.

Number of elements:
HoughImage == Radius

**`radius`** (input_control)  integer(-array) `→` MaybeSequence[int]

Radius of the circle to be searched in the image.

Number of elements:
1 <= Radius <= 500

Default:
12

Value range:
`3
≤
radius` (lin)

Minimum increment:
1

Recommended increment:
1

## Result

The operator `hough_circle_trans` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Module

Foundation
