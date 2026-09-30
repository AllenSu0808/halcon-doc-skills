# get_sample_class_svm (Operator)

## Name

`get_sample_class_svm` — Return a training sample from the training data of a support vector
machine.

## Signature

`def get_sample_class_svm(svmhandle: HHandle, index_sample: int) -> Tuple[Sequence[float], int]`

## Description

`get_sample_class_svm` reads out a training sample from the
support vector machine (SVM) given by *`svmhandle`* that was
added with [`add_sample_class_svm`](add_sample_class_svm.md) or
[`read_samples_class_svm`](read_samples_class_svm.md). The index of the sample is
specified with *`index_sample`*. The index is counted from 0,
i.e., *`index_sample`* must be a number between 0 and
`num_samples` - 1, where `num_samples` can be
determined with [`get_sample_num_class_svm`](get_sample_num_class_svm.md). The training
sample is returned in *`features`* and *`target`*.
*`features`* is a feature vector of length
`num_features` (see [`create_class_svm`](create_class_svm.md)), while *`target`*
is the index of the class, ranging between 0 and `num_classes`-1 (see
[`add_sample_class_svm`](add_sample_class_svm.md)).

`get_sample_class_svm` can, for example, be used to reclassify
the training data with [`classify_class_svm`](classify_class_svm.md) in order to
determine which training samples, if any, are classified
incorrectly.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`index_sample`** (input_control)  integer `→` int

Number of the stored training sample.

**`features`** (output_control)  real-array `→` Sequence[float]

Feature vector of the training sample.

**`target`** (output_control)  integer `→` int

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
`get_sample_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`add_sample_class_svm`,
`read_samples_class_svm`,
`get_sample_num_class_svm`,
`get_support_vector_class_svm`

## Possible Successors

`classify_class_svm`

## See also

`create_class_svm`

## Module

Foundation
