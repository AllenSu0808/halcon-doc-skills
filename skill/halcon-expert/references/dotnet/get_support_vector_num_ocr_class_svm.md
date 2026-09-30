# GetSupportVectorNumOcrClassSvm (Operator)

## Name

`GetSupportVectorNumOcrClassSvm` — Return the number of support vectors of an OCR classifier.

## Signature

`static void HOperatorSet.GetSupportVectorNumOcrClassSvm(HTuple OCRHandle, out HTuple numSupportVectors, out HTuple numSVPerSVM)`

`int HOCRSvm.GetSupportVectorNumOcrClassSvm(out HTuple numSVPerSVM)`

## Description

`GetSupportVectorNumOcrClassSvm` returns in
*`numSupportVectors`* the number of support vectors that are
stored in the support vector machine (SVM) given by
*`OCRHandle`*. `GetSupportVectorNumOcrClassSvm`
should be called before the labels of individual support vectors are
read out with [`GetSupportVectorOcrClassSvm`](get_support_vector_ocr_class_svm.md), e.g., for
visualizing which of the training data become a SV (see
[`GetSupportVectorOcrClassSvm`](get_support_vector_ocr_class_svm.md)). The number of SVs in
each classifier is listed in *`numSVPerSVM`*. The reason that
its sum differs from the number obtained in
*`numSupportVectors`* is that SV evaluations are reused
throughout different binary sub-SVMs.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

OCR handle.

**`numSupportVectors`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Total number of support vectors.

**`numSVPerSVM`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of SV of each sub-SVM.

## Result

If the parameters are valid the operator
[`GetSampleNumClassSvm`](get_sample_num_class_svm.md) returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`

## Possible Successors

`GetSupportVectorOcrClassSvm`

## See also

`CreateOcrClassSvm`

## Module

OCR/OCV
