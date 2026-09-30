# match_funct_1d_trans (Operator)

## Name

`match_funct_1d_trans` — Calculate transformation parameters between two functions.

## Signature

`match_funct_1d_trans( : : Function1, Function2, Border, ParamsConst, UseParams : Params, ChiSquare, Covar)`

## Description

`match_funct_1d_trans` calculates the transformation parameters
between two functions given as the tuples *`Function1`* and
*`Function2`* (see [`create_funct_1d_array`](create_funct_1d_array.md) and
[`create_funct_1d_pairs`](create_funct_1d_pairs.md)). The following model is used for the
transformation between the two functions:
$$y_{1}(x)=a_{1}y_{2}(a_{3}x+a_{4})+a_{2}.$$
The transformation parameters are determined by a least-squares
minimization of the following function:
$$\sum_{i=0}^{n-1} (y_1(x_i) - a_1 y_2(a_3 x_i + a_4) + a_2)^2$$ ![figure](../assets/beae19d936c6d86e.svg)
The values of the function $y_{2}$ are obtained by
linear interpolation. The parameter *`Border`* determines
the values of the function *`Function2`* outside of its domain.
For *`Border`*=*'zero'* these values are set to 0, for
*`Border`*=*'constant'* they are set to the
corresponding value at the border, for
*`Border`*=*'mirror'* they are mirrored at the border,
and for *`Border`*=*'cyclic'* they are continued
cyclically. The calculated transformation parameters are returned
as a 4-tuple $[a_{1},a_{2},a_{3},a_{4}]$ in
*`Params`*. If some of the parameter values are
known, the respective parameters can be excluded from the
least-squares adjustment by setting the corresponding value in the
tuple *`UseParams`* to the value *'false'*. In this
case, the tuple *`ParamsConst`* must contain the known value of
the respective parameter. If a parameter is used for the adjustment
(*`UseParams`* = *'true'*), the corresponding parameter
in *`ParamsConst`* is ignored. On output,
`match_funct_1d_trans` additionally returns the sum of the
squared errors *`ChiSquare`* of the resulting function, i.e.,
the function obtained by transforming the input function with the
transformation parameters, as well as the covariance matrix
*`Covar`* of the transformation parameters *`Params`*.
These parameters can be used to decide whether a successful matching
of the functions was possible.

Note that in case that there is no unique solution for the
transformation parameters, `match_funct_1d_trans` either
returns one selected single solution or returns the error 9205
(Matrix is singular).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function1`** (input_control)  function_1d `→`  (real / integer)

Function 1.

**`Function2`** (input_control)  function_1d `→`  (real / integer)

Function 2.

**`Border`** (input_control)  string `→`  (string)

Border treatment for function 2.

Default:
'constant'

List of values:
'constant', 'cyclic', 'mirror', 'zero'

**`ParamsConst`** (input_control)  number-array `→`  (real)

Values of the parameters to remain constant.

Number of elements:
4

Default:
[1.0,0.0,1.0,0.0]

**`UseParams`** (input_control)  string-array `→`  (string)

Should a parameter be adapted for it?

Number of elements:
4

Default:
['true','true','true','true']

List of values:
'false', 'true'

**`Params`** (output_control)  number-array `→`  (real)

Transformation parameters between the functions.

Number of elements:
4

**`ChiSquare`** (output_control)  number `→`  (real)

Quadratic error of the output function.

**`Covar`** (output_control)  number-array `→`  (real)

Covariance Matrix of the transformation parameters.

Number of elements:
16

## Possible Predecessors

`create_funct_1d_array`,
`create_funct_1d_pairs`

## See also

`gray_projections`

## Module

Foundation
