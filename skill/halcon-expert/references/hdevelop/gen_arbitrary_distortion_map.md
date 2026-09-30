# gen_arbitrary_distortion_map (Operator)

## Name

`gen_arbitrary_distortion_map` — Generate a projection map that describes the mapping between an arbitrarily
distorted image and the rectified image.

## Signature

`gen_arbitrary_distortion_map( : Map : GridSpacing, Row, Column, GridWidth, ImageWidth, ImageHeight, MapType : )`

## Description

`gen_arbitrary_distortion_map` computes the mapping *`Map`*
between an arbitrarily distorted image and the rectified image.
The coordinates *`Row`* and *`Column`* describe a distorted grid,
which will be mapped onto a regular grid in the rectified image.
The coordinates of the (distorted) grid points must be passed line by line
in *`Row`* and *`Column`*. *`GridWidth`* is the width of the
point grid in grid points. *`GridSpacing`* is the distance between
two adjacent grid points in the rectified image. Because the grid points
are always mapped to the centers of their corresponding pixels a grid cell
requires (*`GridSpacing`*+1) x (*`GridSpacing`*+1) pixels in the
rectified image. Note however, that, of course, adjacent grid cells
overlap by one pixel.

To compute the mapping *`Map`*, additionally the width
*`ImageWidth`* and height *`ImageHeight`* of the images to be
rectified must be passed.

*`MapType`* is used to specify the type of the output *`Map`*.
If *'bilinear'* interpolation
is chosen, *`Map`* consists of one image containing five channels.
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
If *'coord_map_sub_pix'* is chosen, *`Map`* consists of
one vector field image, in which for each pixel of the resulting image
the subpixel precise coordinates in the input image are stored.

As mentioned above, four adjacent pixels in the distorted image are required
to interpolate the gray value of one pixel in the mapped image. If at
least one of these pixels is located outside of the distorted image the
gray value can not be calculated. The domain of the resulting *`Map`*
domain is reduced accordingly.

In contrary to [`gen_grid_rectification_map`](gen_grid_rectification_map.md),
`gen_arbitrary_distortion_map` is used when the coordinates
(*`Row`*,*`Column`*) of the grid points in the distorted image are
already known or the relevant part of the image consist of regular grid
structures, which the coordinates can be derived from.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`write_image`](write_image.md), using the format
*'tiff'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Map`** (output_object)  multichannel-image `→` object (int4 / uint2 / vector_field)

Image containing the mapping data.

**`GridSpacing`** (input_control)  integer `→`  (integer)

Distance of the grid points in the rectified
image.

Restriction:
`GridSpacing > 0`

**`Row`** (input_control)  point.y-array `→`  (real)

Row coordinates of the grid points in the distorted
image.

**`Column`** (input_control)  point.x-array `→`  (real)

Column coordinates of the grid points in the distorted
image.

Restriction:
`number(Row) == number(Column)`

**`GridWidth`** (input_control)  integer `→`  (integer)

Width of the point grid (number of grid points).

**`ImageWidth`** (input_control)  extent.x `→`  (integer)

Width of the images to be rectified.

Restriction:
`ImageWidth > 0`

**`ImageHeight`** (input_control)  extent.y `→`  (integer)

Height of the images to be rectified.

Restriction:
`ImageHeight > 0`

**`MapType`** (input_control)  string `→`  (string)

Type of mapping.

Default:
'bilinear'

List of values:
'bilinear', 'coord_map_sub_pix'

## Result

`gen_arbitrary_distortion_map` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Successors

`map_image`

## See also

`create_rectification_grid`,
`find_rectification_grid`,
`connect_grid_points`,
`gen_grid_rectification_map`

## Module

Calibration
