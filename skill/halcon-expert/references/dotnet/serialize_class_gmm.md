# SerializeClassGmm (Operator)

## Name

`SerializeClassGmm` — Serialize a Gaussian Mixture Model (GMM).

## Signature

`static void HOperatorSet.SerializeClassGmm(HTuple GMMHandle, out HTuple serializedItemHandle)`

`HSerializedItem HClassGmm.SerializeClassGmm()`

## Description

`SerializeClassGmm` serializes a Gaussian Mixture Model (GMM) and
its stored training samples (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The same data that
is written in a file by [`WriteClassGmm`](write_class_gmm.md) and
[`WriteSamplesClassGmm`](write_samples_class_gmm.md) is converted to a serialized item.
The Gaussian Mixture Model is defined by the handle *`GMMHandle`*.
The serialized Gaussian Mixture Model is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeClassGmm`](deserialize_class_gmm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainClassGmm`

## Possible Successors

`ClearClassGmm`,
`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeClassGmm`

## See also

`CreateClassGmm`,
`ReadClassGmm`,
`WriteSamplesClassGmm`,
`DeserializeClassGmm`

## Module

Foundation
