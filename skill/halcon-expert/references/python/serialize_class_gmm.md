# serialize_class_gmm (Operator)

## Name

`serialize_class_gmm` — Serialize a Gaussian Mixture Model (GMM).

## Signature

`def serialize_class_gmm(gmmhandle: HHandle) -> HHandle`

## Description

`serialize_class_gmm` serializes a Gaussian Mixture Model (GMM) and
its stored training samples (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`write_class_gmm`](write_class_gmm.md) and
[`write_samples_class_gmm`](write_samples_class_gmm.md) is converted to a serialized item.
The Gaussian Mixture Model is defined by the handle *`gmmhandle`*.
The serialized Gaussian Mixture Model is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_class_gmm`](deserialize_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gmmhandle`** (input_control)  class_gmm `→` HHandle

GMM handle.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_class_gmm`

## Possible Successors

`clear_class_gmm`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_class_gmm`

## See also

`create_class_gmm`,
`read_class_gmm`,
`write_samples_class_gmm`,
`deserialize_class_gmm`

## Module

Foundation
