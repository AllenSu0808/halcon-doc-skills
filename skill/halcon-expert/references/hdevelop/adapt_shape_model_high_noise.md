# adapt_shape_model_high_noise (Operator)

## Name

`adapt_shape_model_high_noise` — Adapt a shape model's parameters for high noise images.

## Signature

`adapt_shape_model_high_noise(ImageReduced : : ModelID, GenParam : ResultDict)`

## Description

`adapt_shape_model_high_noise` adapts the parameters of a shape model
*`ModelID`* for high noise images and returns them in *`ResultDict`*.
Based on a sample search image *`ImageReduced`*, the optimal values of
the shape model's parameters are estimated and adapted in the model. The
domain of *`ImageReduced`* should contain the model and surrounding
background, such that the typical noise is presented to the algorithm.
With *`GenParam`* the parameters to be estimated can be controlled.
Currently, the operator supports the estimation of the lowest pyramid level
used in the matching step. Accordingly, the value *'all'* or
*'lowest_level'* should be provided to *`GenParam`*.

Attention:
 The operator changes the shape model *`ModelID`*
by setting the estimated lowest pyramid level.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator modifies the state of the following input parameter:

- ModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ImageReduced`** (input_object)  (multichannel-)image `→` object (byte / uint2)

Sample search image with reduced domain.

**`ModelID`** (input_control, state is modified)  shape_model `→`  (handle)

Handle of the shape model.

**`GenParam`** (input_control)  string-array `→`  (string)

Parameters to be estimated.

Default:
'all'

List of values:
'all', 'lowest_level'

**`ResultDict`** (output_control)  dict `→`  (handle)

Dictionary with the estimated parameter values.

## Result

If the parameters are valid, the operator
`adapt_shape_model_high_noise` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_generic_shape_model`

## Possible Successors

`find_generic_shape_model`

## Module

Matching
