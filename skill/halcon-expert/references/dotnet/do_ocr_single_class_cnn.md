# DoOcrSingleClassCnn (Operator)

## Name

`DoOcrSingleClassCnn` — Classify a single character with an CNN-based OCR classifier.

## Signature

`static void HOperatorSet.DoOcrSingleClassCnn(HObject character, HObject image, HTuple OCRHandle, HTuple num, out HTuple classVal, out HTuple confidence)`

`HTuple HRegion.DoOcrSingleClassCnn(HImage image, HOCRCnn OCRHandle, HTuple num, out HTuple confidence)`

`string HRegion.DoOcrSingleClassCnn(HImage image, HOCRCnn OCRHandle, HTuple num, out double confidence)`

`HTuple HOCRCnn.DoOcrSingleClassCnn(HRegion character, HImage image, HTuple num, out HTuple confidence)`

`string HOCRCnn.DoOcrSingleClassCnn(HRegion character, HImage image, HTuple num, out double confidence)`

## Description

`DoOcrSingleClassCnn` computes the best classification for the
character given by the region *`character`*
and the gray values *`image`* with the OCR classifier
*`OCRHandle`* and returns the best *`num`* classes in
*`classVal`* and the corresponding confidences (probabilities) of the
classes in *`confidence`*. Because multiple classes may be returned by
`DoOcrSingleClassCnn`, *`character`* may only contain
a single region (a single character). If multiple characters should
be classified in a single call, [`DoOcrMultiClassCnn`](do_ocr_multi_class_cnn.md) must
be used.

In most cases, [`DoOcrMultiClassCnn`](do_ocr_multi_class_cnn.md) should be preferred over
`DoOcrSingleClassCnn`, since [`DoOcrMultiClassCnn`](do_ocr_multi_class_cnn.md) is
typically faster than a loop with `DoOcrSingleClassCnn`.
Furthermore, the resulting confidences can be interpreted as
probabilities. They indicate the uncertainty of a character's classification
result. The operator `DoOcrSingleClassCnn` has to be used if the
nth-best class has to be examined explicitly for n greater than one.

A string of the number
$'\setminus032'$ (alternatively
displayed as $'\setminus0x1A'$) in
*`classVal`* signifies that the region has been classified as rejection
class.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region `→` [HRegion](HRegion.md)

Character to be recognized.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the character.

**`OCRHandle`** (input_control)  ocr_cnn `→` [HOCRCnn](HOCRCnn.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the OCR classifier.

**`num`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Number of best classes to determine.

Default:
1

Suggested values:
1, 2, 3, 4, 5

**`classVal`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Result of classifying the character with the
CNN.

**`confidence`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Confidence(s) of the class(es) of the character.

## Example (HDevelop)

```
read_image(Image, 'bottle2')
OffsetRow := 100
OffsetCol := 108
read_ocr_class_cnn('Universal_0-9_NoRej.occ', OCRHandle)
* Select each digit and use do_ocr_single_class_cnn to apply OCR
gen_rectangle1(ROI_Date, OffsetRow, OffsetCol, OffsetRow, OffsetCol)
for I := 1 to 6 by 1
  Offset := I % 2 * 10
  smallest_rectangle1(ROI_Date, Row1, Col1, Row2, Col2)
  gen_rectangle1(ROI_Date, OffsetRow, Offset + Col2, OffsetRow + 42, \
  Col2 + Offset + 31)
  do_ocr_single_class_cnn(ROI_Date, Image, OCRHandle, 1, Class, Confidence)
endfor
```

## Result

If the parameters are valid, the operator
`DoOcrSingleClassCnn` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadOcrClassCnn`

## Alternatives

`DoOcrMultiClassCnn`

## Module

OCR/OCV
