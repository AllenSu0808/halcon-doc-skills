# ClearClassSvm (Operator)

## Name

`ClearClassSvm` — Clear a support vector machine.

## Signature

`static void HOperatorSet.ClearClassSvm(HTuple SVMHandle)`

`static void HClassSvm.ClearClassSvm(HClassSvm[] SVMHandle)`

`void HClassSvm.ClearClassSvm()`

## Description

`ClearClassSvm` clears the support vector machine (SVM)
given by *`SVMHandle`* and frees all memory required for the
SVM. After calling `ClearClassSvm`, the SVM can no longer
be used. The handle *`SVMHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SVMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SVMHandle`** (input_control, state is modified)  class_svm(-array) `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

## Result

If *`SVMHandle`* is valid the operator `ClearClassSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`ClassifyClassSvm`

## See also

`CreateClassSvm`,
`ReadClassSvm`,
`WriteClassSvm`,
`TrainClassSvm`

## Module

Foundation
