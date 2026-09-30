# gen_grid_rectification_map (Operator)

## Name

`gen_grid_rectification_map` — Compute the mapping between the distorted image and the rectified image
based upon the points of a regular grid.

## Signature

`gen_grid_rectification_map(Image, ConnectingLines : Map, Meshes : GridSpacing, Rotation, Row, Column, MapType : )`

## Description

`gen_grid_rectification_map` calculates the mapping between the grid
points (*`Row`*,*`Column`*), which have been actually detected in
the distorted image *`Image`* (typically using
[`saddle_points_sub_pix`](saddle_points_sub_pix.md)), and the corresponding grid points of the
ideal regular point grid.
First, all paths that lead from their initial point via exactly four
different connecting lines back to the initial point are assembled from the
grid points (*`Row`*,*`Column`*) and the connecting lines
*`ConnectingLines`* (detected by [`connect_grid_points`](connect_grid_points.md)).
In case that the
input of grid points (*`Row`*,*`Column`*) and of connecting lines
*`ConnectingLines`* was meaningful, one such 'mesh' corresponds to
exactly one grid cell in the rectification grid. Afterwards, the meshes are
combined to the point grid.
According to the value of *`Rotation`*, the point grid is rotated by
*0*, *90*, *180* or *270* degrees. Note that the
point grid does not necessarily have the correct orientation. When passing
*'auto'* in *`Rotation`*, the point grid is rotated such that
the black circular mark in the rectification grid is positioned to the left
of the white one (see also [`create_rectification_grid`](create_rectification_grid.md)).
Finally, the mapping *`Map`* between the distorted image and the
rectified image is calculated by interpolation between the grid points.
Each grid cell, for which the coordinates (*`Row`*,*`Column`*) of
all four corner points are known, is projected onto a square of
*`GridSpacing`* x *`GridSpacing`* pixels.

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

`gen_grid_rectification_map` additionally returns the calculated meshes
as XLD contours in *`Meshes`*.

In contrary to [`gen_arbitrary_distortion_map`](gen_arbitrary_distortion_map.md),
`gen_grid_rectification_map` and its predecessors are used when the
coordinates (*`Row`*,*`Column`*) of the grid points in the
distorted image are neither known nor can be derived from the image
contents.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`write_image`](write_image.md), using the format
*'tiff'*.

## Attention

Each input XLD contour *`ConnectingLines`* must own the global
attribute *'bright_dark'*, as it is described with
[`connect_grid_points`](connect_grid_points.md)!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`ConnectingLines`** (input_object)  xld-array `→` object

Input contours.

**`Map`** (output_object)  multichannel-image `→` object (int4 / uint2 / vector_field)

Image containing the mapping data.

**`Meshes`** (output_object)  xld-array `→` object

Output contours.

**`GridSpacing`** (input_control)  integer `→`  (integer)

Distance of the grid points in the rectified
image.

Restriction:
`GridSpacing > 0`

**`Rotation`** (input_control)  string `→`  (string / integer)

Rotation to be applied to the point grid.

Default:
'auto'

List of values:
0, 90, 180, 270, 'auto'

**`Row`** (input_control)  point.y-array `→`  (real)

Row coordinates of the grid points.

**`Column`** (input_control)  point.x-array `→`  (real)

Column coordinates of the grid points.

Restriction:
`number(Column) == number(Row)`

**`MapType`** (input_control)  string `→`  (string)

Type of mapping.

Default:
'bilinear'

List of values:
'bilinear', 'coord_map_sub_pix'

## Result

`gen_grid_rectification_map` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`connect_grid_points`

## Possible Successors

`map_image`

## See also

`gen_arbitrary_distortion_map`

## Module

Calibration
