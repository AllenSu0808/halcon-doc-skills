# VarThreshold (Operator)

## Name

`VarThreshold` — Threshold an image by local mean and standard deviation analysis.

## Signature

`static void HOperatorSet.VarThreshold(HObject image, out HObject region, HTuple maskWidth, HTuple maskHeight, HTuple stdDevScale, HTuple absThreshold, HTuple lightDark)`

`HRegion HImage.VarThreshold(int maskWidth, int maskHeight, HTuple stdDevScale, HTuple absThreshold, string lightDark)`

`HRegion HImage.VarThreshold(int maskWidth, int maskHeight, double stdDevScale, double absThreshold, string lightDark)`

## Description

With `VarThreshold`, it's possible to select the pixels of the input
*`image`* which

- have a high local standard deviation (for a positive
  *`stdDevScale`*), or a low local standard deviation (for a negative
  *`stdDevScale`*)

and

- are locally bright or dark, according to *`lightDark`*.

Thus, it is possible to segment regions on inhomogeneous, noisy, or
unevenly illuminated backgrounds.

### Hints for the input parameters

- ***`maskWidth`*, *`maskHeight`*** —

  The size of the filter mask defined by *`maskWidth`* and
  *`maskHeight`* determines the maximum size of the objects to be
  segmented. However, if the mask is chosen too large, objects that are very
  close might be merged.

  |  |  |
  | --- | --- |
  | ![figure](../assets/7ce4dbfaec1f50a4.svg) | ![figure](../assets/12e4ced9d028c57b.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/fa9d7b42c8763332.svg) | ![figure](../assets/061e09d88e3c65ff.svg) |
  | ( 3) | ( 4) |

  (1) Original image; the goal is to count the vertical lines.
  (2) *`maskWidth`* := *12*, *`maskHeight`* := *12*,
  *`stdDevScale`* := *0.1*, all vertical lines are segmented
  correctly. (3) If the mask size is chosen too low (*3*), the desired
  regions are not selected properly. (4) If the mask size is too high
  (*40*), objects that are very close might be merged.

  If *`maskWidth`* or *`maskHeight`* is even, the next larger odd
  value is used. Altogether, a value of *3* can be considered the
  minimum sensible value.
- ***`stdDevScale`*** —

  The local standard deviation is used as a measure of noise in the image. It
  can be scaled by *`stdDevScale`* to reflect the desired sensitivity.
  A higher value means that only pixels that are very different from their
  surrounding are selected.

  For the parameter *`stdDevScale`* values between -1.0 and
  1.0 are sensible choices, with 0.2 as a suggested value. If the
  parameter is too high or too low, an empty or full region may be
  returned.

  |  |  |
  | --- | --- |
  | ![figure](../assets/a497d31d293dfa6e.svg) | ![figure](../assets/02287208e0bbe8e3.svg) |
  | ( 1) | ( 2) |

  (1) If *`stdDevScale`* is too high (*1.3*), the operator is
  'picky'; only pixels that are very similar to their surrounding are
  selected. (2) If *`stdDevScale`* is too low (*-0.3*), too many
  pixels that are somewhat similar to their surrounding are incorrectly
  selected.
- ***`absThreshold`*** —

  In homogeneous areas of an image, the standard deviation is low; thus, the
  influence of single gray values is high. To reduce the sensitivity of the
  operator in homogeneous areas, it's possible to adjust
  *`absThreshold`*. Thus, small gray value changes in homogeneous
  surroundings can be ignored. Note that for negative values of
  *`stdDevScale`*, *`absThreshold`* should also be chosen negative.
- ***`lightDark`*** —

  *"light"* or *"dark"* returns all pixels that are lighter or
  darker than their surrounding, respectively. *"equal"* returns all
  pixels that are not selected by either option, i.e. the pixels that are
  relatively equal to their surrounding. *"not_equal"* returns
  the combined results of *"light"* and *"dark"*, i.e., all
  pixels that differ from their surrounding.

### The calculation

|  |  |
| --- | --- |
| ![figure](../assets/08eb6985938b327b.svg) | ![figure](../assets/26778e79e7c73773.svg) |
| ( 1) | ( 2) |

(1) Initial image. (2) Thresholded image (*`stdDevScale`* :=
*0.6*, *`maskWidth`* := *15*, *`maskHeight`* :=
*15*, *`absThreshold`* := *10*). The following
images visualize exemplary how the result along the blue arrow came to be.

`VarThreshold` selects from the input image
*`image`* those regions *`region`* in which the pixels
fulfill a threshold condition. The threshold is calculated from the
mean gray value and the standard deviation in a local mask of size
*`maskWidth`* x *`maskHeight`* around each pixel
(x,y).

Let

- g(x,y) be the gray value at position (x,y) in the input
  *`image`*,
- m(x,y) the corresponding mean gray value, and
- d(x,y) the corresponding standard deviation in the mask around that
  pixel.

![figure](../assets/48cf05fa3d54fd6e.svg)

The original gray values, the
corresponding mean gray values, and the corresponding standard
deviation in the mask around these pixels.

Then, the variable threshold v(x,y) is defined as

$$v(x,y)=max(\texttt{StdDevScale}\ast d(x,y),\texttt{AbsThreshold})\text{for}\texttt{StdDevScale}\ge0$$
or
$$v(x,y)=min(\texttt{StdDevScale}\ast d(x,y),\texttt{AbsThreshold})\text{for}\texttt{StdDevScale}<0.$$

Interpretation: For a positive *`stdDevScale`*, each pixel is analyzed.
It is determined whether the user-defined *`absThreshold`* or the
scaled standard deviation is greater. The bigger value is chosen as variable
threshold v(x,y). For a negative *`stdDevScale`*, the corresponding
smaller value is chosen.

![figure](../assets/edee5b10dd791ea3.svg)

The standard deviation can be scaled with *`stdDevScale`*.

![figure](../assets/385b2c6d6b11c521.svg)

The variable threshold is chosen based on the scaled standard deviation
and *`absThreshold`*.

Which pixels are chosen based on the variable threshold is defined by
the parameter *`lightDark`*:

- *"light"*:
  $$g(x,y)\ge m(x,y)+v(x,y).$$

  Interpretation: If the pixel is brighter by v(x,y) than its surrounding,
  it is selected.
- *"dark"*:
  $$g(x,y)\le m(x,y)-v(x,y).$$

  Interpretation: If the pixel is darker by v(x,y) than its surrounding, it
  is selected.

  *`lightDark`* = *"equal"*:
  $$m(x,y)-v(x,y)\le g(x,y)\le m(x,y)+v(x,y).$$

  Interpretation: Select exactly those pixels that are not selected by
  *"light"* and *"dark"*, i.e., the pixels that are relatively
  equal to their surrounding.
- *"not_equal"*:
  $$m(x,y)-v(x,y)>g(x,y)\vee g(x,y)>m(x,y)+v(x,y).$$

  Interpretation: Select all pixels of *"light"* and *"dark"*,
  i.e., all pixels that differ by v(x,y) from their surrounding.

![figure](../assets/67d2d4a9771d2b73.svg)

*"light"* and *"dark"* are calculated based on the
corresponding mean gray value and the variable threshold.

![figure](../assets/0e1a5f5f5eac2052.svg)

For example, if *"dark"* is selected, all pixels where the 'Dark'
curve is above the 'GrayValues' curve would be selected.

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on domain level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int2 / int4 / uint2 / real)

Input image.

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Segmented regions.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Mask width for mean and deviation calculation.

Default:
15

Suggested values:
9, 11, 13, 15

Restriction:
`MaskWidth >= 1`

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Mask height for mean and deviation calculation.

Default:
15

Suggested values:
9, 11, 13, 15

Restriction:
`MaskHeight >= 1`

**`stdDevScale`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Factor for the standard deviation of the gray values.

Default:
0.2

Suggested values:
-0.2, -0.1, 0.1, 0.2

**`absThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Minimum gray value difference from the mean.

Default:
2

Suggested values:
-2, -1, 0, 1, 2

**`lightDark`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Threshold type.

Default:
"dark"

List of values:
"dark", "equal", "light", "not_equal"

## Complexity

Let A be the area of the input region, then the runtime is O(A).

## Result

`VarThreshold` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions can
be determined by setting the values of the flags *"no_object_result"*,
*"empty_region_result"*, and *"store_empty_region"* with
[`SetSystem`](set_system.md). If necessary, an exception is raised.

## Alternatives

`DynThreshold`,
`Threshold`

## References

W.Niblack, ”An Introduction to Digital Image Processing”, Page 115-116,
Englewood Cliffs, N.J., Prentice Hall, 1986

## Module

Foundation
