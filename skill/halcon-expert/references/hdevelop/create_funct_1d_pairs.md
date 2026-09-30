# create_funct_1d_pairs (Operator)

## Name

`create_funct_1d_pairs` — Create a function from a set of (x,y) pairs.

## Signature

`create_funct_1d_pairs( : : XValues, YValues : Function)`

## Description

`create_funct_1d_pairs` creates a one-dimensional function
from a set of pairs of (x,y) values. The *`XValues`* of the
functions have to be passed in ascending order. The resulting
function can then be processed and analyzed with the operators for
1d functions.

The created function is composed like this:

$$\texttt{Function}=[1,x_{1},y_{1},x_{2},y_{2},...,x_{n},y_{n}]$$

where

$\texttt{Function}[1]=1$
denotes the function type as a one-dimensional function from a set of
pairs and

$[x_{i},y_{i}]$
are pairs of (x,y) values passed in *`XValues`* and *`YValues`*
with $i\in[1,n]$ .

Alternatively, functions can be created with the operator
[`create_funct_1d_array`](create_funct_1d_array.md). In contrast to this operator,
x values with arbitrary positions can be specified with
`create_funct_1d_pairs`. Hence, it is the more general
operator. It should be noted, however, that because of this
generality the processing of a function created with
`create_funct_1d_pairs` cannot be carried out as efficiently
as for equidistant functions. In particular, not all operators
accept such functions. If necessary, a function can be transformed
into an equidistant function with the operator
[`sample_funct_1d`](sample_funct_1d.md).

## Attention

`create_funct_1d_pairs` examines whether the x values of type
'double' are ascending. Some other operators apply the same check but use
the type 'float' instead of 'double'. If such an operator is called as
successor, it might happen that two consecutive x values seem to be
equal for the 'float' variant, although they were ascending in the
'double' variant. If this happens, an error is thrown.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`XValues`** (input_control)  number(-array) `→`  (real / integer)

X value for function points.

**`YValues`** (input_control)  number(-array) `→`  (real / integer)

Y value for function points.

**`Function`** (output_control)  function_1d `→`  (real / integer)

Created function.

## Possible Successors

`write_funct_1d`,
`y_range_funct_1d`,
`get_pair_funct_1d`

## Alternatives

`create_funct_1d_array`,
`read_funct_1d`

## See also

`funct_1d_to_pairs`

## Module

Foundation
