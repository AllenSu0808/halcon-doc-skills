# get_support_vector_num_ocr_class_svm (Operator)

## Name

`get_support_vector_num_ocr_class_svm` — Return the number of support vectors of an OCR classifier.

## Signature

`def get_support_vector_num_ocr_class_svm(ocrhandle: HHandle) -> Tuple[int, Sequence[int]]`

## Description

`get_support_vector_num_ocr_class_svm` returns in
*`num_support_vectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`ocrhandle`*. `get_support_vector_num_ocr_class_svm`
should be called before the labels of individual support vectors are
read out with [`get_support_vector_ocr_class_svm`](get_support_vector_ocr_class_svm.md), e.g., for
visualizing which of the training data become a SV (see
[`get_support_vector_ocr_class_svm`](get_support_vector_ocr_class_svm.md)). The number of SVs in
each classifier is listed in *`num_svper_svm`*. The reason that
its sum differs from the number obtained in
*`num_support_vectors`* is that SV evaluations are reused
throughout different binary sub-SVMs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ocrhandle`** (input_control)  ocr_svm `→` HHandle

OCR handle.

**`num_support_vectors`** (output_control)  integer `→` int

Total number of support vectors.

**`num_svper_svm`** (output_control)  integer-array `→` Sequence[int]

Number of SV of each sub-SVM.

## Result

If the parameters are valid the operator
[`get_sample_num_class_svm`](get_sample_num_class_svm.md) returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`trainf_ocr_class_svm`

## Possible Successors

`get_support_vector_ocr_class_svm`

## See also

`create_ocr_class_svm`

## Module

OCR/OCV
