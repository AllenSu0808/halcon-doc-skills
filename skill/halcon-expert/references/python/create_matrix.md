# create_matrix (Operator)

## Name

`create_matrix` — Create a matrix.

## Signature

`def create_matrix(rows: int, columns: int, value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_matrix` creates a new `Matrix`
with *`rows`* rows and *`columns`* columns and returns the
matrix handle *`matrix_id`*. Access to the elements of the
matrix is possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md).
The parameter *`value`* is a string or a tuple of floating
point or integer numbers. Integer numbers are converted to
floating point numbers automatically.

If *`value`* = *"identity"*, *`rows`* and
*`columns`* must have the identical values and an identity matrix
is created.

*Example:*

*`rows`* = *3*,
*`columns`* = *3*,
*`value`* = *"identity"*
$$\rightarrow\ \text{Matrix}=\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}$$ ![figure](../assets/5bef0d2b3f1dc31a.svg)

If the parameter *`value`* contains a single value, all
elements of the matrix are filled with this value.

*Example:*

*`rows`* = *3*,
*`columns`* = *3*,
*`value`* = *7*
$$\rightarrow\quad \mathrm{Matrix} = \left[\begin{array}{ccc}7.0 & 7.0 & 7.0\\7.0 & 7.0 & 7.0\\7.0 & 7.0 & 7.0\end{array}\right]$$ ![figure](../assets/66604e45ffa64f42.svg)

If *`value`* contains as many values as the main diagonal, all
elements of the main diagonal are set to the values of the parameter
*`value`* (i.e., the number of elements in *`value`* is
identical).

*Example:*

*`rows`* = *3*,
*`columns`* = *4*,
*`value`* = *[3,7,1]*
$$\rightarrow\quad \text{Matrix} = \begin{bmatrix}3.0 & 0 & 0 & 0\\0 & 7.0 & 0 & 0\\0 & 0 & 1.0 & 0\end{bmatrix}$$ ![figure](../assets/868e2ae69fd38b83.svg)

It is also possible to set all elements of the matrix with different
values. In this case the parameter *`value`* must contain all
values in a row-major order, i.e., stored line by line. In
addition, the number of elements of *`value`* must be identical
to the number of all elements of the matrix, i.e., *`rows`*
$\times$ *`columns`*.

*Example:*

*`rows`* = *3*,
*`columns`* = *3*,
*`value`* = *[3,1,-2,-5,7,2,-9,-4,1]*
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

**`rows`** (input_control)  integer `→` int

Number of rows of the matrix.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Rows >= 1`

**`columns`** (input_control)  integer `→` int

Number of columns of the matrix.

Default:
3

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 30, 50, 100

Restriction:
`Columns >= 1`

**`value`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float, str]]

Values for initializing the elements of the
matrix.

Default:
0

Suggested values:
0, 1, "identity"

**`matrix_id`** (output_control)  matrix `→` HHandle

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
