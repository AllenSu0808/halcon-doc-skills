# ClearClassMlp (Operator)

## Name

`ClearClassMlp` — Clear a multilayer perceptron.

## Signature

`static void HOperatorSet.ClearClassMlp(HTuple MLPHandle)`

`static void HClassMlp.ClearClassMlp(HClassMlp[] MLPHandle)`

`void HClassMlp.ClearClassMlp()`

## Description

`ClearClassMlp` clears the multilayer perceptron (MLP) given
by *`MLPHandle`* and frees all memory required for the MLP.
After calling `ClearClassMlp`, the MLP can no longer be
used. The handle *`MLPHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp(-array) `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

## Result

If *`MLPHandle`* is valid, the operator `ClearClassMlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`ClassifyClassMlp`,
`EvaluateClassMlp`

## See also

`CreateClassMlp`,
`ReadClassMlp`,
`WriteClassMlp`,
`TrainClassMlp`

## Module

Foundation
