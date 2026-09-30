# GetFeaturesOcrClassKnn (Operator)

## Name

`GetFeaturesOcrClassKnn` — Compute the features of a character.

## Signature

`static void HOperatorSet.GetFeaturesOcrClassKnn(HObject character, HTuple OCRHandle, HTuple transform, out HTuple features)`

`HTuple HImage.GetFeaturesOcrClassKnn(HOCRKnn OCRHandle, string transform)`

`HTuple HOCRKnn.GetFeaturesOcrClassKnn(HImage character, string transform)`

## Description

`GetFeaturesOcrClassKnn` computes the features of the
character given by *`character`* with the k-NN classifier
*`OCRHandle`* and returns them in *`features`*. In
contrast to [`DoOcrSingleClassKnn`](do_ocr_single_class_knn.md) and
[`DoOcrMultiClassKnn`](do_ocr_multi_class_knn.md), the character is passed as a single
image object. Hence, before calling
`GetFeaturesOcrClassKnn`, [`ReduceDomain`](reduce_domain.md) must
typically be called. The parameter *`transform`* determines
whether the feature transformation specified with
`preprocessing` in [`CreateOcrClassKnn`](create_ocr_class_knn.md) for the
classifier should be applied (*`transform`* =
*"true"*) or whether the untransformed features should be
returned (*`transform`* = *"false"*).
`GetFeaturesOcrClassKnn` can be used to inspect the
features that are used for the classification.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input character.

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

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

If the parameters are valid, the operator
`GetFeaturesOcrClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`

## See also

`CreateOcrClassKnn`

## Module

OCR/OCV
