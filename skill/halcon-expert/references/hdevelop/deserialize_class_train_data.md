# deserialize_class_train_data (Operator)

## Name

`deserialize_class_train_data` — Deserialize serialized training data for classifiers.

## Signature

`deserialize_class_train_data( : : SerializedItemHandle : ClassTrainDataHandle)`

## Description

`deserialize_class_train_data` deserializes training data for
classifiers, that were serialized
by [`serialize_class_train_data`](serialize_class_train_data.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized training data is defined by the handle
*`SerializedItemHandle`*. The deserialized values are stored in an
automatically created training data block with the handle
*`ClassTrainDataHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`ClassTrainDataHandle`** (output_control)  class_train_data `→`  (handle)

Handle of the training data.

## Result

If the parameters are valid, the operator
`deserialize_class_train_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`serialize_class_train_data`

## Possible Successors

`fwrite_serialized_item`

## See also

`create_class_train_data`

## Module

Foundation
