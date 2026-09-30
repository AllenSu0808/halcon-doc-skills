# var_threshold (Operator)

## Name

`var_threshold` — Threshold an image by local mean and standard deviation analysis.

## Signature

`var_threshold(Image : Region : MaskWidth, MaskHeight, StdDevScale, AbsThreshold, LightDark : )`

## Description

With `var_threshold`, it's possible to select the pixels of the input
*`Image`* which

- have a high local standard deviation (for a positive
  *`StdDevScale`*), or a low local standard deviation (for a negative
  *`StdDevScale`*)

and

- are locally bright or dark, according to *`LightDark`*.

Thus, it is possible to segment regions on inhomogeneous, noisy, or
unevenly illuminated backgrounds.

### Hints for the input parameters

- ***`MaskWidth`*, *`MaskHeight`*** —

  The size of the filter mask defined by *`MaskWidth`* and
  *`MaskHeight`* determines the maximum size of the objects to be
  segmented. However, if the mask is chosen too large, objects that are very
  close might be merged.

  |  |  |
  | --- | --- |
  | ![figure](../assets/7ce4dbfaec1f50a4.svg) | ![figure](../assets/12e4ced9d028c57b.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/fa9d7b42c8763332.svg) | ![figure](../assets/061e09d88e3c65ff.svg) |
  | ( 3) | ( 4) |

  (1) Original image; the goal is to count the vertical lines.
  (2) *`MaskWidth`* := *12*, *`MaskHeight`* := *12*,
  *`StdDevScale`* := *0.1*, all vertical lines are segmented
  correctly. (3) If the mask size is chosen too low (*3*), the desired
  regions are not selected properly. (4) If the mask size is too high
  (*40*), objects that are very close might be merged.

  If *`MaskWidth`* or *`MaskHeight`* is even, the next larger odd
  value is used. Altogether, a value of *3* can be considered the
  minimum sensible value.
- ***`StdDevScale`*** —

  The local standard deviation is used as a measure of noise in the image. It
  can be scaled by *`StdDevScale`* to reflect the desired sensitivity.
  A higher value means that only pixels that are very different from their
  surrounding are selected.

  For the parameter *`StdDevScale`* values between -1.0 and
  1.0 are sensible choices, with 0.2 as a suggested value. If the
  parameter is too high or too low, an empty or full region may be
  returned.

  |  |  |
  | --- | --- |
  | ![figure](../assets/a497d31d293dfa6e.svg) | ![figure](../assets/02287208e0bbe8e3.svg) |
  | ( 1) | ( 2) |

  (1) If *`StdDevScale`* is too high (*1.3*), the operator is
  'picky'; only pixels that are very similar to their surrounding are
  selected. (2) If *`StdDevScale`* is too low (*-0.3*), too many
  pixels that are somewhat similar to their surrounding are incorrectly
  selected.
- ***`AbsThreshold`*** —

  In homogeneous areas of an image, the standard deviation is low; thus, the
  influence of single gray values is high. To reduce the sensitivity of the
  operator in homogeneous areas, it's possible to adjust
  *`AbsThreshold`*. Thus, small gray value changes in homogeneous
  surroundings can be ignored. Note that for negative values of
  *`StdDevScale`*, *`AbsThreshold`* should also be chosen negative.
- ***`LightDark`*** —

  *'light'* or *'dark'* returns all pixels that are lighter or
  darker than their surrounding, respectively. *'equal'* returns all
  pixels that are not selected by either option, i.e. the pixels that are
  relatively equal to their surrounding. *'not_equal'* returns
  the combined results of *'light'* and *'dark'*, i.e., all
  pixels that differ from their surrounding.

### The calculation

|  |  |
| --- | --- |
| ![figure](../assets/08eb6985938b327b.svg) | ![figure](../assets/26778e79e7c73773.svg) |
| ( 1) | ( 2) |

(1) Initial image. (2) Thresholded image (*`StdDevScale`* :=
*0.6*, *`MaskWidth`* := *15*, *`MaskHeight`* :=
*15*, *`AbsThreshold`* := *10*). The following
images visualize exemplary how the result along the blue arrow came to be.

`var_threshold` selects from the input image
*`Image`* those regions *`Region`* in which the pixels
fulfill a threshold condition. The threshold is calculated from the
mean gray value and the standard deviation in a local mask of size
*`MaskWidth`* x *`MaskHeight`* around each pixel
(x,y).

Let

- g(x,y) be the gray value at position (x,y) in the input
  *`Image`*,
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

Interpretation: For a positive *`StdDevScale`*, each pixel is analyzed.
It is determined whether the user-defined *`AbsThreshold`* or the
scaled standard deviation is greater. The bigger value is chosen as variable
threshold v(x,y). For a negative *`StdDevScale`*, the corresponding
smaller value is chosen.

![figure](../assets/edee5b10dd791ea3.svg)

The standard deviation can be scaled with *`StdDevScale`*.

![figure](../assets/385b2c6d6b11c521.svg)

The variable threshold is chosen based on the scaled standard deviation
and *`AbsThreshold`*.

Which pixels are chosen based on the variable threshold is defined by
the parameter *`LightDark`*:

- *'light'*:
  $$g(x,y)\ge m(x,y)+v(x,y).$$

  Interpretation: If the pixel is brighter by v(x,y) than its surrounding,
  it is selected.
- *'dark'*:
  $$g(x,y)\le m(x,y)-v(x,y).$$

  Interpretation: If the pixel is darker by v(x,y) than its surrounding, it
  is selected.

  *`LightDark`* = *'equal'*:
  $$m(x,y)-v(x,y)\le g(x,y)\le m(x,y)+v(x,y).$$

  Interpretation: Select exactly those pixels that are not selected by
  *'light'* and *'dark'*, i.e., the pixels that are relatively
  equal to their surrounding.
- *'not_equal'*:
  $$m(x,y)-v(x,y)>g(x,y)\vee g(x,y)>m(x,y)+v(x,y).$$

  Interpretation: Select all pixels of *'light'* and *'dark'*,
  i.e., all pixels that differ by v(x,y) from their surrounding.

![figure](../assets/67d2d4a9771d2b73.svg)

*'light'* and *'dark'* are calculated based on the
corresponding mean gray value and the variable threshold.

![figure](../assets/0e1a5f5f5eac2052.svg)

For example, if *'dark'* is selected, all pixels where the 'Dark'
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

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / int2 / int4 / uint2 / real)

Input image.

**`Region`** (output_object)  region(-array) `→` object

Segmented regions.

**`MaskWidth`** (input_control)  extent.x `→`  (integer)

Mask width for mean and deviation calculation.

Default:
15

Suggested values:
9, 11, 13, 15

Restriction:
`MaskWidth >= 1`

**`MaskHeight`** (input_control)  extent.y `→`  (integer)

Mask height for mean and deviation calculation.

Default:
15

Suggested values:
9, 11, 13, 15

Restriction:
`MaskHeight >= 1`

**`StdDevScale`** (input_control)  number `→`  (real / integer)

Factor for the standard deviation of the gray values.

Default:
0.2

Suggested values:
-0.2, -0.1, 0.1, 0.2

**`AbsThreshold`** (input_control)  number `→`  (real / integer)

Minimum gray value difference from the mean.

Default:
2

Suggested values:
-2, -1, 0, 1, 2

**`LightDark`** (input_control)  string `→`  (string)

Threshold type.

Default:
'dark'

List of values:
'dark', 'equal', 'light', 'not_equal'

## Complexity

Let A be the area of the input region, then the runtime is O(A).

## Result

`var_threshold` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior with respect to the input images and output regions can
be determined by setting the values of the flags *'no_object_result'*,
*'empty_region_result'*, and *'store_empty_region'* with
[`set_system`](set_system.md). If necessary, an exception is raised.

## Alternatives

`dyn_threshold`,
`threshold`

## References

W.Niblack, ”An Introduction to Digital Image Processing”, Page 115-116,
Englewood Cliffs, N.J., Prentice Hall, 1986

## Module

Foundation
