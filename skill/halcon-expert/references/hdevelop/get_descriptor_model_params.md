# get_descriptor_model_params (Operator)

## Name

`get_descriptor_model_params` — Return the parameters of a descriptor model.

## Signature

`get_descriptor_model_params( : : ModelID : DetectorType, DetectorParamName, DetectorParamValue, DescriptorParamName, DescriptorParamValue)`

## Description

The operator `get_descriptor_model_params` allows to access the
parameters of a descriptor model that was created with
[`create_uncalib_descriptor_model`](create_uncalib_descriptor_model.md) or
[`create_calib_descriptor_model`](create_calib_descriptor_model.md). Therefore, a handle of a
descriptor model must be passed in *`ModelID`*.
The operator returns in *`DetectorType`*, *`DetectorParamName`*
and *`DetectorParamValue`* the type and parametrization of the
detector. In DescriptorType, *`DescriptorParamName`* and
*`DescriptorParamValue`* the respective descriptor is returned.

An application for this operator is the possibility to query the
parameters that where used in a stored model. As the operator needs a
handle to a descriptor model, it has to be loaded first by using
[`read_descriptor_model`](read_descriptor_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ModelID`** (input_control)  descriptor_model `→`  (handle)

The object handle to the descriptor model.

**`DetectorType`** (output_control)  string `→`  (string)

The type of the detector.

**`DetectorParamName`** (output_control)  attribute.name-array `→`  (string)

The detectors parameter names.

**`DetectorParamValue`** (output_control)  attribute.value-array `→`  (integer / real / string)

Values of the detectors parameters.

**`DescriptorParamName`** (output_control)  attribute.name-array `→`  (string)

The descriptors parameter names.

**`DescriptorParamValue`** (output_control)  attribute.value-array `→`  (integer / real / string)

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
