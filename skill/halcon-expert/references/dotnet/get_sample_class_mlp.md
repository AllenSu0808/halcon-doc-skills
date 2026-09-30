# GetSampleClassMlp (Operator)

## Name

`GetSampleClassMlp` — Return a training sample from the training data of a multilayer
perceptron.

## Signature

`static void HOperatorSet.GetSampleClassMlp(HTuple MLPHandle, HTuple indexSample, out HTuple features, out HTuple target)`

`HTuple HClassMlp.GetSampleClassMlp(int indexSample, out HTuple target)`

## Description

`GetSampleClassMlp` reads out a training sample from the
multilayer perceptron (MLP) given by *`MLPHandle`* that was
added with [`AddSampleClassMlp`](add_sample_class_mlp.md) or
[`ReadSamplesClassMlp`](read_samples_class_mlp.md). The index of the sample is
specified with *`indexSample`*. The index is counted from 0,
i.e., *`indexSample`* must be a number between 0 and
`numSamples` - 1, where `numSamples` can be
determined with [`GetSampleNumClassMlp`](get_sample_num_class_mlp.md). The training
sample is returned in *`features`* and *`target`*.
*`features`* is a feature vector of length `numInput`,
while *`target`* is a target vector of length
`numOutput` (see [`AddSampleClassMlp`](add_sample_class_mlp.md) and
[`CreateClassMlp`](create_class_mlp.md)).

`GetSampleClassMlp` can, for example, be used to reclassify
the training data with [`ClassifyClassMlp`](classify_class_mlp.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MLPHandle`** (input_control)  class_mlp `→` [HClassMlp](HClassMlp.md), [HTuple](HTuple.md) (*IntPtr*)

MLP handle.

**`indexSample`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of stored training sample.

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`target`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Target vector of the training sample.

## Example (HDevelop)

```
* Train an MLP
create_class_mlp (NumIn, NumHidden, NumOut, 'softmax', \
                  'canonical_variates', NumComp, 42, MLPHandle)
read_samples_class_mlp (MLPHandle, 'samples.mtf')
train_class_mlp (MLPHandle, 100, 1, 0.01, Error, ErrorLog)
* Reclassify the training samples
get_sample_num_class_mlp (MLPHandle, NumSamples)
for I := 0 to NumSamples-1 by 1
    get_sample_class_mlp (MLPHandle, I, Data, Target)
    classify_class_mlp (MLPHandle, Data, 1, Class, Confidence)
    Result := gen_tuple_const(NumOut,0)
    Result[Class] := 1
    Diffs := Target-Result
    if (sum(fabs(Diffs)) > 0)
        * Sample has been classified incorrectly
    endif
endfor
```

## Result

If the parameters are valid, the operator
`GetSampleClassMlp` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`AddSampleClassMlp`,
`ReadSamplesClassMlp`,
`GetSampleNumClassMlp`

## Possible Successors

`ClassifyClassMlp`,
`EvaluateClassMlp`

## See also

`CreateClassMlp`

## Module

Foundation
