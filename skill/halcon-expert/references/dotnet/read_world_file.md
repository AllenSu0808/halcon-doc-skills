# ReadWorldFile (Operator)

## Name

`ReadWorldFile` — Read the geo coding from an ARC/INFO world file.

## Signature

`static void HOperatorSet.ReadWorldFile(HTuple fileName, out HTuple worldTransformation)`

`void HHomMat2D.ReadWorldFile(string fileName)`

## Description

`ReadWorldFile` reads a geocoding from an ARC/INFO world
file with the file name *`fileName`* and returns it as a
homogeneous 2D transformation matrix in *`worldTransformation`*.
To find the file *`fileName`*, all directories contained in the
HALCON system variable *"image_dir"* (usually this is the
content of the environment variable HALCONIMAGES) are searched (see
[`ReadImage`](read_image.md)). This transformation matrix can be used to
transform XLD contours to the world coordinate system before writing
them with [`WriteContourXldArcInfo`](write_contour_xld_arc_info.md). If the matrix
*`worldTransformation`* is inverted by calling
[`HomMat2dInvert`](hom_mat2d_invert.md), the resulting matrix can be used to
transform contours that have been read with
[`ReadContourXldArcInfo`](read_contour_xld_arc_info.md) to the image coordinate system.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the ARC/INFO world file.

**`worldTransformation`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix from image to world coordinates.

## Result

If the parameters are correct and the world file could be read, the
operator `ReadWorldFile` returns the value 2 (
H_MSG_TRUE)
. Otherwise
an exception is raised.

## Possible Successors

`HomMat2dInvert`,
`AffineTransContourXld`,
`AffineTransPolygonXld`

## See also

`WriteContourXldArcInfo`,
`ReadContourXldArcInfo`,
`WritePolygonXldArcInfo`,
`ReadPolygonXldArcInfo`

## Module

Foundation
