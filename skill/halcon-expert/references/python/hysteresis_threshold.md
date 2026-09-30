# hysteresis_threshold (Operator)

## Name

`hysteresis_threshold` — Perform a hysteresis threshold operation on an image.

## Signature

`def hysteresis_threshold(image: HObject, low: Union[int, float], high: Union[int, float], max_length: int) -> HObject`

## Description

`hysteresis_threshold` performs a hysteresis threshold
operation (introduced by Canny) on an image. All points in the input image
*`image`* having a gray value larger than or equal to *`high`* are
immediately accepted (“secure” points). Conversely, all points
with gray values less than *`low`* are immediately rejected.
“Potential” points with gray values between both thresholds are
accepted if they are connected to “secure” points by a path of
“potential” points having a length of at most *`max_length`*
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

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / uint2 / int4 / real)

Input image.

**`region_hysteresis`** (output_object)  region(-array) `→` HObject

Segmented region.

**`low`** (input_control)  number `→` Union[int, float]

Lower threshold for the gray values.

Default:
30

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

**`high`** (input_control)  number `→` Union[int, float]

Upper threshold for the gray values.

Default:
60

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130

Restriction:
`High >= Low`

**`max_length`** (input_control)  integer `→` int

Maximum length of a path of “potential” points to
reach a “secure” point.

Default:
10

Suggested values:
1, 2, 3, 5, 7, 10, 12, 14, 17, 20, 25, 30, 35, 40, 50

Value range:
`1
≤
max_length`

Minimum increment:
1

Recommended increment:
5

## Result

`hysteresis_threshold` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Alternatives

`dyn_threshold`,
`threshold`,
`class_2dim_sup`,
`fast_threshold`

## See also

`edges_image`,
`sobel_dir`,
`background_seg`

## References

J. Canny, “Finding Edges and Lines in Images”;
Report, AI-TR-720, M.I.T. Artificial Intelligence Lab.,
Cambridge, MA, 1983.

## Module

Foundation
