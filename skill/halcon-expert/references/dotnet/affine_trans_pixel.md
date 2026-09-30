# AffineTransPixel (Operator)

## Name

`AffineTransPixel` — Apply an arbitrary affine 2D transformation to pixel coordinates.

## Signature

`static void HOperatorSet.AffineTransPixel(HTuple homMat2D, HTuple row, HTuple col, out HTuple rowTrans, out HTuple colTrans)`

`void HHomMat2D.AffineTransPixel(HTuple row, HTuple col, out HTuple rowTrans, out HTuple colTrans)`

`void HHomMat2D.AffineTransPixel(double row, double col, out double rowTrans, out double colTrans)`

## Description

`AffineTransPixel` applies an arbitrary affine 2D transformation,
i.e., scaling, rotation, translation, and slant (skewing), to the input
pixels (*`row`*,*`col`*) and returns the resulting pixels in
(*`rowTrans`*,*`colTrans`*); the input and output pixels are
subpixel precise coordinates. The affine transformation is described by the
homogeneous transformation matrix given in *`homMat2D`*.

In contrast to [`AffineTransPoint2d`](affine_trans_point_2d.md), `AffineTransPixel`
first converts the input coordinates from HALCON's standard coordinate
system (with the origin in the center of the upper left pixel) to a coordinate
system with the origin in the upper left corner of the upper left pixel. After
the transformation with *`homMat2D`* the result is converted back to
the standard coordinate system.
This way, `AffineTransPixel` is compatible with
[`AffineTransImage`](affine_trans_image.md), [`AffineTransImageSize`](affine_trans_image_size.md),
[`AffineTransRegion`](affine_trans_region.md), [`AffineTransContourXld`](affine_trans_contour_xld.md), and
[`AffineTransPolygonXld`](affine_trans_polygon_xld.md).

Applying `AffineTransPixel` corresponds to the following chain of
transformations (input and output pixels as homogeneous vectors):

$$\begin{pmatrix} RowTrans \\ ColTrans \\ 1 \end{pmatrix} = \begin{bmatrix} 1 & 0 & -0.5 \\ 0 & 1 & -0.5 \\ 0 & 0 & 1 \end{bmatrix} \cdot HoMMat2D \cdot \begin{bmatrix} 1 & 0 & +0.5 \\ 0 & 1 & +0.5 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{pmatrix} Row \\ Col \\ 1 \end{pmatrix}$$ ![figure](../assets/872f437a811bcdf8.svg)

Hence, `AffineTransPixel(HomMat2D, Row, Col, RowTrans, ColTrans)`
corresponds to the following operator sequence:

|  |
| --- |
| [`AffineTransPoint2d(HomMat2D, Row+0.5, Col+0.5, RowTmp, ColTmp)`](affine_trans_point_2d.md) |
| `RowTrans := RowTmp-0.5` |
| `ColTrans := ColTmp-0.5` |

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`row`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input pixel(s) (row coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`col`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input pixel(s) (column coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`rowTrans`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Output pixel(s) (row coordinate).

**`colTrans`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Output pixel(s) (column coordinate).

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation),
`AffineTransPixel` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception
is raised.

## Possible Predecessors

`HomMat2dTranslate`,
`HomMat2dTranslateLocal`,
`HomMat2dScale`,
`HomMat2dScaleLocal`,
`HomMat2dRotate`,
`HomMat2dRotateLocal`,
`HomMat2dSlant`,
`HomMat2dSlantLocal`,
`HomMat2dReflect`,
`HomMat2dReflectLocal`

## Alternatives

`AffineTransPoint2d`

## Module

Foundation
