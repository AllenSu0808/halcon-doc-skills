# serialize_class_svm (Operator)

## Name

`serialize_class_svm` — Serialize a support vector machine (SVM).

## Signature

`serialize_class_svm( : : SVMHandle : SerializedItemHandle)`

## Description

`serialize_class_svm` serializes a support vector machine (SVM) and
its stored training samples (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`write_class_svm`](write_class_svm.md) and
[`write_samples_class_svm`](write_samples_class_svm.md) is converted to a serialized item.
The support vector machine is defined by the handle *`SVMHandle`*.
The serialized support vector machine is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_class_svm`](deserialize_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_svm`

## Possible Successors

`clear_class_svm`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_class_svm`

## See also

`create_class_svm`,
`read_class_svm`,
`write_samples_class_svm`,
`deserialize_class_svm`

## Module

Foundation
