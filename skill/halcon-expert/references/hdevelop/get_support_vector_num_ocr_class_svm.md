# get_support_vector_num_ocr_class_svm (Operator)

## Name

`get_support_vector_num_ocr_class_svm` — Return the number of support vectors of an OCR classifier.

## Signature

`get_support_vector_num_ocr_class_svm( : : OCRHandle : NumSupportVectors, NumSVPerSVM)`

## Description

`get_support_vector_num_ocr_class_svm` returns in
*`NumSupportVectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`OCRHandle`*. `get_support_vector_num_ocr_class_svm`
should be called before the labels of individual support vectors are
read out with [`get_support_vector_ocr_class_svm`](get_support_vector_ocr_class_svm.md), e.g., for
visualizing which of the training data become a SV (see
[`get_support_vector_ocr_class_svm`](get_support_vector_ocr_class_svm.md)). The number of SVs in
each classifier is listed in *`NumSVPerSVM`*. The reason that
its sum differs from the number obtained in
*`NumSupportVectors`* is that SV evaluations are reused
throughout different binary sub-SVMs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→`  (handle)

OCR handle.

**`NumSupportVectors`** (output_control)  integer `→`  (integer)

Total number of support vectors.

**`NumSVPerSVM`** (output_control)  integer-array `→`  (integer)

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
