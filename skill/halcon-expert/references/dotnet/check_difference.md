# CheckDifference (Operator)

## Name

`CheckDifference` — Compare two images pixel by pixel.

## Signature

`static void HOperatorSet.CheckDifference(HObject image, HObject pattern, out HObject selected, HTuple mode, HTuple diffLowerBound, HTuple diffUpperBound, HTuple grayOffset, HTuple addRow, HTuple addCol)`

`HRegion HImage.CheckDifference(HImage pattern, string mode, int diffLowerBound, int diffUpperBound, int grayOffset, int addRow, int addCol)`

## Description

`CheckDifference` selects from the input image
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

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Input image.

**`pattern`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte)

Comparison image.

**`selected`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Points in which the two images are similar/different.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode: return similar or different pixels.

Default:
"diff_outside"

Suggested values:
"diff_inside", "diff_outside"

**`diffLowerBound`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Lower bound of the tolerated gray value difference.

Default:
-5

Suggested values:
0, -1, -2, -3, -5, -7, -10, -12, -15, -17, -20, -25, -30

Value range:
`-255
≤
diffLowerBound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`diffUpperBound`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Upper bound of the tolerated gray value difference.

Default:
5

Suggested values:
0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
diffUpperBound
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`grayOffset`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Offset gray value subtracted from the input image.

Default:
0

Suggested values:
-30, -25, -20, -17, -15, -12, -10, -7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7, 10, 12, 15, 17, 20, 25, 30

Value range:
`-255
≤
grayOffset
≤
255` (lin)

Minimum increment:
1

Recommended increment:
2

**`addRow`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
addRow
≤
32000` (lin)

Minimum increment:
1

Recommended increment:
1

**`addCol`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate by which the comparison image is translated.

Default:
0

Suggested values:
-200, -100, -20, -10, 0, 10, 20, 100, 200

Value range:
`-32000
≤
addCol
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

`CheckDifference` returns 2 (
H_MSG_TRUE)
if all parameters
are correct. The behavior with respect to the input images and
output regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Successors

`Connection`,
`SelectShape`,
`ReduceDomain`,
`SelectGray`,
`RankRegion`,
`Dilation1`,
`Opening`

## Alternatives

`SubImage`,
`DynThreshold`

## Module

Foundation
