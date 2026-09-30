# GetDistanceTransformXldParam (Operator)

## Name

`GetDistanceTransformXldParam` — Get the parameters used to build an XLD distance transform.

## Signature

`static void HOperatorSet.GetDistanceTransformXldParam(HTuple distanceTransformID, HTuple genParamName, out HTuple genParamValue)`

`HTuple HXLDDistTrans.GetDistanceTransformXldParam(HTuple genParamName)`

`HTuple HXLDDistTrans.GetDistanceTransformXldParam(string genParamName)`

## Description

`GetDistanceTransformXldParam` returns the parameters used
to build the XLD distance transform *`distanceTransformID`*.
The names of the parameters are passed in *`genParamName`* and their
values are returned in *`genParamValue`*. *`genParamName`* can
contain the names of parameters *"mode"* and *"max_distance"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`distanceTransformID`** (input_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

**`genParamName`** (input_control)  attribute.name(-array) `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters.

Default:
"mode"

List of values:
"max_distance", "mode"

**`genParamValue`** (output_control)  attribute.value(-array) `→` [HTuple](HTuple.md) (*string* / double)

Values of the generic parameters.

Number of elements:
GenParamValue == 1 || GenParamValue == 2

List of values:
5.0, "point_to_point", "point_to_segment"

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`

## Possible Successors

`SetDistanceTransformXldParam`

## See also

`GetDistanceTransformXldContour`,
`CreateDistanceTransformXld`,
`ApplyDistanceTransformXld`,
`ClearDistanceTransformXld`,
`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`

## Module

Foundation
