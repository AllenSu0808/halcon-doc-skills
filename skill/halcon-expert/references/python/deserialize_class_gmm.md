# deserialize_class_gmm (Operator)

## Name

`deserialize_class_gmm` — Deserialize a serialized Gaussian Mixture Model.

## Signature

`def deserialize_class_gmm(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_class_gmm` deserializes a Gaussian Mixture Model (GMM)
(including its training samples), that was serialized
by [`serialize_class_gmm`](serialize_class_gmm.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized Gaussian Mixture Model is defined by the handle
*`serialized_item_handle`*. The deserialized values are stored in an
automatically created Gaussian Mixture Model with the handle
*`gmmhandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`gmmhandle`** (output_control)  class_gmm `→` HHandle

GMM handle.

## Result

If the parameters are valid, the operator
`deserialize_class_gmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_class_gmm`

## Possible Successors

`classify_class_gmm`,
`evaluate_class_gmm`,
`create_class_lut_gmm`

## See also

`create_class_gmm`,
`write_class_gmm`,
`serialize_class_gmm`

## Module

Foundation
