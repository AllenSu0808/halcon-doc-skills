# GetSampleNumClassMlp (Operator)

## Name

`GetSampleNumClassMlp` — Return the number of training samples stored in the training data of
a multilayer perceptron.

## Signature

`static void HOperatorSet.GetSampleNumClassMlp(HTuple MLPHandle, out HTuple numSamples)`

`int HClassMlp.GetSampleNumClassMlp()`

## Description

`GetSampleNumClassMlp` returns in *`numSamples`* the
number of training samples that are stored in the multilayer
perceptron (MLP) given by *`MLPHandle`*.
`GetSampleNumClassMlp` should be called before the
individual training samples are accessed with
[`GetSampleClassMlp`](get_sample_class_mlp.md), e.g., for the purpose of reclassifying
the training data (see [`GetSampleClassMlp`](get_sample_class_mlp.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`numSamples`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training samples.

## Result

If *`MLPHandle`* is valid, the operator
`GetSampleNumClassMlp` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## Possible Predecessors

`AddSampleClassMlp`,
`ReadSamplesClassMlp`

## Possible Successors

`GetSampleClassMlp`

## See also

`CreateClassMlp`

## Module

Foundation
