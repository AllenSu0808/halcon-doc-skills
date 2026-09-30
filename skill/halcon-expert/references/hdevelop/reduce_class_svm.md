# reduce_class_svm (Operator)

## Name

`reduce_class_svm` — Approximate a trained support vector machine by a reduced support
vector machine for faster classification.

## Signature

`reduce_class_svm( : : SVMHandle, Method, MinRemainingSV, MaxError : SVMHandleReduced)`

## Description

As described in [`create_class_svm`](create_class_svm.md), the classification time of
a SVM depends on the number of kernel evaluations between the
support vectors and the feature vectors. While the length of the
data vectors can be reduced in a preprocessing step like
*'principal_components'* or *'canonical_variates'* (see
[`create_class_svm`](create_class_svm.md) for details), the number of resulting SV
depends on the complexity of the classification problem. The number
of SVs is determined during training. To further reduce
classification time, the number of SVs can be reduced by
approximating the original separating hyperplane with fewer SVs than
originally required. For this purpose, a copy of the original SVM
provided by *`SVMHandle`* is created and returned in
*`SVMHandleReduced`*. This new SVM has the same
parametrization as the original SVM, but a different SV expansion.
The training samples that are included in *`SVMHandle`* are not
copied. The original SVM is not modified by
`reduce_class_svm`.

The reduction method is selected with *`Method`*. Currently,
only a bottom up approach is supported, which iteratively merges SVs.
The algorithm stops if either the minimum number of SVs is reached
(*`MinRemainingSV`*) or if the accumulated maximum error exceeds
the threshold *`MaxError`*. Note that the approximation reduces
the complexity of the hyperplane and thereby leads to a deteriorated
classification rate. A common approach is therefore to start from a
small *`MaxError`* e.g., *0.001*, and to increase its
value step by step. To control the reduction ratio, at each step
the number of remaining SVs is determined with
[`get_support_vector_num_class_svm`](get_support_vector_num_class_svm.md) and the classification rate
is checked on a separate test data set with
[`classify_class_svm`](classify_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

Original SVM handle.

**`Method`** (input_control)  string `→`  (string)

Type of postprocessing to reduce number of SV.

Default:
'bottom_up'

List of values:
'bottom_up'

**`MinRemainingSV`** (input_control)  integer `→`  (integer)

Minimum number of remaining SVs.

Default:
2

Suggested values:
2, 3, 4, 5, 7, 10, 15, 20, 30, 50

Restriction:
`MinRemainingSV >= 2`

**`MaxError`** (input_control)  real `→`  (real)

Maximum allowed error of reduction.

Default:
0.001

Suggested values:
0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05

Restriction:
`MaxError > 0.0`

**`SVMHandleReduced`** (output_control)  class_svm `→`  (handle)

SVMHandle of reduced SVM.

## Example (HDevelop)

```
* Train an SVM
create_class_svm (NumFeatures, 'rbf', 0.01, 0.01, NumClasses,\
                  'one-versus-all', 'normalization', NumFeatures,\
                  SVMHandle)
read_samples_class_svm (SVMHandle, 'samples.mtf')
train_class_svm (SVMHandle, 0.001, 'default')
* Create a reduced SVM
reduce_class_svm (SVMHandle, 'bottom_up', 2, 0.01, SVMHandleReduced)
write_class_svm (SVMHandleReduced, 'classifier.svm')
```

## Result

If the parameters are valid the operator [`train_class_svm`](train_class_svm.md)
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is
raised.

## Possible Predecessors

`train_class_svm`,
`get_support_vector_num_class_svm`

## Possible Successors

`classify_class_svm`,
`write_class_svm`,
`get_support_vector_num_class_svm`

## See also

`train_class_svm`

## Module

Foundation
