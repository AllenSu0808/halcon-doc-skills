# append_ocr_trainf (Operator)

## Name

`append_ocr_trainf` — Add characters to a training file.

## Signature

`def append_ocr_trainf(character: HObject, image: HObject, class_val: MaybeSequence[str], training_file: str) -> None`

## Description

The operator `append_ocr_trainf` serves to prepare the
training with the operator [`trainf_ocr_class_mlp`](trainf_ocr_class_mlp.md) or
[`trainf_ocr_class_svm`](trainf_ocr_class_svm.md). Hereby
regions, representing characters, including their gray values (region
and pixel) and the corresponding class name will be written into a
file. An arbitrary number of regions within one image is supported.
For each character (region) in *`character`* the corresponding
class name must be specified in *`class`*. The gray values are
passed via the parameter *`image`*. In
contrast to the operator [`write_ocr_trainf`](write_ocr_trainf.md) the
characters are appended to an existing file using the same training file
format as this file. If
the file does not exist, a new file is generated. In this case, the
file format can be chosen by the parameter
*"ocr_trainf_version"* of the operator [`set_system`](set_system.md). If no
file extension is specified in *`training_file`*, the extension '.trf'
is appended to the name.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`character`** (input_object)  region(-array) `→` HObject

Characters to be trained.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Gray values of the characters.

**`class`** (input_control)  string(-array) `→` MaybeSequence[str]

Class (name) of the characters.

**`training_file`** (input_control)  filename.write `→` str

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
`append_ocr_trainf` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception will be raised.

## Possible Predecessors

`threshold`,
`connection`,
`read_ocr_trainf`

## Possible Successors

`trainf_ocr_class_mlp`,
`trainf_ocr_class_svm`,
`write_ocr_trainf`

## Alternatives

`write_ocr_trainf`,
`write_ocr_trainf_image`

## Module

OCR/OCV
