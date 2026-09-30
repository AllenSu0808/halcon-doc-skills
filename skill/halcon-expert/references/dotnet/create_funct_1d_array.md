# CreateFunct1dArray (Operator)

## Name

`CreateFunct1dArray` — Create a function from a sequence of y values.

## Signature

`static void HOperatorSet.CreateFunct1dArray(HTuple YValues, out HTuple function)`

`public HFunction1D(HTuple YValues)`

`public HFunction1D(double YValues)`

`void HFunction1D.CreateFunct1dArray(HTuple YValues)`

`void HFunction1D.CreateFunct1dArray(double YValues)`

## Description

`CreateFunct1dArray` creates a one-dimensional function
from a set of y values *`YValues`*. The resulting function
can then be processed and analyzed with the operators for 1d
functions. *`YValues`* is interpreted as follows: the first
value of *`YValues`* is the function value at zero, the
second value is the function value at one, etc. Thus, the values
define a function at equidistant x values (with distance
$\Delta x=1$), starting at
$x_{1}=0$.

The created function is composed like this:

$$\texttt{Function}=[0,\Delta x,x_{1},y_{1},y_{2},...,y_{n}]$$

where

$\texttt{Function}[0]=0,$
denotes the function type as an equidistant function,

$\Delta x$
is the equidistance of the x values,

$x_{1}$
is the starting x value (is always 0), and

$y_{i}$
are the y values passed in *`YValues`* with $i\in[1,n]$ .

Alternatively, the operator [`CreateFunct1dPairs`](create_funct_1d_pairs.md) can be
used to create a function. [`CreateFunct1dPairs`](create_funct_1d_pairs.md) also allows
to define a function with non-equidistant x values by specifying them
explicitly. Thus to get the same definition as with
`CreateFunct1dArray`, one would pass a tuple of
x values to [`CreateFunct1dPairs`](create_funct_1d_pairs.md) that has the same length
as *`YValues`* and contains values starting at 0 and increasing by
1 in each position. Note, however, that [`CreateFunct1dPairs`](create_funct_1d_pairs.md)
leads to a different internal representation of the function which
needs more storage (because all (x,y) pairs are stored) and sometimes
cannot be processed as efficiently as functions created by
`CreateFunct1dArray`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`YValues`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

X value for function points.

**`function`** (output_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Created function.

## Possible Successors

`WriteFunct1d`,
`YRangeFunct1d`,
`GetPairFunct1d`,
`TransformFunct1d`

## Alternatives

`CreateFunct1dPairs`,
`ReadFunct1d`

## See also

`Funct1dToPairs`

## Module

Foundation
