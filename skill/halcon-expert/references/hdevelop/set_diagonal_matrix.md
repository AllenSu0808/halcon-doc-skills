# set_diagonal_matrix (Operator)

## Name

`set_diagonal_matrix` — Set the diagonal elements of a matrix.

## Signature

`set_diagonal_matrix( : : MatrixID, VectorID, Diagonal : )`

## Description

The operator `set_diagonal_matrix` *overwrites*
the diagonal elements of the `Matrix` with
the elements of the matrix `Vector`. The matrices are
defined by their matrix handles *`MatrixID`* and
*`VectorID`*. The matrix `Vector` must have one column
and one row, n columns and one row or one column and n rows. n
is the number of elements to be set in the `Matrix` (see
below). If the matrix `Vector` has one column and one row,
i.e., the matrix has one value, each element of the diagonal of the
`Matrix` is overwritten by this value. Otherwise, the
diagonal is overwritten by the elements of the matrix
`Vector`.

If *`Diagonal`* = 0, the main diagonal of the `Matrix`
is overwritten. The number n = min(number of rows of
`Matrix`, number of columns of `Matrix`).

*Example 1:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = \left[ 3.0 \quad 7.0 \quad 1.0 \right] \\ Diagonal = 0$$ ![figure](../assets/389f0c90b80068dd.svg)
$$\rightarrow\quad \mathrm{Matrix} = \left[\begin{array}{cccc}\!3.0\! & 0.0 & 0.0 & 0.0\\0.0 & 7.0 & 0.0 & 0.0\\0.0 & 0.0 & 1.0 & 0.0\\\end{array}\right]$$ ![figure](../assets/81aa9e65dacf26cc.svg)

*Example 2:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = [3.0] \\quad Diagonal = 0$$ ![figure](../assets/e47a207d2a93cc68.svg)
$$\rightarrow\quad \text{Matrix} = \left[\begin{array}{rrrr}\!3.0 & 0.0 & 0.0 & 0.0\\ 0.0 & 3.0 & 0.0 & 0.0\\ 0.0 & 0.0 & 3.0 & 0.0\\ 0.0 & 0.0 & 0.0 & 3.0\!\end{array}\right]$$ ![figure](../assets/a12a7df6f326fbbf.svg)

If *`Diagonal`* is positive, the *`Diagonal`*-th
super-diagonal of `Matrix` is overwritten. For the example
1 the number n = min(number of rows of `Matrix`, parameter
*`Diagonal`*). For the example 2 the number n = min(number
of rows of `Matrix`, number of columns of `Matrix`).

*Example 1:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = [ -2.0 6.0 ] \\text{Diagonal} = 2$$ ![figure](../assets/5e3ff27ac04cfa4b.svg)
$$\rightarrow \text{ Matrix } = \left[\begin{array}{cccc}0.0 & 0.0 & -2.0 & 0.0\\0.0 & 0.0 & 0.0 & 6.0\\0.0 & 0.0 & 0.0 & 0.0\end{array}\right]$$ ![figure](../assets/cfbbf4789cc44d7e.svg)

*Example 2:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = [ -2.0 ] \\ Diagonal = 2$$ ![figure](../assets/76eebeee34d1cf21.svg)
$$\rightarrow\ Matrix = \begin{bmatrix}0.0 & 0.0 & -2.0 & 0.0\\0.0 & 0.0 & 0.0 & -2.0\\0.0 & 0.0 & 0.0 & 0.0\\end{bmatrix}$$ ![figure](../assets/a966c03bbfe1f4ee.svg)

If *`Diagonal`* is negative, the *`Diagonal`*-th
sub-diagonal of `Matrix` is overwritten. For the example 1
the number n = min(number of columns of `Matrix`,
parameter *`Diagonal`*). For the example 2 the number n =
min(number of rows of `Matrix`, number of columns of
`Matrix`).

*Example 1:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = [ -5.0 -4.0 ]\nDiagonal = -1$$ ![figure](../assets/255ec42ce6634cb2.svg)
$$\rightarrow\quad \text{Matrix} = \begin{bmatrix}0.0 & 0.0 & 0.0 & 0.0\\-5.0 & 0.0 & 0.0 & 0.0\\0.0 & -4.0 & 0.0 & 0.0\end{bmatrix}$$ ![figure](../assets/8d160f76dde37b55.svg)

*Example 2:*
$$\mathrm{Matrix} = \left[\begin{array}{cccc}0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\[3pt]0.0 & 0.0 & 0.0 & 0.0\\end{array}\right]$$ ![figure](../assets/7cd8c5838d7d7059.svg)
$$Vector = [ -5.0 ] Diagonal = -1$$ ![figure](../assets/9319444d2558e2af.svg)
$$\rightarrow\quad \text{Matrix} = \begin{bmatrix}0.0 & 0.0 & 0.0 & 0.0\\-5.0 & 0.0 & 0.0 & 0.0\\0.0 & -5.0 & 0.0 & 0.0\end{bmatrix}$$ ![figure](../assets/1c8e146d1599f100.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MatrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MatrixID`** (input_control, state is modified)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`VectorID`** (input_control)  matrix `→`  (handle)

Matrix handle containing the diagonal elements to
be set.

**`Diagonal`** (input_control)  integer `→`  (integer)

Position of the diagonal.

Default:
0

Suggested values:
-20, -10, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 20

## Result

If the parameters are valid, the operator
`set_diagonal_matrix` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## See also

`get_diagonal_matrix`

## Module

Foundation
