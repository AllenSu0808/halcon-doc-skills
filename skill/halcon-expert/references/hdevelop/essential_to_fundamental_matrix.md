# essential_to_fundamental_matrix (Operator)

## Name

`essential_to_fundamental_matrix` — Compute the fundamental matrix from an essential matrix.

## Signature

`essential_to_fundamental_matrix( : : EMatrix, CovEMat, CamMat1, CamMat2 : FMatrix, CovFMat)`

## Description

The fundamental matrix is the entity describing the epipolar constraint
in image coordinates (C,R) and the essential matrix is its counterpart
for 3D direction vectors (X,Y,1):
$$\begin{pmatrix}C_{2}\\R_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{FMatrix}\cdot\begin{pmatrix}C_{1}\\R_{1}\\1\end{pmatrix}=0 \quad\text{and}\quad \begin{pmatrix}X_{2}\\Y_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{EMatrix}\cdot\begin{pmatrix}X_{1}\\Y_{1}\\1\end{pmatrix}=0$$ ![figure](../assets/a8218fd1ba85e608.svg)
Image coordinates result from 3D direction vectors by
multiplication with the camera matrix CamMat:
$$\begin{pmatrix} \text{col} \\ \text{row} \\ 1 \end{pmatrix} = CamMat \cdot \begin{pmatrix} X \\ Y \\ 1 \end{pmatrix} .$$ ![figure](../assets/ff4715e8455e90f3.svg)
Therefore, the fundamental matrix *`FMatrix`* is calculated from the
essential matrix *`EMatrix`* and the camera matrices *`CamMat1`*,
*`CamMat2`* by the following formula:
$$\texttt{FMatrix}=\texttt{CamMat2}^{-T}\cdot\texttt{EMatrix}\cdot\texttt{CamMat1}^{-1}.$$
The transformation of the essential matrix to the fundamental matrix
goes along with the propagation of the covariance matrices *`CovEMat`*
to *`CovFMat`*. If *`CovEMat`* is empty *`CovFMat`* will be
empty too.

The conversion operator `essential_to_fundamental_matrix` is used
especially for a subsequent visualization of the epipolar line structure
via the fundamental matrix, which depicts the underlying stereo geometry.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EMatrix`** (input_control)  hom_mat2d `→`  (real / integer)

Essential matrix.

**`CovEMat`** (input_control)  number-array `→`  (real / integer)

9x9 covariance matrix of the
essential matrix.

Default:
[]

**`CamMat1`** (input_control)  hom_mat2d `→`  (real / integer)

Camera matrix of the 1. camera.

**`CamMat2`** (input_control)  hom_mat2d `→`  (real / integer)

Camera matrix of the 2. camera.

**`FMatrix`** (output_control)  hom_mat2d `→`  (real)

Computed fundamental matrix.

**`CovFMat`** (output_control)  real-array `→`  (real)

9x9 covariance matrix of the
fundamental matrix.

## Possible Predecessors

`vector_to_essential_matrix`

## Alternatives

`rel_pose_to_fundamental_matrix`

## Module

3D Metrology
