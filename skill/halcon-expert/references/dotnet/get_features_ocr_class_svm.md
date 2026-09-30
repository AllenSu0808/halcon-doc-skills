# GetFeaturesOcrClassSvm (Operator)

## Name

`GetFeaturesOcrClassSvm` — Compute the features of a character.

## Signature

`static void HOperatorSet.GetFeaturesOcrClassSvm(HObject character, HTuple OCRHandle, HTuple transform, out HTuple features)`

`HTuple HImage.GetFeaturesOcrClassSvm(HOCRSvm OCRHandle, string transform)`

`HTuple HOCRSvm.GetFeaturesOcrClassSvm(HImage character, string transform)`

## Description

`GetFeaturesOcrClassSvm` computes the features of the
character given by *`character`* with the OCR classifier
*`OCRHandle`* and returns them in *`features`*. In
contrast to [`DoOcrSingleClassSvm`](do_ocr_single_class_svm.md) and
[`DoOcrMultiClassSvm`](do_ocr_multi_class_svm.md), the character is passed as a single
image object. Hence, before calling
`GetFeaturesOcrClassSvm`, [`ReduceDomain`](reduce_domain.md) must
typically be called. The parameter *`transform`* determines
whether the feature transformation specified with
`preprocessing` in [`CreateOcrClassSvm`](create_ocr_class_svm.md) for the
classifier should be applied (*`transform`* =
*"true"*) or whether the untransformed features should be
returned (*`transform`* = *"false"*).
`GetFeaturesOcrClassSvm` can be used to inspect the
features that are used for the classification.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input character.

**`OCRHandle`** (input_control)  ocr_svm `→` [HOCRSvm](HOCRSvm.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`transform`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should the feature vector be transformed with
the preprocessing?

Default:
"true"

List of values:
"false", "true"

**`features`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Feature vector of the character.

## Result

If the parameters are valid the operator
`GetFeaturesOcrClassSvm` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassSvm`

## See also

`CreateOcrClassSvm`

## Module

OCR/OCV
