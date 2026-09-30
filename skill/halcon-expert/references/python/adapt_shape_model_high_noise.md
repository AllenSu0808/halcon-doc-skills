# adapt_shape_model_high_noise (Operator)

## Name

`adapt_shape_model_high_noise` — Adapt a shape model's parameters for high noise images.

## Signature

`def adapt_shape_model_high_noise(image_reduced: HObject, model_id: HHandle, gen_param: Sequence[str]) -> HHandle`

## Description

`adapt_shape_model_high_noise` adapts the parameters of a shape model
*`model_id`* for high noise images and returns them in *`result_dict`*.
Based on a sample search image *`image_reduced`*, the optimal values of
the shape model's parameters are estimated and adapted in the model. The
domain of *`image_reduced`* should contain the model and surrounding
background, such that the typical noise is presented to the algorithm.
With *`gen_param`* the parameters to be estimated can be controlled.
Currently, the operator supports the estimation of the lowest pyramid level
used in the matching step. Accordingly, the value *"all"* or
*"lowest_level"* should be provided to *`gen_param`*.

Attention:
 The operator changes the shape model *`model_id`*
by setting the estimated lowest pyramid level.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

This operator modifies the state of the following input parameter:

- model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`image_reduced`** (input_object)  (multichannel-)image `→` HObject (byte / uint2)

Sample search image with reduced domain.

**`model_id`** (input_control, state is modified)  shape_model `→` HHandle

Handle of the shape model.

**`gen_param`** (input_control)  string-array `→` Sequence[str]

Parameters to be estimated.

Default:
"all"

List of values:
"all", "lowest_level"

**`result_dict`** (output_control)  dict `→` HHandle

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
