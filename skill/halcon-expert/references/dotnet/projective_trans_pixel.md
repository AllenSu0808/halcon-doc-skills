# ProjectiveTransPixel (Operator)

## Name

`ProjectiveTransPixel` — Project pixel coordinates using a homogeneous projective
transformation matrix.

## Signature

`static void HOperatorSet.ProjectiveTransPixel(HTuple homMat2D, HTuple row, HTuple col, out HTuple rowTrans, out HTuple colTrans)`

`void HHomMat2D.ProjectiveTransPixel(HTuple row, HTuple col, out HTuple rowTrans, out HTuple colTrans)`

`void HHomMat2D.ProjectiveTransPixel(double row, double col, out double rowTrans, out double colTrans)`

## Description

`ProjectiveTransPixel` applies the homogeneous projective
transformation matrix *`homMat2D`* to all input pixels
(*`row`*,*`col`*) and returns an array of output pixels
(*`rowTrans`*,*`colTrans`*). The transformation is
described by the homogeneous transformation matrix given in
*`homMat2D`*.

The difference between `ProjectiveTransPixel` and
[`ProjectiveTransPoint2d`](projective_trans_point_2d.md) lies in the used coordinate
system: `ProjectiveTransPixel` uses a coordinate system with
origin in the upper left corner of the image, while
[`ProjectiveTransPoint2d`](projective_trans_point_2d.md) uses the standard image coordinate
system, whose origin lies in the middle of the upper left pixel and
which is also used by operators like [`AreaCenter`](area_center.md).

`ProjectiveTransPixel` corresponds to the following steps
(input and output points as homogeneous vectors):
$$\begin{pmatrix} \mathrm{RTrans} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \end{pmatrix} = \mathrm{HomMat2D} \cdot \begin{pmatrix} \mathrm{Row} \\ \mathrm{Col} \\ 1 \end{pmatrix} \\ \begin{pmatrix} \mathrm{RTrans} \\ \mathrm{WTrans} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \end{pmatrix} = \begin{pmatrix} \frac{\mathrm{RTrans}}{\mathrm{WTrans}} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \\ \mathrm{WTrans} \end{pmatrix}$$ ![figure](../assets/8aca13c0098d86cd.svg)

If a point at infinity (`WTrans` = 0) is created by the
transformation, an error is returned.

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

Homogeneous projective transformation matrix.

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

## Possible Predecessors

`VectorToProjHomMat2d`,
`HomVectorToProjHomMat2d`,
`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`,
`HomMat3dProject`

## See also

`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`

## Module

Foundation
