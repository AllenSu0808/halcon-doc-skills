# serialize_class_train_data (Operator)

## Name

`serialize_class_train_data` — Serialize training data for classifiers.

## Signature

`serialize_class_train_data( : : ClassTrainDataHandle : SerializedItemHandle)`

## Description

`serialize_class_train_data` serializes training data for classifiers
and its stored training samples (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`write_class_train_data`](write_class_train_data.md) is converted to a
serialized item. The training data is defined by the handle
*`ClassTrainDataHandle`*. The serialized training data is returned by
the handle *`SerializedItemHandle`* and can be deserialized by
[`deserialize_class_train_data`](deserialize_class_train_data.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ClassTrainDataHandle`** (input_control)  class_train_data `→`  (handle)

Handle of the training data.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_class_train_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`deserialize_class_train_data`

## See also

`create_class_train_data`,
`read_class_train_data`

## Module

Foundation
