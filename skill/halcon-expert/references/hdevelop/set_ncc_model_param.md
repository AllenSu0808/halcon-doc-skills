# set_ncc_model_param (Operator)

## Name

`set_ncc_model_param` — Set selected parameters of the NCC model.

## Signature

`set_ncc_model_param( : : ModelID, GenParamName, GenParamValue : )`

## Description

The operator `set_ncc_model_param` sets the selected parameters
*`GenParamName`* in the NCC model *`ModelID`*. The following
parameters can be modified:

*'timeout'*

Sets the maximum runtime of the operators used to find the NCC model
*`ModelID`* (using [`find_ncc_model`](find_ncc_model.md)). This is especially useful
in cases where a maximum cycle time has to be ensured. The *'timeout'*
must be given in milliseconds. The temporal accuracy depends on several
factors including the size of the model, the speed of your computer, and
the *'timer_mode'* set via [`set_system`](set_system.md). Be aware that the
runtime of the search increases by up to 10 percent with activated timeout.
To disable the timeout you can either use a negative value or
*'false'*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ModelID`** (input_control, state is modified)  ncc_model `→`  (handle)

Handle of the model.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Parameter names.

List of values:
'timeout'

**`GenParamValue`** (input_control)  attribute.value-array `→`  (real / integer / string)

Parameter values.

## Result

If the parameters are valid, the operator `set_ncc_model_param`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`create_ncc_model`

## Possible Successors

`find_ncc_model`

## Module

Matching
