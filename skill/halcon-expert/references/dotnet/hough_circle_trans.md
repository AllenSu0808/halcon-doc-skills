# HoughCircleTrans (Operator)

## Name

`HoughCircleTrans` — Return the Hough-Transform for circles with a given radius.

## Signature

`static void HOperatorSet.HoughCircleTrans(HObject region, out HObject houghImage, HTuple radius)`

`HImage HRegion.HoughCircleTrans(HTuple radius)`

`HImage HRegion.HoughCircleTrans(int radius)`

## Description

The operator `HoughCircleTrans` calculates the Hough transform for circles
with a certain *`radius`* in the regions passed by *`region`*. Hereby the
centers of all possible circles in the parameter space (the Hough or accumulator space
respectively) will be accumulated for each point in the image space.
Circle hypotheses supported by many points in the input region thereby
generate a maximum in the area showing the circle's center in the output image
(*`houghImage`*). The circles' centers in the image space can be deduced from the
coordinates of these maximums by subtracting the *`radius`*. If more than one radius is
transmitted, all Hough images will be shifted according to the maximal radius.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region `→` [HRegion](HRegion.md)

Binary edge image in which the circles are to be detected.

**`houghImage`** (output_object)  image(-array) `→` [HImage](HImage.md) (int2)

Hough transform for circles with a given radius.

Number of elements:
HoughImage == Radius

**`radius`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

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

The operator `HoughCircleTrans` returns the value 2 (
H_MSG_TRUE)
if the input is not empty.
The behavior in case of empty input (no input regions available) is
set via the operator `set_system('no_object_result',<Result>)`,
the behavior in case of empty region is set via
`set_system('empty_region_result',<Result>)`.
If necessary an exception is raised.

## Module

Foundation
