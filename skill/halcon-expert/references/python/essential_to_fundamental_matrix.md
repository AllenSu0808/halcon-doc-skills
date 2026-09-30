# essential_to_fundamental_matrix (Operator)

## Name

`essential_to_fundamental_matrix` — Compute the fundamental matrix from an essential matrix.

## Signature

`def essential_to_fundamental_matrix(ematrix: Sequence[Union[float, int]], cov_emat: Sequence[Union[float, int]], cam_mat_1: Sequence[Union[float, int]], cam_mat_2: Sequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

## Description

The fundamental matrix is the entity describing the epipolar constraint
in image coordinates (C,R) and the essential matrix is its counterpart
for 3D direction vectors (X,Y,1):
$$\begin{pmatrix}C_{2}\\R_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{FMatrix}\cdot\begin{pmatrix}C_{1}\\R_{1}\\1\end{pmatrix}=0 \quad\text{and}\quad \begin{pmatrix}X_{2}\\Y_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{EMatrix}\cdot\begin{pmatrix}X_{1}\\Y_{1}\\1\end{pmatrix}=0$$ ![figure](../assets/a8218fd1ba85e608.svg)
Image coordinates result from 3D direction vectors by
multiplication with the camera matrix CamMat:
$$\begin{pmatrix} \text{col} \\ \text{row} \\ 1 \end{pmatrix} = CamMat \cdot \begin{pmatrix} X \\ Y \\ 1 \end{pmatrix} .$$ ![figure](../assets/ff4715e8455e90f3.svg)
Therefore, the fundamental matrix *`fmatrix`* is calculated from the
essential matrix *`ematrix`* and the camera matrices *`cam_mat_1`*,
*`cam_mat_2`* by the following formula:
$$\texttt{FMatrix}=\texttt{CamMat2}^{-T}\cdot\texttt{EMatrix}\cdot\texttt{CamMat1}^{-1}.$$
The transformation of the essential matrix to the fundamental matrix
goes along with the propagation of the covariance matrices *`cov_emat`*
to *`cov_fmat`*. If *`cov_emat`* is empty *`cov_fmat`* will be
empty too.

The conversion operator `essential_to_fundamental_matrix` is used
especially for a subsequent visualization of the epipolar line structure
via the fundamental matrix, which depicts the underlying stereo geometry.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ematrix`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Essential matrix.

**`cov_emat`** (input_control)  number-array `→` Sequence[Union[float, int]]

9x9 covariance matrix of the
essential matrix.

Default:
[]

**`cam_mat_1`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Camera matrix of the 1. camera.

**`cam_mat_2`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Camera matrix of the 2. camera.

**`fmatrix`** (output_control)  hom_mat2d `→` Sequence[float]

Computed fundamental matrix.

**`cov_fmat`** (output_control)  real-array `→` Sequence[float]

9x9 covariance matrix of the
fundamental matrix.

## Possible Predecessors

`vector_to_essential_matrix`

## Alternatives

`rel_pose_to_fundamental_matrix`

## Module

3D Metrology
