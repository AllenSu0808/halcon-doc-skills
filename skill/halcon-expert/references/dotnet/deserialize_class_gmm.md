# DeserializeClassGmm (Operator)

## Name

`DeserializeClassGmm` — Deserialize a serialized Gaussian Mixture Model.

## Signature

`static void HOperatorSet.DeserializeClassGmm(HTuple serializedItemHandle, out HTuple GMMHandle)`

`void HClassGmm.DeserializeClassGmm(HSerializedItem serializedItemHandle)`

## Description

`DeserializeClassGmm` deserializes a Gaussian Mixture Model (GMM)
(including its training samples), that was serialized
by [`SerializeClassGmm`](serialize_class_gmm.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized Gaussian Mixture Model is defined by the handle
*`serializedItemHandle`*. The deserialized values are stored in an
automatically created Gaussian Mixture Model with the handle
*`GMMHandle`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`GMMHandle`** (output_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

## Result

If the parameters are valid, the operator
`DeserializeClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeClassGmm`

## Possible Successors

`ClassifyClassGmm`,
`EvaluateClassGmm`,
`CreateClassLutGmm`

## See also

`CreateClassGmm`,
`WriteClassGmm`,
`SerializeClassGmm`

## Module

Foundation
