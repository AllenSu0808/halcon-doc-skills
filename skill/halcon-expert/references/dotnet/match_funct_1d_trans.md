# MatchFunct1dTrans (Operator)

## Name

`MatchFunct1dTrans` — Calculate transformation parameters between two functions.

## Signature

`static void HOperatorSet.MatchFunct1dTrans(HTuple function1, HTuple function2, HTuple border, HTuple paramsConst, HTuple useParams, out HTuple paramsVal, out HTuple chiSquare, out HTuple covar)`

`HTuple HFunction1D.MatchFunct1dTrans(HFunction1D function2, string border, HTuple paramsConst, HTuple useParams, out double chiSquare, out HTuple covar)`

## Description

`MatchFunct1dTrans` calculates the transformation parameters
between two functions given as the tuples *`function1`* and
*`function2`* (see [`CreateFunct1dArray`](create_funct_1d_array.md) and
[`CreateFunct1dPairs`](create_funct_1d_pairs.md)). The following model is used for the
transformation between the two functions:
$$y_{1}(x)=a_{1}y_{2}(a_{3}x+a_{4})+a_{2}.$$
The transformation parameters are determined by a least-squares
minimization of the following function:
$$\sum_{i=0}^{n-1} (y_1(x_i) - a_1 y_2(a_3 x_i + a_4) + a_2)^2$$ ![figure](../assets/beae19d936c6d86e.svg)
The values of the function $y_{2}$ are obtained by
linear interpolation. The parameter *`border`* determines
the values of the function *`function2`* outside of its domain.
For *`border`*=*"zero"* these values are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
and for *`border`*=*"cyclic"* they are continued
cyclically. The calculated transformation parameters are returned
as a 4-tuple $[a_{1},a_{2},a_{3},a_{4}]$ in
*`paramsVal`*. If some of the parameter values are
known, the respective parameters can be excluded from the
least-squares adjustment by setting the corresponding value in the
tuple *`useParams`* to the value *"false"*. In this
case, the tuple *`paramsConst`* must contain the known value of
the respective parameter. If a parameter is used for the adjustment
(*`useParams`* = *"true"*), the corresponding parameter
in *`paramsConst`* is ignored. On output,
`MatchFunct1dTrans` additionally returns the sum of the
squared errors *`chiSquare`* of the resulting function, i.e.,
the function obtained by transforming the input function with the
transformation parameters, as well as the covariance matrix
*`covar`* of the transformation parameters *`paramsVal`*.
These parameters can be used to decide whether a successful matching
of the functions was possible.

Note that in case that there is no unique solution for the
transformation parameters, `MatchFunct1dTrans` either
returns one selected single solution or returns the error 9205
(Matrix is singular).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function1`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function 1.

**`function2`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Function 2.

**`border`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Border treatment for function 2.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`paramsConst`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Values of the parameters to remain constant.

Number of elements:
4

Default:
[1.0,0.0,1.0,0.0]

**`useParams`** (input_control)  string-array `→` [HTuple](HTuple.md) (*string*)

Should a parameter be adapted for it?

Number of elements:
4

Default:
["true","true","true","true"]

List of values:
"false", "true"

**`paramsVal`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Transformation parameters between the functions.

Number of elements:
4

**`chiSquare`** (output_control)  number `→` [HTuple](HTuple.md) (*double*)

Quadratic error of the output function.

**`covar`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Covariance Matrix of the transformation parameters.

Number of elements:
16

## Possible Predecessors

`CreateFunct1dArray`,
`CreateFunct1dPairs`

## See also

`GrayProjections`

## Module

Foundation
