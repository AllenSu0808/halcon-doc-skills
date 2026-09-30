# get_grayval_interpolated (Operator)

## Name

`get_grayval_interpolated` — Return gray values of an image at the positions given by tuples of
rows and columns.

## Signature

`def get_grayval_interpolated(image: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], interpolation: str) -> Sequence[float]`

`def get_grayval_interpolated_s(image: HObject, row: MaybeSequence[Union[float, int]], column: MaybeSequence[Union[float, int]], interpolation: str) -> float`

## Description

The operator `get_grayval_interpolated` returns interpolated
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

Note that `get_grayval_interpolated` does not take the domain of
the image into account, i.e., if the domain has been reduced, e.g.,
with [`reduce_domain`](reduce_domain.md), gray values are returned even for points
that lie outside the domain.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Image whose gray values are to be accessed.

**`row`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

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

**`column`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

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

**`interpolation`** (input_control)  string `→` str

Interpolation method.

Default:
"bilinear"

List of values:
"bicubic", "bicubic_clipped", "bilinear"

**`grayval`** (output_control)  grayval(-array) `→` Sequence[float]

Gray values of the selected image coordinates.

## Result

If the parameters are valid, the operator
`get_grayval_interpolated` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`

## Alternatives

`get_grayval_contour_xld`,
`get_grayval`

## Module

Foundation
