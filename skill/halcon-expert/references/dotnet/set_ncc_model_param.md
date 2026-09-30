# SetNccModelParam (Operator)

## Name

`SetNccModelParam` — Set selected parameters of the NCC model.

## Signature

`static void HOperatorSet.SetNccModelParam(HTuple modelID, HTuple genParamName, HTuple genParamValue)`

`void HNCCModel.SetNccModelParam(HTuple genParamName, HTuple genParamValue)`

`static void HImage.SetNccModelParam(HNCCModel modelID, HTuple genParamName, HTuple genParamValue)`

## Description

The operator `SetNccModelParam` sets the selected parameters
*`genParamName`* in the NCC model *`modelID`*. The following
parameters can be modified:

*"timeout"*

Sets the maximum runtime of the operators used to find the NCC model
*`modelID`* (using [`FindNccModel`](find_ncc_model.md)). This is especially useful
in cases where a maximum cycle time has to be ensured. The *"timeout"*
must be given in milliseconds. The temporal accuracy depends on several
factors including the size of the model, the speed of your computer, and
the *"timer_mode"* set via [`SetSystem`](set_system.md). Be aware that the
runtime of the search increases by up to 10 percent with activated timeout.
To disable the timeout you can either use a negative value or
*"false"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Parameter names.

List of values:
"timeout"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

## Result

If the parameters are valid, the operator `SetNccModelParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`CreateNccModel`

## Possible Successors

`FindNccModel`

## Module

Matching
