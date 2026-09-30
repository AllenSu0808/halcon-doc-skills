# match_funct_1d_trans (Operator)

## Name

`match_funct_1d_trans` — Calculate transformation parameters between two functions.

## Signature

`def match_funct_1d_trans(function_1: Sequence[Union[float, int]], function_2: Sequence[Union[float, int]], border: str, params_const: Sequence[float], use_params: Sequence[str]) -> Tuple[Sequence[float], float, Sequence[float]]`

## Description

`match_funct_1d_trans` calculates the transformation parameters
between two functions given as the tuples *`function_1`* and
*`function_2`* (see [`create_funct_1d_array`](create_funct_1d_array.md) and
[`create_funct_1d_pairs`](create_funct_1d_pairs.md)). The following model is used for the
transformation between the two functions:
$$y_{1}(x)=a_{1}y_{2}(a_{3}x+a_{4})+a_{2}.$$
The transformation parameters are determined by a least-squares
minimization of the following function:
$$\sum_{i=0}^{n-1} (y_1(x_i) - a_1 y_2(a_3 x_i + a_4) + a_2)^2$$ ![figure](../assets/beae19d936c6d86e.svg)
The values of the function $y_{2}$ are obtained by
linear interpolation. The parameter *`border`* determines
the values of the function *`function_2`* outside of its domain.
For *`border`*=*"zero"* these values are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
and for *`border`*=*"cyclic"* they are continued
cyclically. The calculated transformation parameters are returned
as a 4-tuple $[a_{1},a_{2},a_{3},a_{4}]$ in
*`params`*. If some of the parameter values are
known, the respective parameters can be excluded from the
least-squares adjustment by setting the corresponding value in the
tuple *`use_params`* to the value *"false"*. In this
case, the tuple *`params_const`* must contain the known value of
the respective parameter. If a parameter is used for the adjustment
(*`use_params`* = *"true"*), the corresponding parameter
in *`params_const`* is ignored. On output,
`match_funct_1d_trans` additionally returns the sum of the
squared errors *`chi_square`* of the resulting function, i.e.,
the function obtained by transforming the input function with the
transformation parameters, as well as the covariance matrix
*`covar`* of the transformation parameters *`params`*.
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

**`function_1`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Function 1.

**`function_2`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Function 2.

**`border`** (input_control)  string `→` str

Border treatment for function 2.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`params_const`** (input_control)  number-array `→` Sequence[float]

Values of the parameters to remain constant.

Number of elements:
4

Default:
[1.0,0.0,1.0,0.0]

**`use_params`** (input_control)  string-array `→` Sequence[str]

Should a parameter be adapted for it?

Number of elements:
4

Default:
["true","true","true","true"]

List of values:
"false", "true"

**`params`** (output_control)  number-array `→` Sequence[float]

Transformation parameters between the functions.

Number of elements:
4

**`chi_square`** (output_control)  number `→` float

Quadratic error of the output function.

**`covar`** (output_control)  number-array `→` Sequence[float]

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
