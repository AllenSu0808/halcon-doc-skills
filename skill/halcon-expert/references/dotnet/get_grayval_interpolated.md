# GetGrayvalInterpolated (Operator)

## Name

`GetGrayvalInterpolated` — Return gray values of an image at the positions given by tuples of
rows and columns.

## Signature

`static void HOperatorSet.GetGrayvalInterpolated(HObject image, HTuple row, HTuple column, HTuple interpolation, out HTuple grayval)`

`HTuple HImage.GetGrayvalInterpolated(HTuple row, HTuple column, string interpolation)`

`double HImage.GetGrayvalInterpolated(double row, double column, string interpolation)`

## Description

The operator `GetGrayvalInterpolated` returns interpolated
gray values at several subpixel positions of an *`image`*. The
coordinates of the row positions are given in the tuple
*`row`*, the coordinates of column positions are given in the
tuple *`column`*. The gray values are returned in
*`grayval`* as a tuple of floating point numbers.

The interpolation method can be selected via the parameter
*`interpolation`*. The following interpolation methods are
supported:

- ***"bilinear"*:** —

  The parameter
  *`grayval`* is computed using a bilinear interpolation of the
  four neighboring gray values of the selected coordinates. Note:
  direction and cyclic images are treated like byte images.
- ***"bicubic"*:** —

  The parameter
  *`grayval`* is computed using a bicubic interpolation of
  sixteen neighboring gray values of the selected coordinates.
  Direction and cyclic images are treated like byte images. In this
  mode, the resulting gray values may contain values that lie
  outside of the range of numbers that can be represented by the
  input image type.
- ***"bicubic_clipped"*:** —

  The parameter
  *`grayval`* is computed using a bicubic interpolation of
  sixteen neighboring gray values of the selected coordinates.
  Direction and cyclic images are treated like byte images. In this
  mode, resulting gray values that lie outside of the range of
  numbers that can be represented by the input image type are
  clipped to that range.

Note that `GetGrayvalInterpolated` does not take the domain of
the image into account, i.e., if the domain has been reduced, e.g.,
with [`ReduceDomain`](reduce_domain.md), gray values are returned even for points
that lie outside the domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Image whose gray values are to be accessed.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of positions.

Default:
0

Suggested values:
0, 64, 128, 256, 512, 1024

Value range:
`-0.5
≤
row`

Restriction:
`-0.5 <= Row && Row < height(Image) - 0.5`

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of positions.

Number of elements:
Column == Row

Default:
0

Suggested values:
0, 64, 128, 256, 512, 1024

Value range:
`-0.5
≤
column`

Restriction:
`-0.5 <= Column && Column < width(Image) - 0.5`

**`interpolation`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Interpolation method.

Default:
"bilinear"

List of values:
"bicubic", "bicubic_clipped", "bilinear"

**`grayval`** (output_control)  grayval(-array) `→` [HTuple](HTuple.md) (*double*)

Gray values of the selected image coordinates.

## Result

If the parameters are valid, the operator
`GetGrayvalInterpolated` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadImage`

## Alternatives

`GetGrayvalContourXld`,
`GetGrayval`

## Module

Foundation
