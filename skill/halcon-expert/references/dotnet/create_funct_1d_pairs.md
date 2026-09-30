# CreateFunct1dPairs (Operator)

## Name

`CreateFunct1dPairs` — Create a function from a set of (x,y) pairs.

## Signature

`static void HOperatorSet.CreateFunct1dPairs(HTuple XValues, HTuple YValues, out HTuple function)`

`public HFunction1D(HTuple XValues, HTuple YValues)`

`public HFunction1D(double XValues, double YValues)`

`void HFunction1D.CreateFunct1dPairs(HTuple XValues, HTuple YValues)`

`void HFunction1D.CreateFunct1dPairs(double XValues, double YValues)`

## Description

`CreateFunct1dPairs` creates a one-dimensional function
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
[`CreateFunct1dArray`](create_funct_1d_array.md). In contrast to this operator,
x values with arbitrary positions can be specified with
`CreateFunct1dPairs`. Hence, it is the more general
operator. It should be noted, however, that because of this
generality the processing of a function created with
`CreateFunct1dPairs` cannot be carried out as efficiently
as for equidistant functions. In particular, not all operators
accept such functions. If necessary, a function can be transformed
into an equidistant function with the operator
[`SampleFunct1d`](sample_funct_1d.md).

## Attention

`CreateFunct1dPairs` examines whether the x values of type
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

**`XValues`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X value for function points.

**`YValues`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Y value for function points.

**`function`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Created function.

## Possible Successors

`WriteFunct1d`,
`YRangeFunct1d`,
`GetPairFunct1d`

## Alternatives

`CreateFunct1dArray`,
`ReadFunct1d`

## See also

`Funct1dToPairs`

## Module

Foundation
