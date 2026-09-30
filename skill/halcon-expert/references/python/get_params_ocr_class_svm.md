# get_params_ocr_class_svm (Operator)

## Name

`get_params_ocr_class_svm` — Return the parameters of an OCR classifier.

## Signature

`def get_params_ocr_class_svm(ocrhandle: HHandle) -> Tuple[int, int, str, Sequence[str], Sequence[str], str, float, float, str, str, int]`

`def get_params_ocr_class_svm_s(ocrhandle: HHandle) -> Tuple[int, int, str, str, Sequence[str], str, float, float, str, str, int]`

## Description

`get_params_ocr_class_svm` returns the parameters of an OCR
classifier that were specified when the classifier was created with
[`create_ocr_class_svm`](create_ocr_class_svm.md). This is particularly useful if the
classifier was read with [`read_ocr_class_svm`](read_ocr_class_svm.md). The output of
`get_params_ocr_class_svm` can, for example, be used to check
whether a character to be read is contained in the classifier. For
a description of the parameters, see [`create_ocr_class_svm`](create_ocr_class_svm.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

Handle of the OCR classifier.

**`width_character`** (output_control)  integer `→` int

Width of the rectangle to which the gray values
of the segmented character are zoomed.

**`height_character`** (output_control)  integer `→` int

Height of the rectangle to which the gray values
of the segmented character are zoomed.

**`interpolation`** (output_control)  string `→` str

Interpolation mode for the zooming of the characters.

**`features`** (output_control)  string(-array) `→` Sequence[str]

Features to be used for classification.

**`characters`** (output_control)  string-array `→` Sequence[str]

Characters of the character set to be read.

**`kernel_type`** (output_control)  string `→` str

The kernel type.

**`kernel_param`** (output_control)  real `→` float

Additional parameters for the kernel function.

**`nu`** (output_control)  real `→` float

Regularization constant of the SVM.

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
`get_params_ocr_class_svm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_ocr_class_svm`,
`read_ocr_class_svm`

## Possible Successors

`do_ocr_single_class_svm`,
`do_ocr_multi_class_svm`

## See also

`trainf_ocr_class_svm`,
`get_params_class_svm`

## Module

OCR/OCV
