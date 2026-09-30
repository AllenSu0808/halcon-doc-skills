# orthogonal_decompose_matrix (Operator)

## Name

`orthogonal_decompose_matrix` — Perform an orthogonal decomposition of a matrix.

## Signature

`def orthogonal_decompose_matrix(matrix_id: HHandle, decomposition_type: str, output_matrices_type: str, compute_orthogonal: str) -> Tuple[HHandle, HHandle]`

## Description

The operator `orthogonal_decompose_matrix` decomposes the
`Matrix` defined by the matrix handle *`matrix_id`*. The
results are stored in the two generated matrices
`MatrixOrthogonal` and `MatrixTriangular`. The
operator returns the matrix handles *`matrix_orthogonal_id`* and
*`matrix_triangular_id`* of these two matrices. Access
to the elements of the matrices is possible e.g., with the operator
[`get_full_matrix`](get_full_matrix.md).

For *`output_matrices_type`* = *"full"* all results of
the decomposition are stored in the matrices
`MatrixOrthogonal` and `MatrixTriangular`. For
*`output_matrices_type`* = *"reduced"* only a part of
result elements of the matrices `MatrixOrthogonal` and
`MatrixTriangular` are stored. Therefore the sizes of these
matrices are smaller than for *`output_matrices_type`* =
*"full"*.

For the parameter *`compute_orthogonal`* = *"true"* both
output matrices are computed. For the *`compute_orthogonal`* =
*"false"* only the matrix `MatrixTriangular` is
computed. Thus, the runtime of the operation takes fewer time.

The type of the `Matrix` can be selected via the parameter
*`decomposition_type`*. For *`decomposition_type`* =
*"qr"* a QR decomposition (Quadratic/Right) or for
*`decomposition_type`* = *"ql"* a QL decomposition
(Quadratic/Left) is computed. The decomposition is
written as
$$\texttt{Matrix}=\texttt{MatrixOrthogonal}\cdot\texttt{MatrixTriangular}.$$

*Example:*

*`decomposition_type`* = *"qr"*,
*`output_matrices_type`* = *"full"*
$$\mathrm{Matrix} = \begin{bmatrix}6.0 & -3.0 & 4.0\\ 5.0 & 5.0 & -2.0\\ -3.0 & 12.0 & 5.0\\ 3.0 & 4.0 & 7.0\\ 7.0 & 5.0 & 3.0\end{bmatrix}$$ ![figure](../assets/c58094ba032e2df7.svg)
$$\rightarrow\quad \mathrm{MatrixOrthogonal} = \left[\begin{array}{rrrrr} -0.5303 & 0.2613 & -0.4277 & -0.5566 & -0.3972 \\ -0.4419 & -0.2920 & -0.6383 & 0.1727 & -0.5312 \\ 0.2652 & -0.8443 & -0.2059 & -0.3961 & -0.1326 \\ -0.2652 & -0.2432 & -0.6008 & 0.7000 & -0.1400 \\ -0.6187 & -0.2729 & 0.0799 & -0.1160 & 0.7231 \\ \end{array}\right] \quad\text{MatrixTriangular} = \left[\begin{array}{ccc} -11.3137 & -1.5910 & -3.6239 \\ 0 & -14.7129 & -5.1135 \\ 0 & 0 & -7.9824 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ \end{array}\right]$$ ![figure](../assets/d4cd66dc2a9daf49.svg)

*Example:*

*`decomposition_type`* = *"qr"*,
*`output_matrices_type`* = *"reduced"*
$$\mathrm{Matrix} = \begin{bmatrix}6.0 & -3.0 & 4.0\\ 5.0 & 5.0 & -2.0\\ -3.0 & 12.0 & 5.0\\ 3.0 & 4.0 & 7.0\\ 7.0 & 5.0 & 3.0\end{bmatrix}$$ ![figure](../assets/c58094ba032e2df7.svg)
$$\rightarrow\quad \text{MatrixOrthogonal} = \left[\begin{array}{ccc}\!-0.5303 & 0.2613 & -0.4277\\-0.4419 & -0.2920 & -0.6383\\0.2652 & -0.8443 & -0.2059\\-0.2652 & -0.2432 & -0.6008\\-0.6187 & -0.2729 & 0.0799\end{array}\right] \\\ \text{MatrixTriangular} = \left[\begin{array}{ccc}-11.3137 & -1.5910 & -3.6239\\0 & -14.7129 & -5.1135\\0 & 0 & -7.9824\end{array}\right]$$ ![figure](../assets/5fe1e09ff80c2e56.svg)

*Example:*

*`decomposition_type`* = *"ql"*,
*`output_matrices_type`* = *"full"*
$$\mathrm{Matrix} = \begin{bmatrix}6.0 & -3.0 & 4.0\\ 5.0 & 5.0 & -2.0\\ -3.0 & 12.0 & 5.0\\ 3.0 & 4.0 & 7.0\\ 7.0 & 5.0 & 3.0\end{bmatrix}$$ ![figure](../assets/c58094ba032e2df7.svg)
$$\rightarrow\quad \mathrm{MatrixOrthogonal} = \begin{bmatrix}0.6806 & 0.0657 & 0.3659 & -0.4932 & -0.3941\\ 0.1161 & 0.5464 & 0.6091 & 0.5274 & 0.1971\\ 0.4093 & -0.0832 & -0.4046 & 0.6474 & -0.4927\\ -0.5362 & 0.4713 & 0.0072 & -0.1208 & -0.6897\\ -0.2611 & -0.6842 & 0.5757 & 0.2119 & -0.2956\end{bmatrix}\;\\[6pt]\mathrm{MatrixTriangular} = \begin{bmatrix}0 & 0 & 0\\ 0 & 0 & 0\\ 10.5059 & 0 & 0\\ -1.1429 & 12.4620 & 0\\ -4.0399 & -7.9812 & -10.1489\end{bmatrix}$$ ![figure](../assets/92d24d4f88327f64.svg)

*Example:*

*`decomposition_type`* = *"ql"*,
*`output_matrices_type`* = *"reduced"*
$$\mathrm{Matrix} = \begin{bmatrix}6.0 & -3.0 & 4.0\\ 5.0 & 5.0 & -2.0\\ -3.0 & 12.0 & 5.0\\ 3.0 & 4.0 & 7.0\\ 7.0 & 5.0 & 3.0\end{bmatrix}$$ ![figure](../assets/c58094ba032e2df7.svg)
$$\rightarrow MatrixOrthogonal = \begin{bmatrix}0.3659 & -0.4932 & -0.3941 \\ 0.6091 & 0.5274 & 0.1971 \\ -0.4046 & 0.6474 & -0.4927 \\ 0.0072 & -0.1208 & -0.6897 \\ 0.5757 & 0.2119 & -0.2956\end{bmatrix} \\ MatrixTriangular = \begin{bmatrix}10.5059 & 0 & 0 \\ -1.1429 & 12.4610 & 0 \\ -4.0399 & -7.9812 & -10.1489\end{bmatrix}$$ ![figure](../assets/8a99dfe371a82c83.svg)

For *`decomposition_type`* = *"rq"* a RQ decomposition
(Right/Quadratic) or for *`decomposition_type`* = *"lq"*
a LQ decomposition (Left/Quadratic) is computed. The decomposition
is written as
$$\texttt{Matrix}=\texttt{MatrixTriangular}\cdot\texttt{MatrixOrthogonal}.$$

*Example:*

*`decomposition_type`* = *"rq"*,
*`output_matrices_type`* = *"full"*
$$\begin{bmatrix}6.0 & 5.0 & -3.0 & 3.0 & 7.0\\-3.0 & 5.0 & 12.0 & 4.0 & 5.0\\4.0 & -2.0 & 5.0 & 7.0 & 3.0\end{bmatrix}$$ ![figure](../assets/e0f40ce8a796b54d.svg)
$$\rightarrow\ \text{MatrixOrthogonal} = \begin{bmatrix}0.6806 & 0.1161 & 0.4093 & -0.5362 & -0.2611\\0.0657 & 0.5464 & -0.0832 & 0.4713 & -0.6842\\0.3659 & 0.6091 & -0.4046 & 0.0072 & 0.5757\\-0.4932 & 0.5274 & 0.6474 & -0.1208 & 0.2119\\-0.3941 & 0.1971 & -0.4927 & -0.6897 & -0.2956\end{bmatrix}\n\\ MatrixTriangular = \begin{bmatrix}0 & 0 & 10.5059 & -1.1429 & -4.0399\\0 & 0 & 0 & 12.4620 & -7.9812\\0 & 0 & 0 & 0 & -10.1489\\\end{bmatrix}$$ ![figure](../assets/5e31bae7f675c623.svg)

*Example:*

*`decomposition_type`* = *"rq"*,
*`output_matrices_type`* = *"reduced"*
$$\begin{bmatrix}6.0 & 5.0 & -3.0 & 3.0 & 7.0\\-3.0 & 5.0 & 12.0 & 4.0 & 5.0\\4.0 & -2.0 & 5.0 & 7.0 & 3.0\end{bmatrix}$$ ![figure](../assets/e0f40ce8a796b54d.svg)
$$\rightarrow\ MatrixOrthogonal = \begin{bmatrix} 0.3659 & 0.6091 & -0.4046 & 0.0072 & 0.5757 \\ -0.4932 & 0.5274 & 0.6474 & -0.1208 & 0.2119 \\ -0.3941 & 0.1971 & -0.4927 & -0.6897 & -0.2956 \end{bmatrix}\\[6pt] MatrixTriangular = \begin{bmatrix} 10.5059 & -1.1429 & -4.0399 \\ 0 & 12.4620 & -7.9812 \\ 0 & 0 & -10.1489 \end{bmatrix}$$ ![figure](../assets/7e7d77e86cb8df92.svg)

*Example:*

*`decomposition_type`* = *"lq"*,
*`output_matrices_type`* = *"full"*
$$\begin{bmatrix}6.0 & 5.0 & -3.0 & 3.0 & 7.0\\-3.0 & 5.0 & 12.0 & 4.0 & 5.0\\4.0 & -2.0 & 5.0 & 7.0 & 3.0\end{bmatrix}$$ ![figure](../assets/e0f40ce8a796b54d.svg)
$$\rightarrow MatrixOrthogonal = \begin{bmatrix}-0.5303 & -0.4419 & 0.2652 & -0.2652 & -0.6187 \\ 0.2613 & -0.2920 & -0.8443 & -0.2432 & -0.2729 \\ -0.4277 & 0.6383 & -0.2059 & -0.6008 & 0.0799 \\ -0.5566 & 0.1727 & -0.3961 & 0.7000 & -0.1160 \\ -0.3972 & -0.5312 & -0.1326 & -0.1400 & 0.7231\] \\ \\ MatrixTriangular = \begin{bmatrix}-11.3137 & 0 & 0 & 0 & 0 \\ -1.5910 & -14.7129 & 0 & 0 & 0 \\ -3.6239 & -5.1135 & -7.9824 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0\]$$ ![figure](../assets/3250118f3e93e7ec.svg)

*Example:*

*`decomposition_type`* = *"lq"*,
*`output_matrices_type`* = *"reduced"*
$$\begin{bmatrix}6.0 & 5.0 & -3.0 & 3.0 & 7.0\\-3.0 & 5.0 & 12.0 & 4.0 & 5.0\\4.0 & -2.0 & 5.0 & 7.0 & 3.0\end{bmatrix}$$ ![figure](../assets/e0f40ce8a796b54d.svg)
$$\rightarrow\quad \text{MatrixOrthogonal} = \begin{bmatrix}-0.5303 & -0.4419 & 0.2652 & -0.2652 & -0.6187\\ 0.2613 & -0.2920 & -0.8443 & -0.2432 & -0.2729\\ -0.4277 & 0.6383 & -0.2059 & -0.6008 & 0.0799\end{bmatrix} \\ \text{MatrixTriangular} = \begin{bmatrix}-11.3137 & 0 & 0\\ -1.5910 & -14.7129 & 0\\ -3.6239 & -5.1135 & -7.9824\end{bmatrix}$$ ![figure](../assets/079a6f866747e128.svg)

It should be noted that in the examples there are differences in the
meaning of the numbers of the output matrices: The results of the
elements are per definition a certain value if the number of this
value is shown as an integer number, e.g., 0 or 1. If the number is
shown as a floating point number, e.g., 0.0 or 1.0, the value is
computed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`decomposition_type`** (input_control)  string `→` str

Method of decomposition.

Default:
"qr"

List of values:
"lq", "ql", "qr", "rq"

**`output_matrices_type`** (input_control)  string `→` str

Type of output matrices.

Default:
"full"

List of values:
"full", "reduced"

**`compute_orthogonal`** (input_control)  string `→` str

Computation of the orthogonal matrix.

Default:
"true"

List of values:
"false", "true"

**`matrix_orthogonal_id`** (output_control)  matrix `→` HHandle

Matrix handle with the orthogonal part of the
decomposed input matrix.

**`matrix_triangular_id`** (output_control)  matrix `→` HHandle

Matrix handle with the triangular part of the
decomposed input matrix.

## Result

If the parameters are valid, the operator
`orthogonal_decompose_matrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`decompose_matrix`,
`solve_matrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
