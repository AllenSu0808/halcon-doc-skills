# deserialize_class_svm (Operator)

## Name

`deserialize_class_svm` — Deserialize a serialized support vector machine (SVM).

## Signature

`deserialize_class_svm( : : SerializedItemHandle : SVMHandle)`

## Description

`deserialize_class_svm` deserializes a support vector machine (SVM)
(including its training samples), that was serialized
by [`serialize_class_svm`](serialize_class_svm.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized support vector machine is defined by the handle
*`SerializedItemHandle`*. The deserialized values are stored in an
automatically created support vector machine with the handle
*`SVMHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`SVMHandle`** (output_control)  class_svm `→`  (handle)

SVM handle.

## Result

If the parameters are valid, the operator
`deserialize_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_class_svm`

## Possible Successors

`classify_class_svm`,
`create_class_lut_svm`

## See also

`create_class_svm`,
`write_class_svm`,
`serialize_class_svm`

## Module

Foundation
