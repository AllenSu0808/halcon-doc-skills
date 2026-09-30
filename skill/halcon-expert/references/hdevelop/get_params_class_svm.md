# get_params_class_svm (Operator)

## Name

`get_params_class_svm` — Return the parameters of a support vector machine.

## Signature

`get_params_class_svm( : : SVMHandle : NumFeatures, KernelType, KernelParam, Nu, NumClasses, Mode, Preprocessing, NumComponents)`

## Description

`get_params_class_svm` returns the parameters of a support
vector machine (SVM) that were specified when the SVM was created
with [`create_class_svm`](create_class_svm.md). This is particularly useful if the
SVM was read from a file with [`read_class_svm`](read_class_svm.md). The output of
`get_params_class_svm` can, for example, be used to check
whether the feature vectors and, if necessary, the target data to be
used with the SVM have the correct lengths. For a description of
the parameters, see [`create_class_svm`](create_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→`  (handle)

SVM handle.

**`NumFeatures`** (output_control)  integer `→`  (integer)

Number of input variables (features) of the SVM.

**`KernelType`** (output_control)  string `→`  (string)

The kernel type.

**`KernelParam`** (output_control)  real `→`  (real)

Additional parameter for the kernel.

**`Nu`** (output_control)  real `→`  (real)

Regularization constant of the SVM.

**`NumClasses`** (output_control)  integer `→`  (integer)

Number of classes of the test data.

**`Mode`** (output_control)  string `→`  (string)

The mode of the SVM.

**`Preprocessing`** (output_control)  string `→`  (string)

Type of preprocessing used to transform the
feature vectors.

**`NumComponents`** (output_control)  integer `→`  (integer)

Preprocessing parameter: Number of transformed
features (ignored for *`Preprocessing`* =
*'none'* and *`Preprocessing`* =
*'normalization'*).

## Result

If the parameters are valid the operator
`get_params_class_svm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`create_class_svm`,
`read_class_svm`

## Possible Successors

`add_sample_class_svm`,
`train_class_svm`

## See also

`classify_class_svm`

## Module

Foundation
