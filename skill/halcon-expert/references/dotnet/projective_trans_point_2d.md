# ProjectiveTransPoint2d (Operator)

## Name

`ProjectiveTransPoint2d` — Project a homogeneous 2D point using a projective transformation
matrix.

## Signature

`static void HOperatorSet.ProjectiveTransPoint2d(HTuple homMat2D, HTuple px, HTuple py, HTuple pw, out HTuple qx, out HTuple qy, out HTuple qw)`

`HTuple HHomMat2D.ProjectiveTransPoint2d(HTuple px, HTuple py, HTuple pw, out HTuple qy, out HTuple qw)`

`double HHomMat2D.ProjectiveTransPoint2d(double px, double py, double pw, out double qy, out double qw)`

## Description

`ProjectiveTransPoint2d` applies the homogeneous projective
transformation matrix *`homMat2D`* to all homogeneous input
points (*`px`*,*`py`*,*`pw`*) and returns an array of
homogeneous output points (*`qx`*,*`qy`*,*`qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`homMat2D`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x \\ Q_y \\ Q_w\end{pmatrix}=\mathrm{HomMat2D}\cdot \begin{pmatrix}P_x \\ P_y \\ P_w\end{pmatrix}$$ ![figure](../assets/577384673df19c8d.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they have to be divided by *`qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)

If the points to transform are specified in standard image
coordinates, their *row* coordinates must be passed in
*`px`* and their *column* coordinates in *`py`*. This
is necessary to obtain a right-handed coordinate system for the
image. In particular, this assures that rotations are performed in
the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order
for coordinates in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`px`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (y coordinate).

**`pw`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (w coordinate).

**`qx`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (y coordinate).

**`qw`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (w coordinate).

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
`ProjectiveTransPixel`

## Module

Foundation
