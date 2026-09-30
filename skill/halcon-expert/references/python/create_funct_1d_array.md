# create_funct_1d_array (Operator)

## Name

`create_funct_1d_array` — Create a function from a sequence of y values.

## Signature

`def create_funct_1d_array(yvalues: MaybeSequence[Union[float, int]]) -> Sequence[Union[float, int]]`

## Description

`create_funct_1d_array` creates a one-dimensional function
from a set of y values *`yvalues`*. The resulting function
can then be processed and analyzed with the operators for 1d
functions. *`yvalues`* is interpreted as follows: the first
value of *`yvalues`* is the function value at zero, the
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
are the y values passed in *`yvalues`* with $i\in[1,n]$ .

Alternatively, the operator [`create_funct_1d_pairs`](create_funct_1d_pairs.md) can be
used to create a function. [`create_funct_1d_pairs`](create_funct_1d_pairs.md) also allows
to define a function with non-equidistant x values by specifying them
explicitly. Thus to get the same definition as with
`create_funct_1d_array`, one would pass a tuple of
x values to [`create_funct_1d_pairs`](create_funct_1d_pairs.md) that has the same length
as *`yvalues`* and contains values starting at 0 and increasing by
1 in each position. Note, however, that [`create_funct_1d_pairs`](create_funct_1d_pairs.md)
leads to a different internal representation of the function which
needs more storage (because all (x,y) pairs are stored) and sometimes
cannot be processed as efficiently as functions created by
`create_funct_1d_array`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`yvalues`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

X value for function points.

**`function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Created function.

## Possible Successors

`write_funct_1d`,
`y_range_funct_1d`,
`get_pair_funct_1d`,
`transform_funct_1d`

## Alternatives

`create_funct_1d_pairs`,
`read_funct_1d`

## See also

`funct_1d_to_pairs`

## Module

Foundation
