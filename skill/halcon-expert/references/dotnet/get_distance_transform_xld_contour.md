# GetDistanceTransformXldContour (Operator)

## Name

`GetDistanceTransformXldContour` — Get the reference contour used to build the XLD distance transform.

## Signature

`static void HOperatorSet.GetDistanceTransformXldContour(out HObject contour, HTuple distanceTransformID)`

`HXLDCont HXLDDistTrans.GetDistanceTransformXldContour()`

## Description

`GetDistanceTransformXldContour` returns the reference contour
*`contour`* that was used to build the XLD distance transform
*`distanceTransformID`*.
This can be used for visualization purposes while comparing a given contour
against the reference contour using [`ApplyDistanceTransformXld`](apply_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Reference contour.

**`distanceTransformID`** (input_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`

## See also

`GetDistanceTransformXldParam`,
`SetDistanceTransformXldParam`,
`CreateDistanceTransformXld`,
`ApplyDistanceTransformXld`,
`ClearDistanceTransformXld`,
`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`

## Module

Foundation
