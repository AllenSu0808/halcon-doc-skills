# get_grayval_contour_xld (Operator)

## Name

`get_grayval_contour_xld` — Return gray values of an image at the positions of an XLD contour.

## Signature

`def get_grayval_contour_xld(image: HObject, contour: HObject, interpolation: str) -> Sequence[Union[int, float]]`

`def get_grayval_contour_xld_s(image: HObject, contour: HObject, interpolation: str) -> Union[int, float]`

## Description

The operator `get_grayval_contour_xld` returns interpolated
gray values at several subpixel positions of the *`image`*.
The coordinates of the positions are specified via one XLD contour
*`contour`*. The gray values are returned in *`grayval`*.

The interpolation method can be selected via the parameter
*`interpolation`*:

- ***"nearest_neighbor"*:** —

  The results are
  the gray values of the nearest pixels to the selected coordinates.
  For images of type byte, direction, cyclic, uint2, int1, int2,
  int4, and int8, the parameter *`grayval`* is a tuple of
  integer numbers. For images of type real and complex, the
  parameter *`grayval`* is a tuple of floating point numbers.
- ***"bilinear"*:** —

  The parameter
  *`grayval`* is computed using a bilinear interpolation of the
  four neighboring gray values of the selected coordinates. The
  result is a tuple of floating point numbers. The runtime
  increases significantly compared to *"nearest_neighbor"*.
  Direction and cyclic images are treated like byte images.
- ***"bicubic"*:** —

  The parameter
  *`grayval`* is computed using a bicubic interpolation of
  sixteen neighboring gray values of the selected coordinates. The
  result is a tuple of floating point numbers. The runtime
  increases significantly compared to *"bilinear"*.
  Direction and cyclic images are treated like byte images. In this
  mode, the resulting gray values may contain values that lie
  outside of the range of numbers that can be represented by the
  input image type.
- ***"bicubic_clipped"*:** —

  The parameter
  *`grayval`* is computed using a bicubic interpolation of
  sixteen neighboring gray values of the selected coordinates. The
  result is a tuple of floating point numbers. The runtime
  increases significantly compared to *"bilinear"*.
  Direction and cyclic images are treated like byte images. In this
  mode, resulting gray values that lie outside of the range of
  numbers that can be represented by the input image type are
  clipped to that range.

Note that `get_grayval_contour_xld` does not take the domain of
the image into account, i.e., if the domain has been reduced, e.g.,
with [`reduce_domain`](reduce_domain.md), gray values are returned even for points
that lie outside the domain.

Please note also that each point of the XLD contour must be in the
range -0.5 <= row coordinate <
height(*`image`*)-0.5 and -0.5 <= column
coordinate < width(*`image`*)-0.5.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Image whose gray values are to be accessed.

**`contour`** (input_object)  xld_cont `→` HObject

Input XLD contour with the coordinates of the
positions.

**`interpolation`** (input_control)  string `→` str

Interpolation method.

Default:
"nearest_neighbor"

List of values:
"bicubic", "bicubic_clipped", "bilinear", "nearest_neighbor"

**`grayval`** (output_control)  grayval(-array) `→` Sequence[Union[int, float]]

Gray values of the selected image coordinates.

## Result

If the parameters are valid, the operator
`get_grayval_contour_xld` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`draw_xld`,
`gen_contour_polygon_xld`,
`edges_sub_pix`

## Alternatives

`get_grayval_interpolated`

## Module

Foundation
