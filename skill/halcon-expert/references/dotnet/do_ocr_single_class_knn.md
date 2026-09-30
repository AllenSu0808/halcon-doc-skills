# DoOcrSingleClassKnn (Operator)

## Name

`DoOcrSingleClassKnn` — Classify a single character with an OCR classifier.

## Signature

`static void HOperatorSet.DoOcrSingleClassKnn(HObject character, HObject image, HTuple OCRHandle, HTuple numClasses, HTuple numNeighbors, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrSingleClassKnn(HImage image, HOCRKnn OCRHandle, HTuple numClasses, HTuple numNeighbors, out HTuple confidence)`

`string HRegion.DoOcrSingleClassKnn(HImage image, HOCRKnn OCRHandle, HTuple numClasses, HTuple numNeighbors, out double confidence)`

`HTuple HOCRKnn.DoOcrSingleClassKnn(HRegion character, HImage image, HTuple numClasses, HTuple numNeighbors, out HTuple confidence)`

`string HOCRKnn.DoOcrSingleClassKnn(HRegion character, HImage image, HTuple numClasses, HTuple numNeighbors, out double confidence)`

## Description

`DoOcrSingleClassKnn` uses the OCR-k-NN classifier
*`OCRHandle`* to determine the best training samples for the
features of the character given by the region *`character`* and
the gray values *`image`* and returns their classes in
*`classVal`* and the corresponding confidences in *`confidence`*.
If the first *`numNeighbors`* training vectors have different classes,
maximally *`numClasses`* classes are returned sorted by frequency
and weighted distance.
The confidences lie between 0.0 and 1.0. The larger the value, the
more reliable is the classification.
The confidence can be only computed robustly
if *`numNeighbors`* is large enough.

Because multiple classes may be returned by
`DoOcrSingleClassKnn`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`DoOcrMultiClassKnn`](do_ocr_multi_class_knn.md) must
be used. Before calling `DoOcrSingleClassKnn`, the classifier must
be trained with [`TrainfOcrClassKnn`](trainf_ocr_class_knn.md) or
[`SelectFeatureSetTrainfKnn`](select_feature_set_trainf_knn.md).
If all *`numNeighbors`* neighbors are of the same class, only
one class is returned.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` [HRegion](HRegion.md)

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_knn `→` [HOCRKnn](HOCRKnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the k-NN classifier.

**`numClasses`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of maximal classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`numNeighbors`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of neighbors to consider.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Results of classifying the character with the
k-NN.

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence(s) of the class(es) of the character.

## Result

If the parameters are valid, the operator
`DoOcrSingleClassKnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`TrainfOcrClassKnn`,
`ReadOcrClassKnn`

## Alternatives

`DoOcrMultiClassKnn`

## See also

`CreateOcrClassKnn`,
`ClassifyClassKnn`

## Module

OCR/OCV
