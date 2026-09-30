# SetFullMatrix (Operator)

## Name

`SetFullMatrix` — Set all values of a matrix.

## Signature

`static void HOperatorSet.SetFullMatrix(HTuple matrixID, HTuple values)`

`void HMatrix.SetFullMatrix(HTuple values)`

`void HMatrix.SetFullMatrix(double values)`

## Description

The operator `SetFullMatrix` *sets* all
elements of the input `Matrix` defined by the matrix handle
*`matrixID`*. The values of the parameter *`values`* can
be a tuple of floating point or integer numbers. Integer numbers
are converted to floating point numbers automatically. The
parameter *`values`* must contain all values in a row-major
order, i.e., stored line by line. In addition, the number of
elements in *`values`* must be 1 or identical to the number of
all elements of the matrix.

Note: The same result can be reached with the operator
[`CreateMatrix`](create_matrix.md). The advantage by using the operator
`SetFullMatrix` is to recycle a matrix that is no longer
needed. Thus, the runtime of the operation takes fewer time.

*Example 1:*

$$\text{Matrix} = \left[\begin{array}{ccc}0.0 & 0.0 & 0.0\\0.0 & 0.0 & 0.0\\0.0 & 0.0 & 0.0\end{array}\right] \\text{Values} = [3,1,-2,-5,7,2,-9,-4,1]$$ ![figure](../assets/2b253fdef8465fd6.svg)
$$\rightarrow\quad \text{Matrix} = \left[\begin{array}{ccc}3.0 & 1.0 & -2.0\\ -5.0 & 7.0 & 2.0\\ -9.0 & -4.0 & 1.0\end{array}\right]$$ ![figure](../assets/a9a21a1fd6c33de4.svg)

*Example 2:*

$$\text{Matrix} = \begin{bmatrix} 0.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.0 \\ 0.0 & 0.0 & 0.0 \end{bmatrix} \\ \text{Values} = [7]$$ ![figure](../assets/910909dee8aeda99.svg)
$$\rightarrow\ Matrix = \begin{bmatrix} 7.0 & 7.0 & 7.0 \\ 7.0 & 7.0 & 7.0 \\ 7.0 & 7.0 & 7.0 \end{bmatrix}$$ ![figure](../assets/ee1c3341ae346822.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixID`** (input_control, state is modified)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`values`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Values to be set.

## Result

If the parameters are valid, the operator `SetFullMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`ClearMatrix`

## See also

`GetFullMatrix`

## Module

Foundation
