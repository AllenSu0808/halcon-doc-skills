# get_params_class_svm (Operator)

## Name

`get_params_class_svm` — Return the parameters of a support vector machine.

## Signature

`def get_params_class_svm(svmhandle: HHandle) -> Tuple[int, str, float, float, int, str, str, int]`

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

**`svmhandle`** (input_control)  class_svm `→` HHandle

SVM handle.

**`num_features`** (output_control)  integer `→` int

Number of input variables (features) of the SVM.

**`kernel_type`** (output_control)  string `→` str

The kernel type.

**`kernel_param`** (output_control)  real `→` float

Additional parameter for the kernel.

**`nu`** (output_control)  real `→` float

Regularization constant of the SVM.

**`num_classes`** (output_control)  integer `→` int

Number of classes of the test data.

**`mode`** (output_control)  string `→` str

The mode of the SVM.

**`preprocessing`** (output_control)  string `→` str

Type of preprocessing used to transform the
feature vectors.

**`num_components`** (output_control)  integer `→` int

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`* =
*"none"* and *`preprocessing`* =
*"normalization"*).

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
