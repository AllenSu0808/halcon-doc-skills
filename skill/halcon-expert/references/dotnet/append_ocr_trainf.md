# AppendOcrTrainf (Operator)

## Name

`AppendOcrTrainf` — Add characters to a training file.

## Signature

`static void HOperatorSet.AppendOcrTrainf(HObject character, HObject image, HTuple classVal, HTuple trainingFile)`

`void HRegion.AppendOcrTrainf(HImage image, HTuple classVal, string trainingFile)`

`void HRegion.AppendOcrTrainf(HImage image, string classVal, string trainingFile)`

## Description

The operator `AppendOcrTrainf` serves to prepare the
training with the operator [`TrainfOcrClassMlp`](trainf_ocr_class_mlp.md) or
[`TrainfOcrClassSvm`](trainf_ocr_class_svm.md). Hereby
regions, representing characters, including their gray values (region
and pixel) and the corresponding class name will be written into a
file. An arbitrary number of regions within one image is supported.
For each character (region) in *`character`* the corresponding
class name must be specified in *`classVal`*. The gray values are
passed via the parameter *`image`*. In
contrast to the operator [`WriteOcrTrainf`](write_ocr_trainf.md) the
characters are appended to an existing file using the same training file
format as this file. If
the file does not exist, a new file is generated. In this case, the
file format can be chosen by the parameter
*"ocr_trainf_version"* of the operator [`SetSystem`](set_system.md). If no
file extension is specified in *`trainingFile`*, the extension '.trf'
is appended to the name.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Characters to be trained.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Gray values of the characters.

**`classVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Class (name) of the characters.

**`trainingFile`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the training file.

Default:
"train_ocr"

File extension:
.`trf`, .`otr`

## Example (C)

```
char       name[128];
char       class[128];

read_image(&Image,"character.tiff");
binary_threshold(Image,&Dark, 'otsu', 'dark', &UsedThreshold);
connection(Dark,&Character);
count_obj(Character,&num);
create_tuple(&Class,num);
open_window(0,0,-1,-1,0,"","",&WindowHandle);
set_color(WindowHandle,"red");
for (i=0; i<num; i++) {
  select_obj(Character,&SingleCharacter,i);
  disp_region(SingleCharacter,WindowHandle);
  printf("class of character %d ?\n",i);
  scanf("%s\n",class);
  append_ocr_trainf(Character,Image,name,class);
}
```

## Result

If the parameters are correct, the operator
`AppendOcrTrainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`Threshold`,
`Connection`,
`ReadOcrTrainf`

## Possible Successors

`TrainfOcrClassMlp`,
`TrainfOcrClassSvm`,
`WriteOcrTrainf`

## Alternatives

`WriteOcrTrainf`,
`WriteOcrTrainfImage`

## Module

OCR/OCV
