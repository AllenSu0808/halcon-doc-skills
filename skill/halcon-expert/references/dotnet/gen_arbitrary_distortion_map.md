# GenArbitraryDistortionMap (Operator)

## Name

`GenArbitraryDistortionMap` — Generate a projection map that describes the mapping between an arbitrarily
distorted image and the rectified image.

## Signature

`static void HOperatorSet.GenArbitraryDistortionMap(out HObject map, HTuple gridSpacing, HTuple row, HTuple column, HTuple gridWidth, HTuple imageWidth, HTuple imageHeight, HTuple mapType)`

`static HImage HMisc.GenArbitraryDistortionMap(int gridSpacing, HTuple row, HTuple column, int gridWidth, int imageWidth, int imageHeight, string mapType)`

## Description

`GenArbitraryDistortionMap` computes the mapping *`map`*
between an arbitrarily distorted image and the rectified image.
The coordinates *`row`* and *`column`* describe a distorted grid,
which will be mapped onto a regular grid in the rectified image.
The coordinates of the (distorted) grid points must be passed line by line
in *`row`* and *`column`*. *`gridWidth`* is the width of the
point grid in grid points. *`gridSpacing`* is the distance between
two adjacent grid points in the rectified image. Because the grid points
are always mapped to the centers of their corresponding pixels a grid cell
requires (*`gridSpacing`*+1) x (*`gridSpacing`*+1) pixels in the
rectified image. Note however, that, of course, adjacent grid cells
overlap by one pixel.

To compute the mapping *`map`*, additionally the width
*`imageWidth`* and height *`imageHeight`* of the images to be
rectified must be passed.

*`mapType`* is used to specify the type of the output *`map`*.
If *"bilinear"* interpolation
is chosen, *`map`* consists of one image containing five channels.
In the first channel for each pixel in the resulting image the linearized
coordinates of the pixel in the input image is stored that is in the upper
left position relative to the transformed coordinates.
The four other channels contain the weights of the four neighboring pixels
of the transformed coordinates which are used for the bilinear interpolation,
in the following order:

|  |  |
| --- | --- |
| 2 | 3 |
| 4 | 5 |

The second channel, for example, contains the weights of the pixels that
lie to the upper left relative to the transformed coordinates.
If *"coord_map_sub_pix"* is chosen, *`map`* consists of
one vector field image, in which for each pixel of the resulting image
the subpixel precise coordinates in the input image are stored.

As mentioned above, four adjacent pixels in the distorted image are required
to interpolate the gray value of one pixel in the mapped image. If at
least one of these pixels is located outside of the distorted image the
gray value can not be calculated. The domain of the resulting *`map`*
domain is reduced accordingly.

In contrary to [`GenGridRectificationMap`](gen_grid_rectification_map.md),
`GenArbitraryDistortionMap` is used when the coordinates
(*`row`*,*`column`*) of the grid points in the distorted image are
already known or the relevant part of the image consist of regular grid
structures, which the coordinates can be derived from.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`WriteImage`](write_image.md), using the format
*"tiff"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`map`** (output_object)  multichannel-image `→` [HImage](HImage.md) (int4 / uint2 / vector_field)

Image containing the mapping data.

**`gridSpacing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Distance of the grid points in the rectified
image.

Restriction:
`GridSpacing > 0`

**`row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the grid points in the distorted
image.

**`column`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the grid points in the distorted
image.

Restriction:
`number(Row) == number(Column)`

**`gridWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the point grid (number of grid points).

**`imageWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the images to be rectified.

Restriction:
`ImageWidth > 0`

**`imageHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the images to be rectified.

Restriction:
`ImageHeight > 0`

**`mapType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of mapping.

Default:
"bilinear"

List of values:
"bilinear", "coord_map_sub_pix"

## Result

`GenArbitraryDistortionMap` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Successors

`MapImage`

## See also

`CreateRectificationGrid`,
`FindRectificationGrid`,
`ConnectGridPoints`,
`GenGridRectificationMap`

## Module

Calibration
