# TransformFunct1d (Operator)

## Name

`TransformFunct1d` — Transform a function using given transformation parameters.

## Signature

`static void HOperatorSet.TransformFunct1d(HTuple function, HTuple paramsVal, out HTuple transformedFunction)`

`HFunction1D HFunction1D.TransformFunct1d(HTuple paramsVal)`

## Description

`TransformFunct1d` transforms the input function
*`function`* using the transformation parameters given in
*`paramsVal`*. The function *`function`* is passed as a
tuple (see [`CreateFunct1dArray`](create_funct_1d_array.md) and
[`CreateFunct1dPairs`](create_funct_1d_pairs.md)). The following model is used for the
transformation between the two functions (see
[`MatchFunct1dTrans`](match_funct_1d_trans.md)):
$$y_{t}(x)=a_{1}y(a_{3}x+a_{4})+a_{2}.$$
The output function *`transformedFunction`* is obtained by
transforming the x and y values of the input function separately
with the above formula, i.e., the output function is not sampled
again. Therefore, the parameter $a_{3}$ is restricted to
$a_{3} \neq 0.0$ ![figure](../assets/5f65e0d95e7e3cf0.svg). To resample a function, the operator
[`SampleFunct1d`](sample_funct_1d.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`paramsVal`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double*)

Transformation parameters between the functions.

Number of elements:
4

**`transformedFunction`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Transformed function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`,
`MatchFunct1dTrans`

## Module

Foundation
