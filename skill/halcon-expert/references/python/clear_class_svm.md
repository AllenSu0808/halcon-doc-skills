# clear_class_svm (Operator)

## Name

`clear_class_svm` — Clear a support vector machine.

## Signature

`def clear_class_svm(svmhandle: MaybeSequence[HHandle]) -> None`

## Description

`clear_class_svm` clears the support vector machine (SVM)
given by *`svmhandle`* and frees all memory required for the
SVM. After calling `clear_class_svm`, the SVM can no longer
be used. The handle *`svmhandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- svmhandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`svmhandle`** (input_control, state is modified)  class_svm(-array) `→` MaybeSequence[HHandle]

SVM handle.

## Result

If *`svmhandle`* is valid the operator `clear_class_svm`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`classify_class_svm`

## See also

`create_class_svm`,
`read_class_svm`,
`write_class_svm`,
`train_class_svm`

## Module

Foundation
