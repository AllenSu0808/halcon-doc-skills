# CreateClassLutSvm (Operator)

## Name

`CreateClassLutSvm` — Create a look-up table using a Support-Vector-Machine to classify byte
images.

## Signature

`static void HOperatorSet.CreateClassLutSvm(HTuple SVMHandle, HTuple genParamName, HTuple genParamValue, out HTuple classLUTHandle)`

`HClassLUT HClassSvm.CreateClassLutSvm(HTuple genParamName, HTuple genParamValue)`

`public HClassLUT(HClassSvm SVMHandle, HTuple genParamName, HTuple genParamValue)`

`void HClassLUT.CreateClassLutSvm(HClassSvm SVMHandle, HTuple genParamName, HTuple genParamValue)`

## Description

`CreateClassLutSvm` generates a look-up table (LUT)
*`classLUTHandle`* using the data of a trained Support-Vector-Machine
(SVM) *`SVMHandle`* to classify multi-channel byte images. By using
this SVM-based LUT classifier the operator [`ClassifyImageClassSvm`](classify_image_class_svm.md)
of the subsequent classification can be replaced by the operator
[`ClassifyImageClassLut`](classify_image_class_lut.md). The classification gets a major speed-up,
because the estimation of the class in every image point is no longer
necessary since every possible response of the SVM is stored in the LUT.
For the generation of the LUT, the parameters `numFeatures`,
`preprocessing`, and `numComponents` defined in the earlier
called operator [`CreateClassSvm`](create_class_svm.md) are important.
In `numFeatures`, the number of image channels the images must have
to be classified is defined. By using the `preprocessing`
(see [`CreateClassSvm`](create_class_svm.md)) the number of image channels can be
transformed to `numComponents`. `numComponents` defines
the length of the feature vector, which the classifier
[`ClassifyClassSvm`](classify_class_svm.md) handles internally. Because of performance and
disk space, the LUT is restricted to be maximal *3*-dimensional. Since
it replaces the operator [`ClassifyClassSvm`](classify_class_svm.md),
`numComponents` <= *3* must hold.
If there is no preprocessing that reduces the number of image channels
(`numFeatures` = `numComponents`), all possible pixel values,
which can occur in a byte image, are classified with
[`ClassifyClassSvm`](classify_class_svm.md). The returned classes are stored in the LUT.
If there is a preprocessing that reduces the number of image channels
(`numFeatures` > `numComponents`), the preprocessing
parameters of the SVM are stored in a separate structure of the LUT. To
create the LUT, all transformed pixel values are classified with
[`ClassifyClassSvm`](classify_class_svm.md).
The returned classes are stored in the LUT. Because of the discretization
of the LUT, the accuracy of the LUT classifier could become lower than the
accuracy of [`ClassifyImageClassSvm`](classify_image_class_svm.md).
With *"bit_depth"* and *"class_selection"* the accuracy of
the classification, the required storage, and the runtime needed to create
the LUT can be controlled.

The following parameters of the SVM-based LUT classifier can be set with
*`genParamName`* and *`genParamValue`*:

- ***"bit_depth"*:** —

  Number of bits used from the pixels. It controls the storage requirement
  of the LUT classifier and is bounded by the bit depth of the image
  (*"bit_depth"* <= *8*). If the bit depth of the
  LUT is smaller (*"bit_depth"* < *8*), the classes
  of multiple pixel combinations will be mapped to the same LUT entry,
  which can result in a lower accuracy for the classification. One of these
  clusters contains
  $2^{N}umComponents\cdot(8-\text{bit}_{depth})$ ![figure](../assets/71e2a1843aac7e4b.svg) pixel combinations,
  where `numComponents` denotes the dimension of the LUT, which is
  specified in [`CreateClassSvm`](create_class_svm.md). For example,
  for *"bit_depth"* = *7*,
  `numComponents` = *3*, the classes of 8 pixel
  combinations are mapped in the same LUT entry. The LUT requires at most
  $2^{N}NumComponents\cdot bit\_depth+2$ ![figure](../assets/8cd5090353586584.svg) bytes of storage.
  For example, for `numComponents` = *3*,
  *"bit_depth"* = *8* and `numClasses` < *16*
  (specified in [`CreateClassSvm`](create_class_svm.md)), the LUT requires 8 MB of storage
  with internal storage optimization. If `numClasses` = *1*,
  the LUT requires only 2 MB of storage by using the full bit depth of the
  LUT. The runtime for the classification in [`ClassifyImageClassLut`](classify_image_class_lut.md)
  becomes minimal if the LUT fits into the cache.

  Suggested values:
   *6*,*7*,*8*

  Default:
   *8*

  Restriction:
   *"bit_depth"* >= *1*,
  *"bit_depth"* <= *8*.
- ***"class_selection"*:** —

  Method for the class selection for the LUT. Can be modified to control
  the accuracy and the runtime needed to create the LUT classifier.
  The value in *"class_selection"* is ignored if the bit depth of
  the LUT is maximal, thus *"bit_depth"* = *8* holds.
  If the bit depth of the LUT is smaller
  (*"bit_depth"* < *8*), the classes of multiple pixel
  combinations will be mapped to the same LUT entry. One of these clusters
  contains
  $2^{N}umComponents\cdot(8-\text{bit}_{depth})$ ![figure](../assets/71e2a1843aac7e4b.svg) pixel combinations,
  where `numComponents` denotes the dimension of the LUT, which is
  specified in [`CreateClassSvm`](create_class_svm.md). By choosing
  *"class_selection"* = *"best"*, the class that
  appears most often in the cluster is stored in the LUT.
  For *"class_selection"* = *"fast"*, only one pixel of the
  cluster, i.e., the pixel with the smallest value (component-wise), is
  classified. The returned class is stored in the LUT. In this case, the
  accuracy of the subsequent classification could become lower. On the other
  hand, the runtime needed to create the LUT can be reduced, which is
  proportional to the maximal needed storage of the LUT, which is defined
  with
  $2^{N}NumComponents\cdot bit\_depth+2$ ![figure](../assets/8cd5090353586584.svg).

  List of values:
   *"fast"*, *"best"*

  Default:
   *"fast"*

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`SVMHandle`** (input_control)  class_svm `→` [HClassSvm](HClassSvm.md), [HTuple](HTuple.md) (*IntPtr*)

SVM handle.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Names of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
"bit_depth", "class_selection"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*string* / int / long)

Values of the generic parameters that can be adjusted
for the LUT classifier creation.

Default:
[]

Suggested values:
8, 7, 6, "fast", "best"

**`classLUTHandle`** (output_control)  class_lut `→` [HClassLUT](HClassLUT.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the LUT classifier.

## Result

If the parameters are valid, the operator `CreateClassLutSvm`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`TrainClassSvm`,
`ReadClassSvm`

## Possible Successors

`ClassifyImageClassLut`

## Alternatives

`CreateClassLutGmm`,
`CreateClassLutKnn`,
`CreateClassLutMlp`

## See also

`ClassifyImageClassLut`,
`ClearClassLut`

## Module

Foundation
