# ClearClassGmm (Operator)

## Name

`ClearClassGmm` — Clear a Gaussian Mixture Model.

## Signature

`static void HOperatorSet.ClearClassGmm(HTuple GMMHandle)`

`static void HClassGmm.ClearClassGmm(HClassGmm[] GMMHandle)`

`void HClassGmm.ClearClassGmm()`

## Description

`ClearClassGmm` clears the Gaussian Mixture Model (GMM)
given by *`GMMHandle`* and frees all memory required for the
GMM. After calling `ClearClassGmm`, the GMM can no longer
be used. The handle *`GMMHandle`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- GMMHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`GMMHandle`** (input_control, state is modified)  class_gmm(-array) `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

## Result

If the parameters are valid, the operator `ClearClassGmm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is
raised.

## Possible Predecessors

`ClassifyClassGmm`,
`EvaluateClassGmm`

## See also

`CreateClassGmm`,
`ReadClassGmm`,
`WriteClassGmm`,
`TrainClassGmm`

## Module

Foundation
