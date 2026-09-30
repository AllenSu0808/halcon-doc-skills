# gen_grid_rectification_map (Operator)

## Name

`gen_grid_rectification_map` — Compute the mapping between the distorted image and the rectified image
based upon the points of a regular grid.

## Signature

`def gen_grid_rectification_map(image: HObject, connecting_lines: HObject, grid_spacing: int, rotation: Union[str, int], row: Sequence[float], column: Sequence[float], map_type: str) -> Tuple[HObject, HObject]`

## Description

`gen_grid_rectification_map` calculates the mapping between the grid
points (*`row`*,*`column`*), which have been actually detected in
the distorted image *`image`* (typically using
[`saddle_points_sub_pix`](saddle_points_sub_pix.md)), and the corresponding grid points of the
ideal regular point grid.
First, all paths that lead from their initial point via exactly four
different connecting lines back to the initial point are assembled from the
grid points (*`row`*,*`column`*) and the connecting lines
*`connecting_lines`* (detected by [`connect_grid_points`](connect_grid_points.md)).
In case that the
input of grid points (*`row`*,*`column`*) and of connecting lines
*`connecting_lines`* was meaningful, one such 'mesh' corresponds to
exactly one grid cell in the rectification grid. Afterwards, the meshes are
combined to the point grid.
According to the value of *`rotation`*, the point grid is rotated by
*0*, *90*, *180* or *270* degrees. Note that the
point grid does not necessarily have the correct orientation. When passing
*"auto"* in *`rotation`*, the point grid is rotated such that
the black circular mark in the rectification grid is positioned to the left
of the white one (see also [`create_rectification_grid`](create_rectification_grid.md)).
Finally, the mapping *`map`* between the distorted image and the
rectified image is calculated by interpolation between the grid points.
Each grid cell, for which the coordinates (*`row`*,*`column`*) of
all four corner points are known, is projected onto a square of
*`grid_spacing`* x *`grid_spacing`* pixels.

*`map_type`* is used to specify the type of the output *`map`*.
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

`gen_grid_rectification_map` additionally returns the calculated meshes
as XLD contours in *`meshes`*.

In contrary to [`gen_arbitrary_distortion_map`](gen_arbitrary_distortion_map.md),
`gen_grid_rectification_map` and its predecessors are used when the
coordinates (*`row`*,*`column`*) of the grid points in the
distorted image are neither known nor can be derived from the image
contents.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`write_image`](write_image.md), using the format
*"tiff"*.

## Attention

Each input XLD contour *`connecting_lines`* must own the global
attribute *"bright_dark"*, as it is described with
[`connect_grid_points`](connect_grid_points.md)!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image.

**`connecting_lines`** (input_object)  xld-array `→` HObject

Input contours.

**`map`** (output_object)  multichannel-image `→` HObject (int4 / uint2 / vector_field)

Image containing the mapping data.

**`meshes`** (output_object)  xld-array `→` HObject

Output contours.

**`grid_spacing`** (input_control)  integer `→` int

Distance of the grid points in the rectified
image.

Restriction:
`GridSpacing > 0`

**`rotation`** (input_control)  string `→` Union[str, int]

Rotation to be applied to the point grid.

Default:
"auto"

List of values:
0, 90, 180, 270, "auto"

**`row`** (input_control)  point.y-array `→` Sequence[float]

Row coordinates of the grid points.

**`column`** (input_control)  point.x-array `→` Sequence[float]

Column coordinates of the grid points.

Restriction:
`number(Column) == number(Row)`

**`map_type`** (input_control)  string `→` str

Type of mapping.

Default:
"bilinear"

List of values:
"bilinear", "coord_map_sub_pix"

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
