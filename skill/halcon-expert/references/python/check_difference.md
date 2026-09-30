# check_difference (Operator)

## Name

`check_difference` — Compare two images pixel by pixel.

## Signature

`def check_difference(image: HObject, pattern: HObject, mode: str, diff_lower_bound: int, diff_upper_bound: int, gray_offset: int, add_row: int, add_col: int) -> HObject`

## Description

`check_difference` selects from the input image
*`image`* those pixels
($g_{0} = g\mathrm{Image}$ ![figure](../assets/f1c89f78ccfa4816.svg)),
whose gray value difference to the corresponding pixels in
*`pattern`* is inside (outside) of the interval
$[\texttt{DiffLowerBound},\texttt{DiffUpperBound}]$.
The pixels of *`pattern`* are
translated by $(\texttt{AddRow},\texttt{AddCol})$
with respect to *`image`*.
Let $g_{p}$ be the gray value from
*`pattern`* translated by
$(\texttt{AddRow},\texttt{AddCol})$
with respect to $g_{o}$.

If the selected mode *`mode`* is *"diff_inside"*,
a pixel $g_{o}$ is selected if
$$g_o - g_p - GrayOffset \ge DiffLowerBound and g_o - g_p - GrayOffset \le DiffUpperBound.$$ ![figure](../assets/48eab04b9237a799.svg)
If the mode is set to *"diff_outside"*, a pixel $g_{o}$
is selected if
g_o - g_p - GrayOffset < DiffLowerBound or
g_o - g_p - GrayOffset > DiffUpperBound.
This test is performed for all points of the domain (region) of
*`image`*, intersected with the domain of the translated
*`pattern`*. All points fulfilling the above condition are
aggregated in the output region. The two images may be of different
size. Typically, *`pattern`* is smaller than
*`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Input image.

**`pattern`** (input_object)  singlechannelimage(-array) `→` HObject (byte)

Comparison image.

**`selected`** (output_object)  region(-array) `→` HObject

Points in which the two images are similar/different.

**`mode`** (input_control)  string `→` str

Mode: return similar or different pixels.

Default:
"diff_outside"

Suggested values:
"diff_inside", "diff_outside"

**`diff_lower_bound`** (input_control)  number `→` int

Lower bound of the tolerated gray value difference.

Default:
-5

Suggested values:
0, -1, -2, -3, -5, -7, -10, -12, -15, -17, -20, -25, -30

Value range:
`-255
≤
diff_lower_bound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`diff_upper_bound`** (input_control)  number `→` int

Upper bound of the tolerated gray value difference.

Default:
5

Suggested values:
0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
diff_upper_bound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`gray_offset`** (input_control)  number `→` int

Offset gray value subtracted from the input image.

Default:
0

Suggested values:
-30, -25, -20, -17, -15, -12, -10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
gray_offset
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`add_row`** (input_control)  point.y `→` int

Row coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
add_row
≤
32000` (lin)

Minimum increment:
1

Recommended increment:
1

**`add_col`** (input_control)  point.x `→` int

Column coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
add_col
≤
32000` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let $A$ be the number of valid pixels. Then the runtime complexity
is $O(A)$.

## Result

`check_difference` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Successors

`connection`,
`select_shape`,
`reduce_domain`,
`select_gray`,
`rank_region`,
`dilation1`,
`opening`

## Alternatives

`sub_image`,
`dyn_threshold`

## Module

Foundation
