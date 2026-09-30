# compose_funct_1d (Operator)

## Name

`compose_funct_1d` — Compose two functions.

## Signature

`compose_funct_1d( : : Function1, Function2, Border : ComposedFunction)`

## Description

`compose_funct_1d` composes two functions, i.e., calculates
ComposedFunction(x) = Function2(Function1(x)).
*`ComposedFunction`* has the same domain (x-range) as
*`Function1`*. If the range (y value range) of
*`Function1`* is larger than the domain of *`Function2`*,
the parameter *`Border`* determines the border treatment of
*`Function2`*. For *`Border`*=*'zero'* values
outside the domain of *`Function2`* are set to 0, for
*`Border`*=*'constant'* they are set to the
corresponding value at the border, for
*`Border`*=*'mirror'* they are mirrored at the border,
and for *`Border`*=*'cyclic'* they are continued
cyclically. To obtain y values, *`Function2`* is interpolated
linearly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function1`** (input_control)  function_1d `→`  (real / integer)

Input function 1.

**`Function2`** (input_control)  function_1d `→`  (real / integer)

Input function 2.

**`Border`** (input_control)  string `→`  (string)

Border treatment for the input functions.

Default:
'constant'

List of values:
'constant', 'cyclic', 'mirror', 'zero'

**`ComposedFunction`** (output_control)  function_1d `→`  (real / integer)

Composed function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
