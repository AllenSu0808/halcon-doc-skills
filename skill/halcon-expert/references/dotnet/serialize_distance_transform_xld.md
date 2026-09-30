# SerializeDistanceTransformXld (Operator)

## Name

`SerializeDistanceTransformXld` — Serialize an XLD distance transform.

## Signature

`static void HOperatorSet.SerializeDistanceTransformXld(HTuple distanceTransformID, out HTuple serializedItemHandle)`

`HSerializedItem HXLDDistTrans.SerializeDistanceTransformXld()`

## Description

`SerializeDistanceTransformXld` serializes the XLD distance
transform *`distanceTransformID`*. The serialized XLD distance
transform is returned in the handle *`serializedItemHandle`* and
can be deserialized with [`DeserializeDistanceTransformXld`](deserialize_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`distanceTransformID`** (input_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized XLD distance
transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`CreateDistanceTransformXld`

## Possible Successors

`ClearDistanceTransformXld`

## Alternatives

`WriteDistanceTransformXld`

## See also

`DeserializeDistanceTransformXld`,
`ReadDistanceTransformXld`,
`ApplyDistanceTransformXld`,
`GetDistanceTransformXldContour`,
`GetDistanceTransformXldParam`,
`SetDistanceTransformXldParam`

## Module

Foundation
