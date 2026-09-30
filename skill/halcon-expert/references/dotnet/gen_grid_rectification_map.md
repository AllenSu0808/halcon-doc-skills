# GenGridRectificationMap (Operator)

## Name

`GenGridRectificationMap` — Compute the mapping between the distorted image and the rectified image
based upon the points of a regular grid.

## Signature

`static void HOperatorSet.GenGridRectificationMap(HObject image, HObject connectingLines, out HObject map, out HObject meshes, HTuple gridSpacing, HTuple rotation, HTuple row, HTuple column, HTuple mapType)`

`HImage HImage.GenGridRectificationMap(HXLD connectingLines, out HXLD meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HImage.GenGridRectificationMap(HXLD connectingLines, out HXLD meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLD.GenGridRectificationMap(HImage image, out HXLD meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLD.GenGridRectificationMap(HImage image, out HXLD meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDCont.GenGridRectificationMap(HImage image, out HXLDCont meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDCont.GenGridRectificationMap(HImage image, out HXLDCont meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDPoly.GenGridRectificationMap(HImage image, out HXLDPoly meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDPoly.GenGridRectificationMap(HImage image, out HXLDPoly meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDPara.GenGridRectificationMap(HImage image, out HXLDPara meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDPara.GenGridRectificationMap(HImage image, out HXLDPara meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDModPara.GenGridRectificationMap(HImage image, out HXLDModPara meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDModPara.GenGridRectificationMap(HImage image, out HXLDModPara meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDExtPara.GenGridRectificationMap(HImage image, out HXLDExtPara meshes, int gridSpacing, HTuple rotation, HTuple row, HTuple column, string mapType)`

`HImage HXLDExtPara.GenGridRectificationMap(HImage image, out HXLDExtPara meshes, int gridSpacing, string rotation, HTuple row, HTuple column, string mapType)`

## Description

`GenGridRectificationMap` calculates the mapping between the grid
points (*`row`*,*`column`*), which have been actually detected in
the distorted image *`image`* (typically using
[`SaddlePointsSubPix`](saddle_points_sub_pix.md)), and the corresponding grid points of the
ideal regular point grid.
First, all paths that lead from their initial point via exactly four
different connecting lines back to the initial point are assembled from the
grid points (*`row`*,*`column`*) and the connecting lines
*`connectingLines`* (detected by [`ConnectGridPoints`](connect_grid_points.md)).
In case that the
input of grid points (*`row`*,*`column`*) and of connecting lines
*`connectingLines`* was meaningful, one such 'mesh' corresponds to
exactly one grid cell in the rectification grid. Afterwards, the meshes are
combined to the point grid.
According to the value of *`rotation`*, the point grid is rotated by
*0*, *90*, *180* or *270* degrees. Note that the
point grid does not necessarily have the correct orientation. When passing
*"auto"* in *`rotation`*, the point grid is rotated such that
the black circular mark in the rectification grid is positioned to the left
of the white one (see also [`CreateRectificationGrid`](create_rectification_grid.md)).
Finally, the mapping *`map`* between the distorted image and the
rectified image is calculated by interpolation between the grid points.
Each grid cell, for which the coordinates (*`row`*,*`column`*) of
all four corner points are known, is projected onto a square of
*`gridSpacing`* x *`gridSpacing`* pixels.

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

`GenGridRectificationMap` additionally returns the calculated meshes
as XLD contours in *`meshes`*.

In contrary to [`GenArbitraryDistortionMap`](gen_arbitrary_distortion_map.md),
`GenGridRectificationMap` and its predecessors are used when the
coordinates (*`row`*,*`column`*) of the grid points in the
distorted image are neither known nor can be derived from the image
contents.

If you want to re-use the created map in another program, you can save it as
a multi-channel image with the operator [`WriteImage`](write_image.md), using the format
*"tiff"*.

## Attention

Each input XLD contour *`connectingLines`* must own the global
attribute *"bright_dark"*, as it is described with
[`ConnectGridPoints`](connect_grid_points.md)!

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`connectingLines`** (input_object)  xld-array `→` [HXLD](HXLD.md)

Input contours.

**`map`** (output_object)  multichannel-image `→` [HImage](HImage.md) (int4 / uint2 / vector_field)

Image containing the mapping data.

**`meshes`** (output_object)  xld-array `→` [HXLD](HXLD.md)

Output contours.

**`gridSpacing`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Distance of the grid points in the rectified
image.

Restriction:
`GridSpacing > 0`

**`rotation`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long)

Rotation to be applied to the point grid.

Default:
"auto"

List of values:
0, 90, 180, 270, "auto"

**`row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the grid points.

**`column`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the grid points.

Restriction:
`number(Column) == number(Row)`

**`mapType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of mapping.

Default:
"bilinear"

List of values:
"bilinear", "coord_map_sub_pix"

## Result

`GenGridRectificationMap` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`ConnectGridPoints`

## Possible Successors

`MapImage`

## See also

`GenArbitraryDistortionMap`

## Module

Calibration
