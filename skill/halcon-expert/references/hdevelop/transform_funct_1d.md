# transform_funct_1d (Operator)

## Name

`transform_funct_1d` — Transform a function using given transformation parameters.

## Signature

`transform_funct_1d( : : Function, Params : TransformedFunction)`

## Description

`transform_funct_1d` transforms the input function
*`Function`* using the transformation parameters given in
*`Params`*. The function *`Function`* is passed as a
tuple (see [`create_funct_1d_array`](create_funct_1d_array.md) and
[`create_funct_1d_pairs`](create_funct_1d_pairs.md)). The following model is used for the
transformation between the two functions (see
[`match_funct_1d_trans`](match_funct_1d_trans.md)):
$$y_{t}(x)=a_{1}y(a_{3}x+a_{4})+a_{2}.$$
The output function *`TransformedFunction`* is obtained by
transforming the x and y values of the input function separately
with the above formula, i.e., the output function is not sampled
again. Therefore, the parameter $a_{3}$ is restricted to
$a_{3} \neq 0.0$ ![figure](../assets/5f65e0d95e7e3cf0.svg). To resample a function, the operator
[`sample_funct_1d`](sample_funct_1d.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Input function.

**`Params`** (input_control)  number-array `→`  (real)

Transformation parameters between the functions.

Number of elements:
4

**`TransformedFunction`** (output_control)  function_1d `→`  (real / integer)

Transformed function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`,
`match_funct_1d_trans`

## Module

Foundation
