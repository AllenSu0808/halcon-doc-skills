# DeserializeTextureInspectionModel (Operator)

## Name

`DeserializeTextureInspectionModel` — Deserialize a serialized texture inspection model.

## Signature

`static void HOperatorSet.DeserializeTextureInspectionModel(HTuple serializedItemHandle, out HTuple textureInspectionModel)`

`void HTextureInspectionModel.DeserializeTextureInspectionModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeTextureInspectionModel` deserializes a texture
inspection model, that was serialized
by [`SerializeTextureInspectionModel`](serialize_texture_inspection_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized texture inspection model is
defined by the handle *`serializedItemHandle`*. The deserialized values
are stored in an automatically created texture inspection model with the
handle *`textureInspectionModel`*.

For an explanation of the concept of the texture inspection
see the introduction of chapter [Inspection / Texture Inspection](toc_inspection_texture.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- textureInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`textureInspectionModel`** (output_control, state is modified)  texture_inspection_model `→` [HTextureInspectionModel](HTextureInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the texture inspection model.

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
`DeserializeTextureInspectionModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeTextureInspectionModel`

## Possible Successors

`ApplyTextureInspectionModel`

## See also

`CreateTextureInspectionModel`,
`WriteTextureInspectionModel`,
`SerializeTextureInspectionModel`

## Module

Matching
