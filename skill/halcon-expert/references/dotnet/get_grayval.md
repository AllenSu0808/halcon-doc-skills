# GetGrayval (Operator)

## Name

`GetGrayval` — Access the gray values of an image object.

## Signature

`static void HOperatorSet.GetGrayval(HObject image, HTuple row, HTuple column, out HTuple grayval)`

`HTuple HImage.GetGrayval(HTuple row, HTuple column)`

`HTuple HImage.GetGrayval(int row, int column)`

## Description

The parameter *`grayval`* is a tuple of floating point numbers
or integer numbers which returns the gray values of several pixels
of *`image`*. For a multi-channel image, a group of elements,
in particular one value for each channel (or two values for each
channel for complex or vector field images), is returned for each
pixel. The row coordinates of the pixels are specified in the tuple
*`row`*, the column coordinates are specified in the tuple
*`column`*.

Note that `GetGrayval` does not take the domain of the image
into account, i.e., if the domain has been reduced, e.g., with
[`ReduceDomain`](reduce_domain.md), gray values are returned even for points that
lie outside the domain.

## Attention

The type of the values of *`grayval`* depends on the type of
the gray values of the channels of the image *`image`*. The
operator `GetGrayval` produces quite some overhead.
Typically, it is used to get single gray values of an image (e.g.,
[`GetMposition`](get_mposition.md) followed by `GetGrayval`). It is not
suitable for programming image processing operations such as
filters. In this case it is more useful to use the operator
[`GetImagePointer1`](get_image_pointer1.md) and to directly use the C or C++
interface for integrating own procedures.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real / complex / vector_field)

Image whose gray value is to be accessed.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Row coordinates of pixels to be viewed.

Default:
0

Suggested values:
0, 64, 128, 256, 512, 1024

Value range:
`0
≤
row
≤
32767` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`0 <= Row && Row < height(Image)`

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Column coordinates of pixels to be viewed.

Number of elements:
Column == Row

Default:
0

Suggested values:
0, 64, 128, 256, 512, 1024

Value range:
`0
≤
column
≤
32767` (lin)

Minimum increment:
1

Recommended increment:
1

Restriction:
`0 <= Column && Column < width(Image)`

**`grayval`** (output_control)  grayval-array `→` [HTuple](HTuple.md) (*double* / int / long)

Gray values of indicated pixels.

## Result

If the state of the parameters is correct, the operator
`GetGrayval` returns the value 2 (
H_MSG_TRUE)
. The behavior in case of
empty input (no input images available) is set via the operator
`set_system('no_object_result',<Result>)`. If necessary, an
exception is raised.

## Possible Predecessors

`ReadImage`

## Alternatives

`GetImagePointer1`,
`GetGrayvalInterpolated`,
`GetGrayvalContourXld`

## See also

`SetGrayval`

## Module

Foundation
