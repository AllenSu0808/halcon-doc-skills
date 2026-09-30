# clear_class_mlp (Operator)

## Name

`clear_class_mlp` — Clear a multilayer perceptron.

## Signature

`clear_class_mlp( : : MLPHandle : )`

## Description

`clear_class_mlp` clears the multilayer perceptron (MLP) given
by *`MLPHandle`* and frees all memory required for the MLP.
After calling `clear_class_mlp`, the MLP can no longer be
used. The handle *`MLPHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MLPHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MLPHandle`** (input_control, state is modified)  class_mlp(-array) `→`  (handle)

MLP handle.

## Result

If *`MLPHandle`* is valid, the operator `clear_class_mlp`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`classify_class_mlp`,
`evaluate_class_mlp`

## See also

`create_class_mlp`,
`read_class_mlp`,
`write_class_mlp`,
`train_class_mlp`

## Module

Foundation
