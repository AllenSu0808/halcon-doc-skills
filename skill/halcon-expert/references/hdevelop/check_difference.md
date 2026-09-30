# check_difference (Operator)

## Name

`check_difference` — Compare two images pixel by pixel.

## Signature

`check_difference(Image, Pattern : Selected : Mode, DiffLowerBound, DiffUpperBound, GrayOffset, AddRow, AddCol : )`

## Description

`check_difference` selects from the input image
*`Image`* those pixels
($g_{0} = g\mathrm{Image}$ ![figure](../assets/f1c89f78ccfa4816.svg)),
whose gray value difference to the corresponding pixels in
*`Pattern`* is inside (outside) of the interval
$[\texttt{DiffLowerBound},\texttt{DiffUpperBound}]$.
The pixels of *`Pattern`* are
translated by $(\texttt{AddRow},\texttt{AddCol})$
with respect to *`Image`*.
Let $g_{p}$ be the gray value from
*`Pattern`* translated by
$(\texttt{AddRow},\texttt{AddCol})$
with respect to $g_{o}$.

If the selected mode *`Mode`* is *'diff_inside'*,
a pixel $g_{o}$ is selected if
$$g_o - g_p - GrayOffset \ge DiffLowerBound and g_o - g_p - GrayOffset \le DiffUpperBound.$$ ![figure](../assets/48eab04b9237a799.svg)
If the mode is set to *'diff_outside'*, a pixel $g_{o}$
is selected if
g_o - g_p - GrayOffset < DiffLowerBound or
g_o - g_p - GrayOffset > DiffUpperBound.
This test is performed for all points of the domain (region) of
*`Image`*, intersected with the domain of the translated
*`Pattern`*. All points fulfilling the above condition are
aggregated in the output region. The two images may be of different
size. Typically, *`Pattern`* is smaller than
*`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte)

Input image.

**`Pattern`** (input_object)  singlechannelimage(-array) `→` object (byte)

Comparison image.

**`Selected`** (output_object)  region(-array) `→` object

Points in which the two images are similar/different.

**`Mode`** (input_control)  string `→`  (string)

Mode: return similar or different pixels.

Default:
'diff_outside'

Suggested values:
'diff_inside', 'diff_outside'

**`DiffLowerBound`** (input_control)  number `→`  (integer)

Lower bound of the tolerated gray value difference.

Default:
-5

Suggested values:
0, -1, -2, -3, -5, -7, -10, -12, -15, -17, -20, -25, -30

Value range:
`-255
≤
DiffLowerBound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`DiffUpperBound`** (input_control)  number `→`  (integer)

Upper bound of the tolerated gray value difference.

Default:
5

Suggested values:
0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
DiffUpperBound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`GrayOffset`** (input_control)  number `→`  (integer)

Offset gray value subtracted from the input image.

Default:
0

Suggested values:
-30, -25, -20, -17, -15, -12, -10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
GrayOffset
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`AddRow`** (input_control)  point.y `→`  (integer)

Row coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
AddRow
≤
32000` (lin)

Minimum increment:
1

Recommended increment:
1

**`AddCol`** (input_control)  point.x `→`  (integer)

Column coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
AddCol
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
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
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
