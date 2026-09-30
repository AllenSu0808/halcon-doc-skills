# get_structured_light_model_param (Operator)

## Name

`get_structured_light_model_param` — Query parameters of a structured light model.

## Signature

`get_structured_light_model_param( : : StructuredLightModel, GenParamName : GenParamValue)`

## Description

The operator `get_structured_light_model_param` is used to query the
values of the different parameters of a structured light model
(*`StructuredLightModel`*). The names of the desired parameters are
passed in the parameter *`GenParamName`*, the corresponding values are
returned in *`GenParamValue`*. It is possible to query multiple
parameters with a single call to `get_structured_light_model_param`.

All parameters which can be manipulated by
[`set_structured_light_model_param`](set_structured_light_model_param.md) can be queried.
Please refer to the documentation of
[`set_structured_light_model_param`](set_structured_light_model_param.md) for an explanation of the
individual parameters.

The following additional parameter can be queried:

- ***'type'*:** —

  Type of the structured light model (currently either
  *'deflectometry'* or *'3d_reconstruction'*,
  as set in [`create_structured_light_model`](create_structured_light_model.md)).

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`StructuredLightModel`** (input_control)  structured_light_model `→`  (handle)

Handle of the structured light model.

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Name of the queried model parameter.

Default:
'min_stripe_width'

List of values:
'camera_setup_model', 'derivative_sigma', 'min_gray_difference', 'min_stripe_width', 'normalization', 'pattern_height', 'pattern_orientation', 'pattern_type', 'pattern_width', 'persistence', 'single_stripe_width', 'type'

**`GenParamValue`** (output_control)  attribute.value(-array) `→`  (integer / real / string)

Value of the queried model parameter.

## Example (HDevelop)

```
* Create the model
create_structured_light_model ('deflectometry', StructuredLightModel)
* Get the default value
get_structured_light_model_param (StructuredLightModel, \
                                  'min_stripe_width', Default)
* Set the value
set_structured_light_model_param (StructuredLightModel, \
                                  'min_stripe_width', 64)
* Get the value
get_structured_light_model_param (StructuredLightModel, 'min_stripe_width', \
                                  MinStripeWidth)
* Generate the patterns to project
gen_structured_light_pattern (PatternImages, StructuredLightModel)
* Decode the camera images
decode_structured_light_pattern (CameraImages, StructuredLightModel)
```

## Result

The operator `get_structured_light_model_param` returns the value
2 (
H_MSG_TRUE)
if the given parameters are valid. Otherwise, an exception will be
raised.

## Possible Predecessors

`create_structured_light_model`

## See also

`set_structured_light_model_param`

## Module

3D Metrology
