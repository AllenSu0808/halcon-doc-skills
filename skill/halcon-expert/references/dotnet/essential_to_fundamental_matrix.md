# EssentialToFundamentalMatrix (Operator)

## Name

`EssentialToFundamentalMatrix` — Compute the fundamental matrix from an essential matrix.

## Signature

`static void HOperatorSet.EssentialToFundamentalMatrix(HTuple EMatrix, HTuple covEMat, HTuple camMat1, HTuple camMat2, out HTuple FMatrix, out HTuple covFMat)`

`HHomMat2D HHomMat2D.EssentialToFundamentalMatrix(HTuple covEMat, HHomMat2D camMat1, HHomMat2D camMat2, out HTuple covFMat)`

## Description

The fundamental matrix is the entity describing the epipolar constraint
in image coordinates (C,R) and the essential matrix is its counterpart
for 3D direction vectors (X,Y,1):
$$\begin{pmatrix}C_{2}\\R_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{FMatrix}\cdot\begin{pmatrix}C_{1}\\R_{1}\\1\end{pmatrix}=0 \quad\text{and}\quad \begin{pmatrix}X_{2}\\Y_{2}\\1\end{pmatrix}^{T} \cdot\mathrm{EMatrix}\cdot\begin{pmatrix}X_{1}\\Y_{1}\\1\end{pmatrix}=0$$ ![figure](../assets/a8218fd1ba85e608.svg)
Image coordinates result from 3D direction vectors by
multiplication with the camera matrix CamMat:
$$\begin{pmatrix} \text{col} \\ \text{row} \\ 1 \end{pmatrix} = CamMat \cdot \begin{pmatrix} X \\ Y \\ 1 \end{pmatrix} .$$ ![figure](../assets/ff4715e8455e90f3.svg)
Therefore, the fundamental matrix *`FMatrix`* is calculated from the
essential matrix *`EMatrix`* and the camera matrices *`camMat1`*,
*`camMat2`* by the following formula:
$$\texttt{FMatrix}=\texttt{CamMat2}^{-T}\cdot\texttt{EMatrix}\cdot\texttt{CamMat1}^{-1}.$$
The transformation of the essential matrix to the fundamental matrix
goes along with the propagation of the covariance matrices *`covEMat`*
to *`covFMat`*. If *`covEMat`* is empty *`covFMat`* will be
empty too.

The conversion operator `EssentialToFundamentalMatrix` is used
especially for a subsequent visualization of the epipolar line structure
via the fundamental matrix, which depicts the underlying stereo geometry.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`EMatrix`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double* / int / long)

Essential matrix.

**`covEMat`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

9x9 covariance matrix of the
essential matrix.

Default:
[]

**`camMat1`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double* / int / long)

Camera matrix of the 1. camera.

**`camMat2`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double* / int / long)

Camera matrix of the 2. camera.

**`FMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed fundamental matrix.

**`covFMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
fundamental matrix.

## Possible Predecessors

`VectorToEssentialMatrix`

## Alternatives

`RelPoseToFundamentalMatrix`

## Module

3D Metrology
