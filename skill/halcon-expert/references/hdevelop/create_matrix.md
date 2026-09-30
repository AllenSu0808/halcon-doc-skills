# create_matrix (Operator)

## Name

`create_matrix` — Create a matrix.

## Signature

`create_matrix( : : Rows, Columns, Value : MatrixID)`

## Description

The operator `create_matrix` creates a new `Matrix`
with *`Rows`* rows and *`Columns`* columns and returns the
matrix handle *`MatrixID`*. Access to the elements of the
matrix is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).
The parameter *`Value`* is a string or a tuple of floating
point or integer numbers. Integer numbers are converted to
floating point numbers automatically.

If *`Value`* = *'identity'*, *`Rows`* and
*`Columns`* must have the identical values and an identity matrix
is created.

*Example:*

*`Rows`* = *3*,
*`Columns`* = *3*,
*`Value`* = *'identity'*
$$\rightarrow\ \text{Matrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}$$ ![figure](../assets/5bef0d2b3f1dc31a.svg)

If the parameter *`Value`* contains a single value, all
elements of the matrix are filled with this value.

*Example:*

*`Rows`* = *3*,
*`Columns`* = *3*,
*`Value`* = *7*
$$\rightarrow\quad \mathrm{Matrix} = \left[\begin{array}{ccc}7.0 & 7.0 & 7.0\\7.0 & 7.0 & 7.0\\7.0 & 7.0 & 7.0\end{array}\right]$$ ![figure](../assets/66604e45ffa64f42.svg)

If *`Value`* contains as many values as the main diagonal, all
elements of the main diagonal are set to the values of the parameter
*`Value`* (i.e., the number of elements in *`Value`* is
identical).

*Example:*

*`Rows`* = *3*,
*`Columns`* = *4*,
*`Value`* = *[3,7,1]*
$$\rightarrow\quad \text{Matrix} = \begin{bmatrix}3.0 & 0 & 0 & 0\\0 & 7.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{bmatrix}$$ ![figure](../assets/868e2ae69fd38b83.svg)

It is also possible to set all elements of the matrix with different
values. In this case the parameter *`Value`* must contain all
values in a row-major order, i.e., stored line by line. In
addition, the number of elements of *`Value`* must be identical
to the number of all elements of the matrix, i.e., *`Rows`*
$\times$ *`Columns`*.

*Example:*

*`Rows`* = *3*,
*`Columns`* = *3*,
*`Value`* = *[3,1,-2,-5,7,2,-9,-4,1]*
$$\rightarrow\quad \text{Matrix} = \left[\begin{array}{ccc}3.0 & 1.0 & -2.0\\ -5.0 & 7.0 & 2.0\\ -9.0 & -4.0 & 1.0\end{array}\right]$$ ![figure](../assets/a9a21a1fd6c33de4.svg)

It should be noted that in the examples there are differences in the
meaning of the values of the output matrices: If a value is shown as
an integer number, e.g., 0 or 1, the value of this element is per
definition this certain value. If the number is shown as a floating
point number, e.g., 0.0 or 1.0, the value is computed by the
operator.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Rows`** (input_control)  integer `→`  (integer)

Number of rows of the matrix.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Rows >= 1`

**`Columns`** (input_control)  integer `→`  (integer)

Number of columns of the matrix.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Columns >= 1`

**`Value`** (input_control)  number(-array) `→`  (real / integer / string)

Values for initializing the elements of the
matrix.

Default:
0

Suggested values:
0, 1, 'identity'

**`MatrixID`** (output_control)  matrix `→`  (handle)

Matrix handle.

## Result

If the parameters are valid, the operator `create_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_full_matrix`,
`clear_matrix`

## Module

Foundation
