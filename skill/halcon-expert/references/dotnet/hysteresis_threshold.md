# HysteresisThreshold (Operator)

## Name

`HysteresisThreshold` — Perform a hysteresis threshold operation on an image.

## Signature

`static void HOperatorSet.HysteresisThreshold(HObject image, out HObject regionHysteresis, HTuple low, HTuple high, HTuple maxLength)`

`HRegion HImage.HysteresisThreshold(HTuple low, HTuple high, int maxLength)`

`HRegion HImage.HysteresisThreshold(int low, int high, int maxLength)`

## Description

`HysteresisThreshold` performs a hysteresis threshold
operation (introduced by Canny) on an image. All points in the input image
*`image`* having a gray value larger than or equal to *`high`* are
immediately accepted (“secure” points). Conversely, all points
with gray values less than *`low`* are immediately rejected.
“Potential” points with gray values between both thresholds are
accepted if they are connected to “secure” points by a path of
“potential” points having a length of at most *`maxLength`*
points. This means that “secure” points influence their
surroundings (hysteresis).

## Attention

For images of type byte, uint2, or int4 the lower threshold must be
*`low`* > 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / uint2 / int4 / real)

Input image.

**`regionHysteresis`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented region.

**`low`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Lower threshold for the gray values.

Default:
30

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

**`high`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Upper threshold for the gray values.

Default:
60

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130

Restriction:
`High >= Low`

**`maxLength`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum length of a path of “potential” points to
reach a “secure” point.

Default:
10

Suggested values:
1, 2, 3, 5, 7, 10, 12, 14, 17, 20, 25, 30, 35, 40, 50

Value range:
`1
≤
maxLength`

Minimum increment:
1

Recommended increment:
5

## Result

`HysteresisThreshold` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Alternatives

`DynThreshold`,
`Threshold`,
`Class2dimSup`,
`FastThreshold`

## See also

`EdgesImage`,
`SobelDir`,
`BackgroundSeg`

## References

J. Canny, “Finding Edges and Lines in Images”;
Report, AI-TR-720, M.I.T. Artificial Intelligence Lab.,
Cambridge, MA, 1983.

## Module

Foundation
