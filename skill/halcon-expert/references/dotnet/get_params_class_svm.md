# GetParamsClassSvm (Operator)

## Name

`GetParamsClassSvm` — Return the parameters of a support vector machine.

## Signature

`static void HOperatorSet.GetParamsClassSvm(HTuple SVMHandle, out HTuple numFeatures, out HTuple kernelType, out HTuple kernelParam, out HTuple nu, out HTuple numClasses, out HTuple mode, out HTuple preprocessing, out HTuple numComponents)`

`int HClassSvm.GetParamsClassSvm(out string kernelType, out double kernelParam, out double nu, out int numClasses, out string mode, out string preprocessing, out int numComponents)`

## Description

`GetParamsClassSvm` returns the parameters of a support
vector machine (SVM) that were specified when the SVM was created
with [`CreateClassSvm`](create_class_svm.md). This is particularly useful if the
SVM was read from a file with [`ReadClassSvm`](read_class_svm.md). The output of
`GetParamsClassSvm` can, for example, be used to check
whether the feature vectors and, if necessary, the target data to be
used with the SVM have the correct lengths. For a description of
the parameters, see [`CreateClassSvm`](create_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`numFeatures`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of input variables (features) of the SVM.

**`kernelType`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

The kernel type.

**`kernelParam`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Additional parameter for the kernel.

**`nu`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Regularization constant of the SVM.

**`numClasses`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of classes of the test data.

**`mode`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

The mode of the SVM.

**`preprocessing`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of preprocessing used to transform the
feature vectors.

**`numComponents`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Preprocessing parameter: Number of transformed
features (ignored for *`preprocessing`* =
*"none"* and *`preprocessing`* =
*"normalization"*).

## Result

If the parameters are valid the operator
`GetParamsClassSvm` returns the value 2 (
H_MSG_TRUE)
. If necessary,
an exception is raised.

## Possible Predecessors

`CreateClassSvm`,
`ReadClassSvm`

## Possible Successors

`AddSampleClassSvm`,
`TrainClassSvm`

## See also

`ClassifyClassSvm`

## Module

Foundation
