# GetDescriptorModelParams (Operator)

## Name

`GetDescriptorModelParams` — Return the parameters of a descriptor model.

## Signature

`static void HOperatorSet.GetDescriptorModelParams(HTuple modelID, out HTuple detectorType, out HTuple detectorParamName, out HTuple detectorParamValue, out HTuple descriptorParamName, out HTuple descriptorParamValue)`

`string HDescriptorModel.GetDescriptorModelParams(out HTuple detectorParamName, out HTuple detectorParamValue, out HTuple descriptorParamName, out HTuple descriptorParamValue)`

## Description

The operator `GetDescriptorModelParams` allows to access the
parameters of a descriptor model that was created with
[`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md) or
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md). Therefore, a handle of a
descriptor model must be passed in *`modelID`*.
The operator returns in *`detectorType`*, *`detectorParamName`*
and *`detectorParamValue`* the type and parametrization of the
detector. In DescriptorType, *`descriptorParamName`* and
*`descriptorParamValue`* the respective descriptor is returned.

An application for this operator is the possibility to query the
parameters that where used in a stored model. As the operator needs a
handle to a descriptor model, it has to be loaded first by using
[`ReadDescriptorModel`](read_descriptor_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

The object handle to the descriptor model.

**`detectorType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the detector.

**`detectorParamName`** (output_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

The detectors parameter names.

**`detectorParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the detectors parameters.

**`descriptorParamName`** (output_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

The descriptors parameter names.

**`descriptorParamValue`** (output_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Values of the descriptors parameters.

## Possible Predecessors

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`,
`ReadDescriptorModel`

## See also

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Module

Matching
