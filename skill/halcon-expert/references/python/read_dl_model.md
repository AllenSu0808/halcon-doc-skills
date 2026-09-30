# read_dl_model (Operator)

## Name

`read_dl_model` — Read a deep learning model from a file.

## Signature

`def read_dl_model(file_name: str) -> HHandle`

## Description

The operator `read_dl_model` reads a deep learning model.
Such models have to be in the HALCON format or in the ONNX format
(see the reference below). Restrictions apply to the latter.
As a result, the handle *`dlmodel_handle`* is returned.

The model is loaded from the file *`file_name`*.
This file is thereby searched in the directory `$HALCONROOT/dl/`
as well as in the currently used directory.
The default HALCON file extension for deep learning networks is
`'.hdl'`.

Please note that the values of runtime specific parameters are not written
to file, see [`write_dl_model`](write_dl_model.md).
As a consequence, when reading a model, these parameters are initialized
with their default value, see [`get_dl_model_param`](get_dl_model_param.md).

Models that require a higher HALCON version (*"min_version"*) than
the one currently in use cannot be read. Before writing a model the
*"min_version"* can be checked with the operator [`get_dl_model_param`](get_dl_model_param.md).

For further explanations on deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

### Reading a Model provided by HALCON

HALCON provides pretrained neural networks for classification and
semantic segmentation. These neural networks are good starting points when
training a custom network. They have been pretrained on a large image dataset.
For anomaly detection, HALCON provides initial models.

- **Models for 3D Gripping Point Detection** —

  The following network is provided for 3D Gripping Point Detection:

  - ***"pretrained_dl_3d_gripping_point.hdl"*** —

    The network expects up to 5 images of type `real`:

    - —

      *"image"*: intensity (gray value) image
    - —

      *"x"*: X-image (values need to increase from left to right)
    - —

      *"y"*: Y-image (values need to increase from top to bottom)
    - —

      *"z"*: Z-image (values need to increase from points close to the sensor to
      far points; this is for example the case if the data is given in the
      camera coordinate system)
    - —

      *"normals"*: 2D mappings

    Additionally, the network requires certain image properties (for all input images
    mentioned above). The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values:

    - —

      *"image_width"*: 640
    - —

      *"image_height"*: 480

    The network architecture allows changes concerning the image dimensions.
- **Models for Anomaly Detection** —

  The following networks are provided for anomaly detection:

  - ***"initial_dl_anomaly_medium.hdl"*** —

    This neural network is designed to be memory and runtime efficient.

    The network expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values:

    - —

      *"image_width"*: 480
    - —

      *"image_height"*: 480
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -2
    - —

      *"image_range_max"*: 2

    The network architecture allows changes concerning the image dimensions,
    but the sizes *"image_width"* and *"image_height"* have to
    be multiples of 32 pixels, resulting in a minimum of 32 pixels.
  - ***"initial_dl_anomaly_large.hdl"*** —

    This neural network is assumed to be better suited for more complex
    anomaly detection tasks.
    This comes at the cost of being more time and memory demanding.

    The network expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values:

    - —

      *"image_width"*: 480
    - —

      *"image_height"*: 480
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -2
    - —

      *"image_range_max"*: 2

    The network architecture allows changes concerning the image dimensions,
    but the sizes *"image_width"* and *"image_height"* have to
    be multiples of 32 pixels, resulting in a minimum of 32 pixels.
- **Models for Global Context Anomaly Detection** —

  The following networks are provided for Global Context Anomaly Detection:

  - ***"pretrained_dl_anomaly_global_context.hdl"*** —

    The network expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values:

    - —

      *"image_width"*: 256
    - —

      *"image_height"*: 256
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0
- **Models for Classification** —

  The following pretrained neural networks are provided for
  classification and usable as backbones for detection:

  - ***"pretrained_dl_classifier_alexnet.hdl"*:** —

    This neural network is designed for simple classification tasks.
    It is characterized by its convolution kernels in the first
    convolution layers, which are larger than those in other networks with
    comparable classification performance
    (e.g., *"pretrained_dl_classifier_compact.hdl"*).
    This may be beneficial for feature extraction.

    This classifier expects the images to be of the type `real`.
    Additionally, the network is designed for certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 29 pixels.
    There is no maximum image size, but large image sizes will increase
    the memory demand and the runtime significantly.
    Changing the image size will reinitialize the weights of the fully
    connected layers and therefore makes a retraining necessary.

    Note that one can improve the runtime for this network
    by fusing the convolution and ReLU layers, see
    [`set_dl_model_param`](set_dl_model_param.md) and the parameter
    *"fuse_conv_relu"*.
  - ***"pretrained_dl_classifier_compact.hdl"*:** —

    This neural network is designed to be more memory and runtime
    efficient.

    The classifier expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    This network does not contain any fully connected layer.
    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 15 pixels.
  - ***"pretrained_dl_classifier_enhanced.hdl"*:** —

    This neural network has more hidden layers than
    *"pretrained_dl_classifier_compact.hdl"* and is therefore
    assumed to be better suited for more complex classification tasks.
    This comes at the cost of being more time and memory demanding.

    The classifier expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 47 pixels.
    There is no maximum image size, but large image sizes will increase
    the memory demand and the runtime significantly.
    Changing the image size will reinitialize the weights of the fully
    connected layers and therefore makes a retraining necessary.
  - ***"pretrained_dl_classifier_mobilenet_v2.hdl"*:** —

    This classifier is a small and low-power model, for what reason it is more
    suitable for mobile and embedded vision applications.

    The classifier expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 32 pixels.
    There is no maximum image size, but large image sizes will increase
    the memory demand and the runtime significantly.

    On the GPU, the network architecture can benefit greatly from special
    optimizations, without which the network can be significantly slower.
  - ***"pretrained_dl_classifier_resnet18.hdl"*:** —

    As the neural network
    *"pretrained_dl_classifier_enhanced.hdl"*, this classifier is
    suited for more complex tasks.
    However, due to its special structure, it provides the advantage of making
    the training more stable and internally more robust. Compared to
    the neural network *"pretrained_dl_classifier_resnet50.hdl"*
    it is less complex and has faster inference times.

    The classifier expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 32 pixels.
    There is no maximum image size, but large image sizes will increase
    the memory demand and the runtime significantly.
    Despite the fully connected layer a change of the image size does
    not lead to a reinitialization of the weights.
  - ***"pretrained_dl_classifier_resnet50.hdl"*:** —

    As the neural network
    *"pretrained_dl_classifier_enhanced.hdl"*, this classifier is
    suited for more complex tasks.
    However, due to its special structure, it provides the advantage of making
    the training more stable and internally more robust.

    The classifier expects the images to be of the type `real`.
    Additionally, the network requires certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the classifier has been trained:

    - —

      *"image_width"*: 224
    - —

      *"image_height"*: 224
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image
    dimensions. *"image_width"* and *"image_height"*
    should not be less than 32 pixels.
    There is no maximum image size, but large image sizes will increase
    the memory demand and the runtime significantly.
    Despite the fully connected layer a change of the image size does
    not lead to a reinitialization of the weights.
- **Models for Advanced Object Detection** —

  The following pretrained neural networks are provided for
  advanced object detection:

  - ***"pretrained_dl_detection_rectangle1_small.hdl"*:** —
  - ***"pretrained_dl_detection_rectangle1_medium.hdl"*:** —
  - ***"pretrained_dl_detection_rectangle1_large.hdl"*:** —

  All provided models support multi-scale detection.
  The approach is characterized by feature extraction, multi-scale accumulation
  and anchor-free prediction.
  The models differ in the number of trainable parameters.
  Larger models better capture fine details in large objects.
  The small model prioritizes speed.

  The model expects the input images to be of the type `real`.
  Additionally, the network requires certain image properties.
  The corresponding values can be retrieved with
  [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values:

  - —

    *"image_width"*: 640
  - —

    *"image_height"*: 640
  - —

    *"image_num_channels"*: 3
  - —

    *"image_range_min"*: -127.0
  - —

    *"image_range_max"*: 128.0

  The network architecture allows changes concerning the image dimensions,
  but the sizes *"image_width"* and *"image_height"* have to
  be multiples of 32 pixels, resulting in a minimum of 32 pixels.
- **Models for Semantic Segmentation** —

  The following pretrained neural networks are provided for semantic
  segmentation:

  - ***"pretrained_dl_edge_extractor.hdl"*:** —

    This neural network is designed and pretrained for edge extraction.
    As a consequence this model is meant for two class problems
    with one class for edges and one for background.

    This network expects the images to be of the type `real`.
    Additionally, the network is designed for certain image properties.
    The corresponding values can be retrieved with
    [`get_dl_model_param`](get_dl_model_param.md). Here we list the default values with
    which the model has been trained:

    - —

      *"image_width"*: 512
    - —

      *"image_height"*: 512
    - —

      *"image_num_channels"*: 1
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0
    - —

      *"num_classes"*: 2

    The network architecture allows changes concerning the image dimensions,
    but the sizes *"image_width"* and *"image_height"* have to
    be multiples of 16 pixels, resulting in a minimum of 16 pixels.
  - ***"pretrained_dl_segmentation_compact.hdl"*:** —

    This neural network is designed to handle segmentation tasks with
    detailed structures and uses only few memory and is runtime efficient.

    The network architecture allows changes concerning the image dimensions,
    but requires a minimum *"image_width"* and
    *"image_height"* of 21 pixels.
  - ***"pretrained_dl_segmentation_enhanced.hdl"*:** —

    This neural network has more hidden layers than
    *"pretrained_dl_segmentation_compact.hdl"* and is therefore
    better suited for segmentation tasks including more complex scenes.

    The network architecture allows changes concerning the image dimensions,
    but requires a minimum *"image_width"* and
    *"image_height"* of 47 pixels.
- **Models for Deep OCR** —

  The following pretrained neural networks are provided for Deep OCR:

  - ***"pretrained_deep_ocr_detection.hdl"*:** —

    This neural network is the default pretrained detection component of a
    Deep OCR model, but can be retrained, too. It is designed to detect words
    in images.

    This network expects the images to be of the type `real`.
    Additionally, the network is designed for certain image properties. The
    corresponding values can be retrieved with [`get_dl_model_param`](get_dl_model_param.md).
    Here we list the default values with which the model has been trained:

    - —

      *"image_width"*: 1024
    - —

      *"image_height"*: 1024
    - —

      *"image_num_channels"*: 3
    - —

      *"image_range_min"*: -127.0
    - —

      *"image_range_max"*: 128.0

    The network architecture allows changes concerning the image dimensions
    *"image_width"* and *"image_height"*.
  - ***"pretrained_deep_ocr_detection_compact.hdl"*:** —

    This pretrained network is a compact alternative to the default text
    detection model *"pretrained_deep_ocr_detection.hdl"*.
    It is designed to be more memory and runtime efficient, but it can be less
    accurate than the default model.

    Regarding the input images and image dimensions, this network has the
    same requirements as the default model
    *"pretrained_deep_ocr_detection.hdl"*.
  - ***"pretrained_deep_ocr_recognition.hdl"*:** —

    This neural network is the default pretrained recognition component of a
    Deep OCR model, but can be retrained, too. It is designed to recognize
    words in images that are cropped to a single word.

    This network expects the images to be of the type `real`.
    Additionally, the network is designed for certain image properties. The
    corresponding values can be retrieved with [`get_dl_model_param`](get_dl_model_param.md).
    Here we list the default values with which the model has been trained:

    - —

      *"image_width"*: 120
    - —

      *"image_height"*: 32
    - —

      *"image_num_channels"*: 1
    - —

      *"image_range_min"*: -1.0
    - —

      *"image_range_max"*: 1.0

    The network architecture allows changes concerning the image width
    *"image_width"*. The image height *"image_height"* cannot
    be changed. The parameter *"image_width"* is very important: its
    value can be decreased or increased to adapt to the expected lengths of
    words, e.g., due to the average width per character. A bigger
    *"image_width"* will consume more time and memory resources. The
    image width *"image_width"* may be changed after training.
  - ***"pretrained_deep_ocr_recognition_compact.hdl"*:** —

    This pretrained network is a compact alternative to the default text
    recognition model *"pretrained_deep_ocr_recognition.hdl"*.
    It is designed to be more memory and runtime efficient, but it can be less
    accurate than the default model.

    Regarding the input images and image dimensions, this network has the
    same requirements as the default model
    *"pretrained_deep_ocr_recognition.hdl"*.

### Reading a Model in the ONNX Format

You can read in an ONNX model, but there are some points to consider.

- **Restrictions** —

  Reading in ONNX models with `read_dl_model`, some restrictions
  apply:

  - Only models up to ONNX operator set version (OpSetVersion) 13 are
    supported. For operators using a higher OpSetVersion, support is not
    guaranteed. For further limitations, please refer to the supported
    ONNX operations listing.
  - Only 32 bit floating point tensors are supported.
  - Only models ending with a SoftMax layer are automatically recognized
    as classifiers.
    All other models are considered as generic model, thus
    models of *"type"* = *"generic"*.
    [`set_dl_model_param`](set_dl_model_param.md) can be used to change the model type.
  - The input graph nodes (images) must be of shape dimension 4:
    Number of images (=*"batch_size"*), *"num_channels"*,
    *"image_height"*, and *"image_width"*.
- **Automatic transformations** —

  After reading an ONNX model with `read_dl_model`, some network
  transformations are executed automatically:

  - Every non-global pooling layer with a resulting
    feature map of size 1x1 is converted to a global pooling layer.
    Doing so enables resizable input images.
    For more information about pooling layer and possible modes of
    operation, see the `“Solution Guide on Classification”`.
  - Layer pairs consisting of a convolution layer without activation
    and a directly connected activation layer with ReLU activation are
    fused.
    In order to do so, the output of the convolution layer is only used
    as input for the activation layer.
    As a result a convolution layer with activation mode ReLU is obtained.
    For more information about layers and possible modes of operation,
    see the `“Solution Guide on Classification”`.
  - When reading split layers, each split is converted into slice layers.
    The conversion process creates corresponding slice layers that extract
    the exact subsections of data. This ensures that the original split
    functionality is preserved, even though it appears as separate slice
    operations instead of a single split layer.
  - Permutation layers are added before and after elementwise layers in
    case the ONNX elementwise node`s inputs have different dimensions,
    to enable broadcasting.
  - Permutation layers are added before and after softmax layers in
    case the ONNX softmax node`s axis attribute is not equal 1.
  - Slice layers that follow a shape layer are fused with it, if possible.
    This requires that the slice layer is the only consumer of the shape
    layer`s output and that its step size is 1.
    This improves performance and reduces memory consumption.
- **Supported operations** —

  ONNX models with the following operations can be read by
  `read_dl_model`:

  - **`'Abs'`:** —

    No restrictions.
  - **`'Acos'`:** —

    No restrictions.
  - **`'Add'`:** —

    No restrictions.
  - **`'ArgMax'`:** —

    The following restrictions apply:

    - attribute *"axis"*: The value must be *1*.
    - attribute *"keepdims"*: The value must be *1*.
    - attribute *"select_last_index"*: The value
      must be *0*.
  - **`'Asin'`:** —

    No restrictions.
  - **`'Atan'`:** —

    No restrictions.
  - **`'AveragePool'`:** —

    The following restrictions apply:

    - attribute *"count_include_pad"*: The value must be
      *0*.
  - **`'BatchNormalization'`:** —

    No restrictions.
  - **`'Ceil'`:** —

    No restrictions.
  - **`'Celu'`:** —

    No restrictions.
  - **`'Clip'`:** —

    The following restrictions apply:

    - attribute *"min"*: The value must be less or equal
      *"max"*.
    - attribute *"max"*: The value must be
      greater or equal *"min"* and less than maximum float number.
  - **`'Concat'`:** —

    No restrictions.
  - **`'Constant'`:** —

    The following restrictions apply:

    - attribute *"sparse_value"*: The attribute is not supported.
    - attribute *"value_floats"*: The attribute is not supported.
    - attribute *"value_ints"*: The attribute is not supported.
    - attribute *"value_string"*: The attribute is not supported.
    - attribute *"value_strings"*: The attribute is not supported.
  - **`'Conv'`:** —

    The following restrictions apply:

    - attribute *"pads"*: Padding values greater than
      or equal to kernel size are not supported.
  - **`'ConvTranspose'`:** —

    The following restrictions apply:

    - attribute *"dilations"*: Only the value *"(1, 1)"*
      (no dilations) is supported.
    - attribute *"group"*: Only the value *1* is supported
      (no grouped transposed convolution).
    - attribute *"kernel_shape"*: Only symmetric kernel shapes
      are supported.
    - attribute *"output_padding"*: See restrictions mentioned in
      [`create_dl_layer_transposed_convolution`](create_dl_layer_transposed_convolution.md).
    - attribute *"output_shape"*: The attribute is not supported.
    - attribute *"pads"*: Padding values greater than
      or equal to kernel size are not supported.
    - attribute *"strides"*: Only symmetric strides are supported.
  - **`'Cos'`:** —

    No restrictions.
  - **`'Cosh'`:** —

    No restrictions.
  - **`'DepthToSpace'`:** —

    The following restrictions apply:

    - attribute *"mode"*: The value must be *"CRD"*.
  - **`'Div'`:** —

    No restrictions.
  - **`'Dropout'`:** —

    No restrictions.
  - **`'Elu'`:** —

    No restrictions.
  - **`'Erf'`:** —

    No restrictions.
  - **`'Exp'`:** —

    No restrictions.
  - **`'Floor'`:** —

    No restrictions.
  - **`'Gather'`:** —

    The following restrictions apply:

    - input *"indices"*: Indices with rank greater than one are
      not supported.
  - **`'Gelu'`:** —

    No restrictions.
  - **`'Gemm'`:** —

    The following restrictions apply:

    - attribute *"alpha"*: The value must be *1*.
    - attribute *"beta"*: The value must be *1*.
    - attribute *"transA"*: The value must be
      *0*.
  - **`'GlobalAveragePool'`:** —

    No restrictions.
  - **`'GlobalMaxPool'`:** —

    The following restrictions apply:

    - attribute *"dilations"*: The value must be *1*.
  - **`'HardSigmoid'`:** —

    No restrictions.
  - **`'HardSwish'`:** —

    No restrictions.
  - **`'LeakyRelu'`:** —

    No restrictions.
  - **`'Log'`:** —

    No restrictions.
  - **`'LogSoftmax'`:** —

    The following restrictions apply:

    - attribute *"axis"*:

      - OpSetVersion < 13: The value must be *1* and the
        width and height of the input shape must be 1, or the value
        must be *3*.
      - OpSetVersion >= 13: No restrictions.
  - **`'LRN'`:** —

    No restrictions. Hint: Attribute *"size"*
    has no effect.
  - **`'MatMul'`:** —

    No restrictions.
  - **`'MaxPool'`:** —

    No restrictions.
  - **`'Mean'`:** —

    No restrictions.
  - **`'Mish'`:** —

    No restrictions.
  - **`'Mul'`:** —

    No restrictions.
  - **`'Neg'`:** —

    No restrictions.
  - **`'Pow'`:** —

    The exponent must be a scalar constant input
    or initializer.
  - **`'Reciprocal'`:** —

    No restrictions.
  - **`'ReduceL2'`:** —
    - attribute *"noop_with_empty_axes"*: The attribute is
      optional. The value must be *0*.
    - attribute *"keepdims"*: The attribute is optional.
      The value must be *1*.
    - attribute *"axes"*: The attribute is optional.
      If empty reduce all dimensions. In the new opset versions
      the attribute *"axes"* was moved to the inputs.
  - **`'ReduceMax'`:** —

    The following restrictions apply:

    - attribute *"axes"*: The value must be *1*.
    - attribute *"keepdims"*: The value must be *1*.
  - **`'ReduceSum'`:** —
    - attribute *"noop_with_empty_axes"*: The attribute is
      optional. The value must be *0*.
    - attribute *"keepdims"*: The attribute is optional.
      The value must be *1*.
    - attribute *"axes"*: The attribute is optional.
      If empty reduce all dimensions. In the new opset versions
      the attribute *"axes"* was moved to the inputs.
  - **`'Relu'`:** —

    No restrictions.
  - **`'Resize'`:** —

    The following restrictions apply:

    - attribute *"mode"*: Only the values *"linear"*,
      *"bilinear"* and *"nearest"* are supported.
    - attribute *"coordinate_transformation_mode"*: Only the values
      *"half_pixel"*, *"pytorch_half_pixel"*,
      *"align_corners"* and *"asymmetric"* are supported.
    - input tensor *"roi"*: If values are set they have no
      effect on the inference.
    - The attributes *"cubic_coeff_a"*, *"exclude_outside"*,
      *"extrapolation_value"*, or *"nearest_mode"* have no
      effect.
  - **`'Reshape'`:** —

    The following restrictions apply:

    - attribute *"allowzero"*: If the attribute is used its value
      must be *0*.
  - **`'Round'`:** —

    No restrictions.
  - **`'Sigmoid'`:** —

    No restrictions.
  - **`'Sin'`:** —

    No restrictions.
  - **`'Sinh'`:** —

    No restrictions.
  - **`'Slice'`:** —

    No restrictions.
  - **`'Softmax'`:** —

    The following restrictions apply:

    - attribute *"axis"*:

      - OpSetVersion < 13: The value must be *1* and the
        width and height of the input shape must be 1, or the value
        must be *3*.
      - OpSetVersion >= 13: No restrictions.
  - **`'Softplus'`:** —

    No restrictions.
  - **`'Softsign'`:** —

    No restrictions.
  - **`'Split'`:** —

    No restrictions.
  - **`'Sqrt'`:** —

    No restrictions.
  - **`'Sub'`:** —

    No restrictions.
  - **`'Sum'`:** —

    No restrictions.
  - **`'Swish'`:** —

    No restrictions.
  - **`'Tan'`:** —

    No restrictions.
  - **`'Tanh'`:** —

    No restrictions.
  - **`'ThresholdedRelu'`:** —

    No restrictions.
  - **`'Transpose'`:** —

    No restrictions.

  Moreover the ONNX `'metadata_props'` field is supported. It is written to
  the model parameter *"meta_data"*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Filename

Default:
"pretrained_dl_classifier_compact.hdl"

List of values:
"initial_dl_anomaly_large.hdl", "initial_dl_anomaly_medium.hdl", "pretrained_deep_ocr_detection.hdl", "pretrained_deep_ocr_detection_compact.hdl", "pretrained_deep_ocr_recognition.hdl", "pretrained_deep_ocr_recognition_compact.hdl", "pretrained_dl_3d_gripping_point.hdl", "pretrained_dl_anomaly_global_context.hdl", "pretrained_dl_classifier_alexnet.hdl", "pretrained_dl_classifier_compact.hdl", "pretrained_dl_classifier_enhanced.hdl", "pretrained_dl_classifier_mobilenet_v2.hdl", "pretrained_dl_classifier_mobilenet_v4_large.hdl", "pretrained_dl_classifier_mobilenet_v4_medium.hdl", "pretrained_dl_classifier_mobilenet_v4_small.hdl", "pretrained_dl_classifier_resnet18.hdl", "pretrained_dl_classifier_resnet50.hdl", "pretrained_dl_detection_rectangle1_large.hdl", "pretrained_dl_detection_rectangle1_medium.hdl", "pretrained_dl_detection_rectangle1_small.hdl", "pretrained_dl_edge_extractor.hdl", "pretrained_dl_segmentation_compact.hdl", "pretrained_dl_segmentation_enhanced.hdl"

File extension:
.`hdl`, .`onnx`

**`dlmodel_handle`** (output_control)  dl_model `→` HHandle

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `read_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`set_dl_model_param`,
`get_dl_model_param`,
`apply_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`

## Alternatives

`create_dl_model_detection`

## References

Open Neural Network Exchange (ONNX), https://onnx.ai/

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
