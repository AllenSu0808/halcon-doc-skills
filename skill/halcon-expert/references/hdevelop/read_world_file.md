# read_world_file (Operator)

## Name

`read_world_file` — Read the geo coding from an ARC/INFO world file.

## Signature

`read_world_file( : : FileName : WorldTransformation)`

## Description

`read_world_file` reads a geocoding from an ARC/INFO world
file with the file name *`FileName`* and returns it as a
homogeneous 2D transformation matrix in *`WorldTransformation`*.
To find the file *`FileName`*, all directories contained in the
HALCON system variable *'image_dir'* (usually this is the
content of the environment variable HALCONIMAGES) are searched (see
[`read_image`](read_image.md)). This transformation matrix can be used to
transform XLD contours to the world coordinate system before writing
them with [`write_contour_xld_arc_info`](write_contour_xld_arc_info.md). If the matrix
*`WorldTransformation`* is inverted by calling
[`hom_mat2d_invert`](hom_mat2d_invert.md), the resulting matrix can be used to
transform contours that have been read with
[`read_contour_xld_arc_info`](read_contour_xld_arc_info.md) to the image coordinate system.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

Name of the ARC/INFO world file.

**`WorldTransformation`** (output_control)  hom_mat2d `→`  (real)

Transformation matrix from image to world coordinates.

## Result

If the parameters are correct and the world file could be read, the
operator `read_world_file` returns the value 2 (
H_MSG_TRUE)
. Otherwise
an exception is raised.

## Possible Successors

`hom_mat2d_invert`,
`affine_trans_contour_xld`,
`affine_trans_polygon_xld`

## See also

`write_contour_xld_arc_info`,
`read_contour_xld_arc_info`,
`write_polygon_xld_arc_info`,
`read_polygon_xld_arc_info`

## Module

Foundation
