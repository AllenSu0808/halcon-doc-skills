# GetSampleNumClassGmm (Operator)

## Name

`GetSampleNumClassGmm` — Return the number of training samples stored in the training data of
a Gaussian Mixture Model (GMM).

## Signature

`static void HOperatorSet.GetSampleNumClassGmm(HTuple GMMHandle, out HTuple numSamples)`

`int HClassGmm.GetSampleNumClassGmm()`

## Description

`GetSampleNumClassGmm` returns in *`numSamples`* the
number of training samples that are stored in the Gaussian Mixture
Model (GMM) given by *`GMMHandle`*.
`GetSampleNumClassGmm` should be called before the
individual training samples are read out with
[`GetSampleClassGmm`](get_sample_class_gmm.md), e.g., for the purpose of reclassifying
the training data (see [`GetSampleClassGmm`](get_sample_class_gmm.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`GMMHandle`** (input_control)  class_gmm `→` [HClassGmm](HClassGmm.md), [HTuple](HTuple.md) (*IntPtr*)

GMM handle.

**`numSamples`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training samples.

## Result

If the parameters are valid, the operator
`GetSampleNumClassGmm` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`AddSampleClassGmm`,
`AddSamplesImageClassGmm`,
`ReadSamplesClassGmm`

## Possible Successors

`GetSampleClassGmm`

## See also

`CreateClassGmm`

## Module

Foundation
