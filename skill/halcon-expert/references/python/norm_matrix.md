# norm_matrix (Operator)

## Name

`norm_matrix` — Norm of a matrix.

## Signature

`def norm_matrix(matrix_id: HHandle, norm_type: str) -> float`

## Description

The operator `norm_matrix` computes the norm of the elements
of the `Matrix` defined by the matrix handle
*`matrix_id`*. The return value is a floating point number.

The type of norming of the matrix can be selected via the parameter
*`norm_type`*:

- ***"frobenius-norm"*:** —

  The Frobenius norm
  is computed. The formula for the calculation of the result is:
  $$\sqrt{\sum_{i=0}^{m-1}\sum_{j=0}^{n-1} Matrix_{ij}^{2}}$$ ![figure](../assets/4e8e1f156045db6b.svg)
  with m = number of rows and n = number of columns of the
  `Matrix`.

  *Example:*

  $$\text{Matrix} = \begin{bmatrix}3.0 & 1.0\\4.0 & -3.0\\-7.0 & 4.0\end{bmatrix} \rightarrow \text{Value} = 10.0$$ ![figure](../assets/fb55a9017d126ee1.svg)
- ***"infinity-norm"*:** —

  The infinity norm is
  computed. The result is the largest value of the sum of the
  absolute values of the elements of the rows. The formula for the
  calculation is:
  $$Value = \max_{i=0, m-1}^{n-1} \sum_{j=0}^{n-1} |\text{Matrix}_{ij}|$$ ![figure](../assets/acc6bb8a19b21cda.svg)
  with m = number of rows and n = number of columns of the
  `Matrix`.

  *Example:*

  $$\text{Matrix} = \begin{bmatrix}3.0 & 1.0\\ 4.0 & -3.0\\ -7.0 & 4.0\end{bmatrix} \rightarrow \text{Value} = 11.0$$ ![figure](../assets/94a3097c7f0ab120.svg)
- ***"1-norm"*:** —

  The 1-norm is computed. The
  result is the largest value of the sum of the absolute values of
  the elements of the columns. The formula for the calculation is:
  $$Value = \max_{j=0,n-1} \sum_{i=0}^{n-1} |\text{Matrix}_{x_{ij}}|$$ ![figure](../assets/5b61e12e635cd1db.svg)
  with m = number of rows and n = number of columns of the
  `Matrix`.

  *Example:*

  $$\text{Matrix} = \begin{bmatrix}3.0 & 1.0\\4.0 & -3.0\\-7.0 & 4.0\end{bmatrix} \rightarrow \text{Value} = 14.0$$ ![figure](../assets/d20dc910ed65e747.svg)
- ***"2-norm"*:** —

  The 2-norm is computed. The
  result is the largest singular value of the `Matrix`. The
  formula for the calculation of the result is:
  $$\texttt{Value}=\max (\mathrm{singularvalues}(\texttt{Matrix}))$$

  *Example:*

  $$\mathrm{Matrix} = \begin{bmatrix}3.0 & 1.0\\ 4.0 & -3.0\\ -7.0 & 4.0\end{bmatrix} \rightarrow \mathrm{Value} = 9.7006$$ ![figure](../assets/0134867defb047f9.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`norm_type`** (input_control)  string `→` str

Type of norm.

Default:
"2-norm"

List of values:
"1-norm", "2-norm", "frobenius-norm", "infinity-norm"

**`value`** (output_control)  real `→` float

Norm of the input matrix.

## Result

If the parameters are valid, the operator `norm_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## See also

`sum_matrix`,
`mean_matrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
