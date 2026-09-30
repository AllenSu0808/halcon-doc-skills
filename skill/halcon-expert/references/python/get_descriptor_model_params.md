# get_descriptor_model_params (Operator)

## Name

`get_descriptor_model_params` — Return the parameters of a descriptor model.

## Signature

`def get_descriptor_model_params(model_id: HHandle) -> Tuple[str, Sequence[str], Sequence[Union[int, float, str]], Sequence[str], Sequence[Union[int, float, str]]]`

## Description

The operator `get_descriptor_model_params` allows to access the
parameters of a descriptor model that was created with
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md) or
[`create_calib_descriptor_model`](create_calib_descriptor_model.md). Therefore, a handle of a
descriptor model must be passed in *`model_id`*.
The operator returns in *`detector_type`*, *`detector_param_name`*
and *`detector_param_value`* the type and parametrization of the
detector. In DescriptorType, *`descriptor_param_name`* and
*`descriptor_param_value`* the respective descriptor is returned.

An application for this operator is the possibility to query the
parameters that where used in a stored model. As the operator needs a
handle to a descriptor model, it has to be loaded first by using
[`read_descriptor_model`](read_descriptor_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`model_id`** (input_control)  descriptor_model `→` HHandle

The object handle to the descriptor model.

**`detector_type`** (output_control)  string `→` str

The type of the detector.

**`detector_param_name`** (output_control)  attribute.name-array `→` Sequence[str]

The detectors parameter names.

**`detector_param_value`** (output_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Values of the detectors parameters.

**`descriptor_param_name`** (output_control)  attribute.name-array `→` Sequence[str]

The descriptors parameter names.

**`descriptor_param_value`** (output_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Values of the descriptors parameters.

## Possible Predecessors

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`,
`read_descriptor_model`

## See also

`create_uncalib_descriptor_model`,
`create_calib_descriptor_model`

## Module

Matching
