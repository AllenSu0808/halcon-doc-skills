# serialize_texture_inspection_model (Operator)

## Name

`serialize_texture_inspection_model` — Serialize a texture inspection model.

## Signature

`def serialize_texture_inspection_model(texture_inspection_model: HHandle) -> HHandle`

## Description

`serialize_texture_inspection_model` serializes a texture inspection
model (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization).
The texture inspection model is defined by the handle
*`texture_inspection_model`*. The serialized texture inspection model is
returned by the handle *`serialized_item_handle`* and can be deserialized
by [`deserialize_texture_inspection_model`](deserialize_texture_inspection_model.md).

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`texture_inspection_model`** (input_control)  texture_inspection_model `→` HHandle

Handle of the texture inspection model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Example (HDevelop)

```
* Create texture inspection model
create_texture_inspection_model ('basic', TextureInspectionModel)
* Set parameters
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gen_result_handle', 'true')
* Make this short example fast:
set_texture_inspection_model_param (TextureInspectionModel, \
                                    'gmm_em_max_iter', 1)
* Read and add training images
read_image (TrainImage, 'carpet/carpet_01')
add_texture_inspection_model_image (TrainImage, TextureInspectionModel, \
                                    Indices)
* Train the model
train_texture_inspection_model (TextureInspectionModel)
* Serialize texture inspection model
serialize_texture_inspection_model (TextureInspectionModel, \
                                    SerializedItemHandle)
* Deserialize in Model
deserialize_texture_inspection_model (SerializedItemHandle, \
                                      TextureInspectionModelSerialized)
* Read and apply a test image
read_image (TestImage, 'carpet/carpet_02')
apply_texture_inspection_model (TestImage, DefectCandidates, \
                                TextureInspectionModelSerialized, \
                                TextureInspectionResultID)
```

## Result

If the parameters are valid, the operator
`serialize_texture_inspection_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`train_texture_inspection_model`

## Possible Successors

`clear_texture_inspection_model`,
`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_texture_inspection_model`

## See also

`create_texture_inspection_model`,
`read_texture_inspection_model`,
`deserialize_texture_inspection_model`

## Module

Matching
