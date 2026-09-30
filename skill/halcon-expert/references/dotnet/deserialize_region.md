# DeserializeRegion (Operator)

## Name

`DeserializeRegion` — Deserialize a serialized region.

## Signature

`static void HOperatorSet.DeserializeRegion(out HObject region, HTuple serializedItemHandle)`

`void HRegion.DeserializeRegion(HSerializedItem serializedItemHandle)`

## Description

`DeserializeRegion` deserializes a region, that was serialized
by [`SerializeRegion`](serialize_region.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized region is defined by the parameter
*`serializedItemHandle`*.
The deserialized region is stored in the region defined by the
parameter *`region`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Region.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`DeserializeRegion` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadImage`,
`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeRegion`

## Possible Successors

`ReduceDomain`,
`DispRegion`

## See also

`SerializeRegion`

## Module

Foundation
