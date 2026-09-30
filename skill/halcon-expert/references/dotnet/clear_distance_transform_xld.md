# ClearDistanceTransformXld (Operator)

## Name

`ClearDistanceTransformXld` — Clear a XLD distance transform.

## Signature

`static void HOperatorSet.ClearDistanceTransformXld(HTuple distanceTransformID)`

`void HXLDDistTrans.ClearDistanceTransformXld()`

## Description

`ClearDistanceTransformXld` clears the XLD distance transform
*`distanceTransformID`* that was previously created by
[`CreateDistanceTransformXld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- distanceTransformID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`distanceTransformID`** (input_control, state is modified)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`CreateDistanceTransformXld`,
`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`

## See also

`ApplyDistanceTransformXld`,
`GetDistanceTransformXldContour`,
`GetDistanceTransformXldParam`,
`SetDistanceTransformXldParam`,
`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`

## Module

Foundation
