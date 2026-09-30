# Funct1dToPairs (Operator)

## Name

`Funct1dToPairs` — Access to the x/y values of a function.

## Signature

`static void HOperatorSet.Funct1dToPairs(HTuple function, out HTuple XValues, out HTuple YValues)`

`void HFunction1D.Funct1dToPairs(out HTuple XValues, out HTuple YValues)`

## Description

`Funct1dToPairs` splits the input function *`function`*
into tuples for the x and y values.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`function`** (input_control)  function_1d `→` [HFunction1D](HFunction1D.md), [HTuple](HTuple.md) (*double* / int / long)

Input function.

**`XValues`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

X values of the function.

**`YValues`** (output_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Y values of the function.

## Possible Predecessors

`CreateFunct1dPairs`,
`CreateFunct1dArray`

## Module

Foundation
