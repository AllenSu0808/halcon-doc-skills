# point_line_to_hom_mat2d (Operator)

## Name

`point_line_to_hom_mat2d` — Approximate an affine transformation from point-to-line correspondences.

## Signature

`point_line_to_hom_mat2d( : : TransformationType, Px, Py, L1x, L1y, L2x, L2y : HomMat2D)`

## Description

`point_line_to_hom_mat2d` approximates an affine
transformation from point-to-line correspondences and returns it as
the homogeneous transformation matrix *`HomMat2D`* (see
[`hom_mat2d_to_affine_par`](hom_mat2d_to_affine_par.md) for the content of the homogeneous
transformation matrix).

The points are passed in the tuples (*`Px`*,*`Py`*).
Their corresponding lines are specified as two points on the line,
which are passed in (*`L1x`*,*`L1y`*) and
(*`L2x`*,*`L2y`*). Corresponding points and lines must be
at the same index positions in these tuples.

The type of transformation to be approximated is determined with
*`TransformationType`*. Each type of transformation requires a
certain minimum number of point-to-line correspondences, as
described in the following table:

|  |  |  |
| --- | --- | --- |
| *`TransformationType`* | Type of transformation | Minimum number of correspondences |
| *'translation'* | translation | 2 |
| *'rigid'* | rigid transformation | 3 |
| *'similarity'* | similarity transformation | 4 |
| *'aniso'* | anisotropic similarity transformation | 5 |
| *'affine'* | general affine transformation | 6 |

The types of transformations that are supported can be described as
follows:

- **'translation':** —
  A translation, i.e., a transformation that can
  be obtained as follows:

  |  |
  | --- |
  | [`hom_mat2d_identity(HomMat2D)`](hom_mat2d_identity.md) |
  | [`hom_mat2d_translate(HomMat2D, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

  This means that
  $$\mathrm{HomMat2D} = \left[\begin{array}{ccc} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{array}\right] \\ = H(T)$$ ![figure](../assets/9ed6f3878bf8353b.svg)
  where $\mathbf{T}$ is the translation
  vector.
- **'rigid':** —

  A rigid transformation, i.e., a transformation that
  can be obtained as follows:

  |  |
  | --- |
  | [`hom_mat2d_identity(HomMat2D)`](hom_mat2d_identity.md) |
  | [`hom_mat2d_rotate(HomMat2D, Phi, 0, 0, HomMat2D)`](hom_mat2d_rotate.md) |
  | [`hom_mat2d_translate(HomMat2D, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

  This means that
  $$\mathrm{HomMat2D} = \left[\begin{array}{cc} \mathbf{R} & \mathbf{T} \\ 0 & 1 \end{array}\right] \\\n= \left[\begin{array}{ccc} 1 & 0 & \mathbf{T} \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array}\right] \cdot \left[\begin{array}{cc} \mathbf{R} & 0 \\ 0 & 1 \end{array}\right] \\\n= \mathbf{H}(\mathbf{T}) \cdot \mathbf{H}(\mathbf{R})$$ ![figure](../assets/9ff68e484829559c.svg)
  where $\mathbf{R}$ is a rotation matrix
  corresponding to the rotation angle `Phi` and
  $\mathbf{T}$ is the translation vector.
- **'similarity':** —
  A similarity transformation, i.e., a
  transformation that can be obtained as follows (note the identical
  scale factors in [`hom_mat2d_scale`](hom_mat2d_scale.md)):

  |  |
  | --- |
  | [`hom_mat2d_identity(HomMat2D)`](hom_mat2d_identity.md) |
  | [`hom_mat2d_scale(HomMat2D, S, S, 0, 0, HomMat2D)`](hom_mat2d_scale.md) |
  | [`hom_mat2d_rotate(HomMat2D, Phi, 0, 0, HomMat2D)`](hom_mat2d_rotate.md) |
  | [`hom_mat2d_translate(HomMat2D, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

  This means that
  $$HomMat2D = \left[\begin{array}{ccc} R \cdot S & T \\ 0 & 0 & 1 \end{array}\right] = \left[\begin{array}{ccc} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{array}\right] \cdot \left[\begin{array}{ccc} R & 0 & 0 \\ 0 & R & 0 \\ 0 & 0 & 1 \end{array}\right] \cdot \left[\begin{array}{ccc} S & 0 & 0 \\ 0 & 0 & 1 \\end{array}\right] = H(T) \cdot H(R) \cdot H(S)$$ ![figure](../assets/ba03a78b0f4a9119.svg)
  where $\mathbf{S}$ is a scaling matrix with
  identical scaling `S` in the x and y directions,
  $\mathbf{R}$ is a rotation matrix corresponding
  to the rotation angle `Phi`, and
  $\mathbf{T}$ is the translation vector.
- **'aniso':** —
  An anisotropic similarity transformation, i.e., a
  transformation that can be obtained as follows (note the different
  scale factors in [`hom_mat2d_scale`](hom_mat2d_scale.md)):

  |  |
  | --- |
  | [`hom_mat2d_identity(HomMat2D)`](hom_mat2d_identity.md) |
  | [`hom_mat2d_scale(HomMat2D, Sx, Sy, 0, 0, HomMat2D)`](hom_mat2d_scale.md) |
  | [`hom_mat2d_rotate(HomMat2D, Phi, 0, 0, HomMat2D)`](hom_mat2d_rotate.md) |
  | [`hom_mat2d_translate(HomMat2D, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

  This means that
  $$\operatorname{HomMat2D} = \begin{bmatrix} \mathbf{R} \cdot \mathbf{S} \quad \mathbf{T} \\ 0 \ 0 \ 1 \end{bmatrix} \\quad = \\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} \mathbf{R} \\ 0 \\ 0 \end{bmatrix} \\qquad\cdot \\begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} \\quad = H(\mathbf{T}) \cdot H(\mathbf{R}) \cdot H(\mathbf{S})$$ ![figure](../assets/95d9ec338a50cc0b.svg)
  where $\mathbf{S}$ is a scaling matrix with
  non-identical scaling `Sx` and `Sy` in the x and y
  directions, $\mathbf{R}$ is a rotation matrix
  corresponding to the rotation angle `Phi`, and
  $\mathbf{T}$ is the translation vector.
- **'affine':** —
  A general affine transformation, i.e., a
  transformation that can be obtained as follows:

  |  |
  | --- |
  | [`hom_mat2d_identity(HomMat2D)`](hom_mat2d_identity.md) |
  | [`hom_mat2d_scale(HomMat2D, Sx, Sy, 0, 0, HomMat2D)`](hom_mat2d_scale.md) |
  | [`hom_mat2d_slant(HomMat2D, Theta, 'y', 0, 0, HomMat2D)`](hom_mat2d_slant.md) |
  | [`hom_mat2d_rotate(HomMat2D, Phi, 0, 0, HomMat2D)`](hom_mat2d_rotate.md) |
  | [`hom_mat2d_translate(HomMat2D, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

  This means that
  $$HomMat2D = \begin{bmatrix} h_{1,1} & h_{1,2} & h_{1,3} \\ h_{2,1} & h_{2,2} & h_{2,3} \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/5f30bac1c486535c.svg)
  where $h_{1,1} - h_{2,3}$ ![figure](../assets/b1adb29d93bf9996.svg) are arbitrary numbers.

The transformation is computed by minimizing the sum of the squared
distances of the points (*`Px`*,*`Py`*) transformed with
the computed transformation to the lines given by
(*`L1x`*,*`L1y`*) and (*`L2x`*,*`L2y`*). The
lines are regarded as lines with infinite extent. This means that
the points (*`Px`*,*`Py`*) transformed with the
transformation *`HomMat2D`* may not lie “between”
(*`L1x`*,*`L1y`*) and (*`L2x`*,*`L2y`*). An
exception to this rule occurs for rigid and anisotropic similarity
transformations that are determined from the minimum number of
point-to-line correspondences (3 and 5, respectively). In this
case, there are in general two possible solutions that both yield an
error of 0. The algorithm returns the solution for which the
transformed points lie as close as possible to the line
*segments* given by (*`L1x`*,*`L1y`*) and
(*`L2x`*,*`L2y`*). If a unique solution is desired, one
additional point-to-line correspondence should be used (i.e., 4 or
6, respectively).

*`HomMat2D`* can be used directly with operators that transform
data using affine transformations, e.g.,
[`affine_trans_image`](affine_trans_image.md).

## Attention

It should be noted that homogeneous transformation matrices refer to
a general right-handed mathematical coordinate system. If a
homogeneous transformation matrix is used to transform images,
regions, XLD contours, or any other data that has been extracted
from images, the row coordinates of the transformation must be
passed in the x coordinates, while the column coordinates must be
passed in the y coordinates. Consequently, the order of passing row
and column coordinates follows the usual order
(`Row`,`Column`). This convention is essential to
obtain a right-handed coordinate system for the transformation of
iconic data, and consequently to ensure in particular that rotations
are performed in the correct mathematical direction.

Furthermore, it should be noted that if a homogeneous transformation
matrix is used to transform images, regions, XLD contours, or any
other data that has been extracted from images, it is assumed that
the origin of the coordinate system of the homogeneous
transformation matrix lies in the upper left corner of a pixel. The
image processing operators that return point coordinates, however,
assume a coordinate system in which the origin lies in the center of
a pixel. Therefore, to obtain a consistent homogeneous
transformation matrix, 0.5 must be added to the point coordinates
before computing the transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TransformationType`** (input_control)  string `→`  (string)

Type of the transformation to compute.

Default:
'rigid'

List of values:
'affine', 'aniso', 'rigid', 'similarity', 'translation'

**`Px`** (input_control)  point.x-array `→`  (real)

X coordinates of the original points.

**`Py`** (input_control)  point.y-array `→`  (real)

Y coordinates of the original points.

**`L1x`** (input_control)  point.x-array `→`  (real)

X coordinates of the first point on the corresponding line.

**`L1y`** (input_control)  point.y-array `→`  (real)

Y coordinates of the first point on the corresponding line.

**`L2x`** (input_control)  point.x-array `→`  (real)

X coordinates of the second point on the corresponding line.

**`L2y`** (input_control)  point.y-array `→`  (real)

Y coordinates of the second point on the corresponding line.

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

Output transformation matrix.

## Example (HDevelop)

```
* Use point_line_to_hom_mat2d for alignment.
* Read the reference image.
read_image (Image, ReferenceFileName)
* Set up the metrology model with four lines.  Four lines are used
* since this is the minimum number of point-to-line correspondences
* that results in a unique rigid transformation.
Row1 := [RowB1,RowB2,RowB3,RowB4]
Col1 := [ColB1,ColB2,ColB3,ColB4]
Row2 := [RowE1,RowE2,RowE3,RowE4]
Col2 := [ColE1,ColE2,ColE3,ColE4]
create_metrology_model (MetrologyHandle)
add_metrology_object_line_measure (MetrologyHandle, Row1, Col1, \
                                   Row2, Col2, 40, 5, 1, 30, \
                                   [], [], Index)
* Apply the metrology model to the reference image and read out
* the results.
apply_metrology_model (Image, MetrologyHandle)
get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                             'result_type', 'row_begin', \
                             RowBegin)
get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                             'result_type', 'column_begin', \
                             ColBegin)
get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                             'result_type', 'row_end', \
                             RowEnd)
get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                             'result_type', 'column_end', \
                             ColEnd)
* The reference points of the model are the center points of the
* detected line segments.  They will be used to compute the
* transformation from the current image to the reference image
* using point_line_to_hom_mat2d below.
RowRef := 0.5*(RowBegin+RowEnd)
ColRef := 0.5*(ColBegin+ColEnd)
for I := 1 to |FileNames|-1 by 1
    read_image (Image, FileNames[I])
    * Apply the metrology model to the current image and read out
    * the line segment coordinates.
    apply_metrology_model (Image, MetrologyHandle)
    get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                                 'result_type', 'row_begin', \
                                 RowBegin)
    get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                                 'result_type', 'column_begin', \
                                 ColBegin)
    get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                                 'result_type', 'row_end', \
                                 RowEnd)
    get_metrology_object_result (MetrologyHandle, 'all', 'all', \
                                 'result_type', 'column_end', \
                                 ColEnd)
    * Determine a rigid transformation based on the point-to-line
    * correspondences from the reference points to the extracted
    * lines.  Note that this determines a transformation from the
    * reference points to the lines in the current image.
    * Therefore, we must invert this transformation to obtain the
    * transformation from the current image to the rerefence image.
    point_line_to_hom_mat2d ('rigid', RowRef+0.5, ColRef+0.5, \
                             RowBegin+0.5, ColBegin+0.5, \
                             RowEnd+0.5, ColEnd+0.5, HomMat2D)
    hom_mat2d_invert (HomMat2D, HomMat2DInvert)
    affine_trans_image (Image, ImageTrans, HomMat2DInvert, \
                        'constant', 'false')
    * Now that the current image has been aligned with the
    * reference image, we can do some processing based on the
    * aligned image ImageTrans.
    * [...]
endfor
```

## Possible Successors

`affine_trans_image`,
`affine_trans_image_size`,
`affine_trans_region`,
`affine_trans_contour_xld`,
`affine_trans_polygon_xld`,
`affine_trans_point_2d`

## See also

`vector_to_hom_mat2d`,
`vector_to_aniso`,
`vector_to_similarity`,
`vector_to_rigid`

## Module

Foundation
