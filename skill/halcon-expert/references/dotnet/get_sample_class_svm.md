# GetSampleClassSvm (Operator)

## Name

`GetSampleClassSvm` — Return a training sample from the training data of a support vector
machine.

## Signature

`static void HOperatorSet.GetSampleClassSvm(HTuple SVMHandle, HTuple indexSample, out HTuple features, out HTuple target)`

`HTuple HClassSvm.GetSampleClassSvm(int indexSample, out int target)`

## Description

`GetSampleClassSvm` reads out a training sample from the
support vector machine (SVM) given by *`SVMHandle`* that was
added with [`AddSampleClassSvm`](add_sample_class_svm.md) or
[`ReadSamplesClassSvm`](read_samples_class_svm.md). The index of the sample is
specified with *`indexSample`*. The index is counted from 0,
i.e., *`indexSample`* must be a number between 0 and
`numSamples` - 1, where `numSamples` can be
determined with [`GetSampleNumClassSvm`](get_sample_num_class_svm.md). The training
sample is returned in *`features`* and *`target`*.
*`features`* is a feature vector of length
`numFeatures` (see [`CreateClassSvm`](create_class_svm.md)), while *`target`*
is the index of the class, ranging between 0 and `numClasses`-1 (see
[`AddSampleClassSvm`](add_sample_class_svm.md)).

`GetSampleClassSvm` can, for example, be used to reclassify
the training data with [`ClassifyClassSvm`](classify_class_svm.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`indexSample`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of the stored training sample.

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the training sample.

**`target`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Target vector of the training sample.

## Example (HDevelop)

```
* Train an SVM
create_class_svm (NumFeatures, 'rbf', 0.01, 0.01, NumClasses,\
                  'one-versus-all', 'normalization', NumFeatures,\
                  SVMHandle)
read_samples_class_svm (SVMHandle, 'samples.mtf')
train_class_svm (SVMHandle, 0.001, 'default')
* Reclassify the training samples
get_sample_num_class_svm (SVMHandle, NumSamples)
for I := 0 to NumSamples-1 by 1
    get_sample_class_svm (SVMHandle, I, Data, Target)
    classify_class_svm (SVMHandle, Data, 1, Class)
    if (Class != Target)
        * Sample has been classified incorrectly
    endif
endfor
```

## Result

If the parameters are valid the operator
`GetSampleClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`AddSampleClassSvm`,
`ReadSamplesClassSvm`,
`GetSampleNumClassSvm`,
`GetSupportVectorClassSvm`

## Possible Successors

`ClassifyClassSvm`

## See also

`CreateClassSvm`

## Module

Foundation
