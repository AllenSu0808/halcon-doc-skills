# NormMatrix (Operator)

## Name

`NormMatrix` — Norm of a matrix.

## Signature

`static void HOperatorSet.NormMatrix(HTuple matrixID, HTuple normType, out HTuple value)`

`double HMatrix.NormMatrix(string normType)`

## Description

The operator `NormMatrix` computes the norm of the elements
of the `Matrix` defined by the matrix handle
*`matrixID`*. The return value is a floating point number.

The type of norming of the matrix can be selected via the parameter
*`normType`*:

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

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`normType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of norm.

Default:
"2-norm"

List of values:
"1-norm", "2-norm", "frobenius-norm", "infinity-norm"

**`value`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Norm of the input matrix.

## Result

If the parameters are valid, the operator `NormMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## See also

`SumMatrix`,
`MeanMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
