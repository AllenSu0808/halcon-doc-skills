# compose_funct_1d (Operator)

## Name

`compose_funct_1d` — Compose two functions.

## Signature

`def compose_funct_1d(function_1: Sequence[Union[float, int]], function_2: Sequence[Union[float, int]], border: str) -> Sequence[Union[float, int]]`

## Description

`compose_funct_1d` composes two functions, i.e., calculates
ComposedFunction(x) = Function2(Function1(x)).
*`composed_function`* has the same domain (x-range) as
*`function_1`*. If the range (y value range) of
*`function_1`* is larger than the domain of *`function_2`*,
the parameter *`border`* determines the border treatment of
*`function_2`*. For *`border`*=*"zero"* values
outside the domain of *`function_2`* are set to 0, for
*`border`*=*"constant"* they are set to the
corresponding value at the border, for
*`border`*=*"mirror"* they are mirrored at the border,
and for *`border`*=*"cyclic"* they are continued
cyclically. To obtain y values, *`function_2`* is interpolated
linearly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function_1`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function 1.

**`function_2`** (input_control)  function_1d `→` Sequence[Union[float, int]]

Input function 2.

**`border`** (input_control)  string `→` str

Border treatment for the input functions.

Default:
"constant"

List of values:
"constant", "cyclic", "mirror", "zero"

**`composed_function`** (output_control)  function_1d `→` Sequence[Union[float, int]]

Composed function.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Module

Foundation
