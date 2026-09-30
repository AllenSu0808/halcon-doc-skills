# SetDescriptorModelOrigin (Operator)

## Name

`SetDescriptorModelOrigin` — Sets the origin of a descriptor model.

## Signature

`static void HOperatorSet.SetDescriptorModelOrigin(HTuple modelID, HTuple row, HTuple column)`

`void HDescriptorModel.SetDescriptorModelOrigin(HTuple row, HTuple column)`

`void HDescriptorModel.SetDescriptorModelOrigin(double row, double column)`

## Description

The operator `SetDescriptorModelOrigin` sets the origin (reference
point) of the descriptor model *`modelID`* to a new
value. The origin is specified relative to the center of gravity of the
domain (region) of the image that was used to create the descriptor model
with [`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md), or
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md). Hence, an origin of (0,0) means
that the center of gravity of the domain of the model image is used as
the origin. An origin of (-20,-40) means that the origin lies to the
upper left of the center of gravity. The new setting affects the
succeeding [`FindUncalibDescriptorModel`](find_uncalib_descriptor_model.md) and
[`FindCalibDescriptorModel`](find_calib_descriptor_model.md) calls.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a descriptor model.

**`row`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Translation of origin in row direction.

Default:
0

**`column`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Translation of origin in column direction.

Default:
0

## Possible Predecessors

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`,
`ReadDescriptorModel`

## See also

`GetDescriptorModelOrigin`,
`CreateUncalibDescriptorModel`

## Module

Matching
