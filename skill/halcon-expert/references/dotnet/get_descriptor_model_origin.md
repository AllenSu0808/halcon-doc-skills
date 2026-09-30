# GetDescriptorModelOrigin (Operator)

## Name

`GetDescriptorModelOrigin` — Return the origin of a descriptor model.

## Signature

`static void HOperatorSet.GetDescriptorModelOrigin(HTuple modelID, out HTuple row, out HTuple column)`

`void HDescriptorModel.GetDescriptorModelOrigin(out HTuple row, out HTuple column)`

`void HDescriptorModel.GetDescriptorModelOrigin(out double row, out double column)`

## Description

The operator `GetDescriptorModelOrigin` returns the origin
(reference point) of the descriptor model *`modelID`*.
The origin is specified relative to the center of gravity of the domain
(region) of the image that was used to create the descriptor model
with [`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md), or
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md). Hence, an origin of (0,0) means
that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a descriptor model.

**`row`** (output_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Position of origin in row direction.

**`column`** (output_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Position of origin in column direction.

## Possible Predecessors

`CreateUncalibDescriptorModel`,
`ReadDescriptorModel`

## See also

`SetDescriptorModelOrigin`,
`CreateUncalibDescriptorModel`

## Module

Matching
