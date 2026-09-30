# hysteresis_threshold (Operator)

## Name

`hysteresis_threshold` — Perform a hysteresis threshold operation on an image.

## Signature

`hysteresis_threshold(Image : RegionHysteresis : Low, High, MaxLength : )`

## Description

`hysteresis_threshold` performs a hysteresis threshold
operation (introduced by Canny) on an image. All points in the input image
*`Image`* having a gray value larger than or equal to *`High`* are
immediately accepted (“secure” points). Conversely, all points
with gray values less than *`Low`* are immediately rejected.
“Potential” points with gray values between both thresholds are
accepted if they are connected to “secure” points by a path of
“potential” points having a length of at most *`MaxLength`*
points. This means that “secure” points influence their
surroundings (hysteresis).

## Attention

For images of type byte, uint2, or int4 the lower threshold must be
*`Low`* > 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / uint2 / int4 / real)

Input image.

**`RegionHysteresis`** (output_object)  region(-array) `→` object

Segmented region.

**`Low`** (input_control)  number `→`  (integer / real)

Lower threshold for the gray values.

Default:
30

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100

**`High`** (input_control)  number `→`  (integer / real)

Upper threshold for the gray values.

Default:
60

Suggested values:
5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130

Restriction:
`High >= Low`

**`MaxLength`** (input_control)  integer `→`  (integer)

Maximum length of a path of “potential” points to
reach a “secure” point.

Default:
10

Suggested values:
1, 2, 3, 5, 7, 10, 12, 14, 17, 20, 25, 30, 35, 40, 50

Value range:
`1
≤
MaxLength`

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
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
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
