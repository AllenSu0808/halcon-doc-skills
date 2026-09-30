## Model

List of Operators ↓

This chapter explains the general concept of the deep learning (DL) model
in HALCON and the data handling.

By concept, a deep learning model in HALCON is an internal representation of
a deep neural network. Each deep neural network has an architecture defining
its function, i.e., the tasks it can be used for.
There can be several possible network architectures for one functionality.
Currently, networks for the following functionalities
are implemented in HALCON as model:

- 3D Gripping Point Detection,
  see [3D Matching / 3D Gripping Point Detection](toc_3dmatching_3dgrippingpointdetection.md).
- Advanced object detection see
  [Deep Learning / Advanced Object Detection](toc_deeplearning_objectdetection.md).
- Anomaly detection and Global Context Anomaly Detection,
  see [Deep Learning / Anomaly Detection and Global Context Anomaly Detection](toc_deeplearning_anomalydetection.md).
- Classification, see [Deep Learning / Classification](toc_deeplearning_classification.md).
- Deep 3D Matching,
  see [3D Matching / Deep 3D Matching](toc_3dmatching_deep3dmatching.md).
- Deep OCR, see [OCR / Deep OCR](toc_ocr_deepocr.md).
- Instance segmentation and object detection see
  [Deep Learning / Instance Segmentation and Object Detection](toc_deeplearning_instancesegmentation.md).
- Multi-Label Classification, see [Deep Learning / Multi-Label Classification](toc_deeplearning_multilabelclassification.md).
- Semantic segmentation and edge extraction, see
  [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md).

Each functionality is identified by its unique model type.
For the implemented methods you can find further information about the
specific workflow, data requirements, and validation measures in the
corresponding chapters.
Information to deep learning in general are given in the chapter
[Deep Learning](toc_deeplearning.md).

In this chapter you find the information, which data a DL model needs
and returns as well as how this data is transferred.

### Data

Deep Learning applications have different types of data to be distinguished.
Roughly spoken these are: The raw images with possible annotations, data
preprocessed in a way suitable for the model, and output data.

Before the different types of data and the entries of the specific
dictionaries are explained, we will have a look how the data is connected.
Thereby, symbols and colors refer to the schematic overviews given below.

In brief, the data structure for training or evaluation starts with the raw
images and their ground truth annotations (gray frames).
With the read data the following dictionaries are created:
A dictionary `DLDataset` (red), which serves as database and
refers to a specific dictionary (yellow) for every input image.
The dictionary `DLSample` (orange) contains the data for a sample
in the way the network can process it.
A batch of `DLSample` is handed to the model in
`dlsample_batch`.
For evaluation, `dlresult_batch` is returned, a tuple of
dictionaries `DLResult` (dark blue), one for every sample.
They are needed to obtain the evaluation results `EvaluationResult`.
For training, the training results (e.g., loss values) are returned in the
dictionary `DLTrainResult` (light blue).
The most important steps concerning modifying or creating a dictionary:

- reading the raw data (symbol: paper with arrow)
- preprocessing the data (symbol: cogs)
- training (symbol: transparent brain in an arc)
- evaluation of the model (symbol: graph)
- evaluation of a sample (symbol: magnifying glass)

![figure](../assets/bb8f326a7a697a8b.svg)

Schematic overview of the data structure during training and evaluation.

For inference no annotations are needed.
Thus, the data structure starts with the raw images (gray frames).
The dictionary `DLSample` (orange) contains the data for a sample
in the way the network can process it.
The results for a sample are returned in a dictionary `DLResult`
(dark blue).
The most important steps concerning modifying or creating a dictionary:

- reading the raw data (symbol: paper with arrow)
- preprocessing the data (symbol: cogs)
- inference (symbol: brain in a circle)
- evaluation of a sample (symbol: magnifying glass)

![figure](../assets/97228b43e401a783.svg)

Schematic overview of the data connection during inference.

In order for the model to process the data, the data needs to follow certain
conventions about what is needed and how it is given to the model.
As visible from the figures above, in HALCON the data is transferred using
dictionaries.

In the following we explain the involved dictionaries, how they can be
created, and their entries.
Thereby, we group them according to the main step of a deep learning
application they are created in and whether they serve as input or output
data. The following abbreviations mark for which methods the entry applies:

- 'Any': any method
- '3D-GPD': 3D Gripping Point Detection
- '3D-PE': Deep 3D Matching pose estimation component
- 'AD': anomaly detection
- 'CL': classification
- 'MLC': multi-label classification
- 'OCR-D': Deep OCR detection component
- 'OCR-R': Deep OCR recognition component
- 'GC-AD': Global Context Anomaly Detection
- 'OD': object detection

  In case the entry is only applicable for a certain
  *`"instance_type"`*,
  the specification 'r1': *`"rectangle1"`*,
  'r2': *`"rectangle2"`* is added.

  For entries only applicable for instance segmentation the
  specification 'is' is added.
- 'SE': semantic segmentation

The entries only applicable for certain methods are described more
extensively in the corresponding chapter.

- **Training and evaluation input data** —

  The dataset consists of images and corresponding information.
  They have to be provided in a way the model can process them.
  Concerning the image requirements, find more information in the
  section “Images” below.

  The information about the images and the dataset is
  represented in a dictionary `DLDataset`, which serves as a database.
  More precisely, it stores the general information about the dataset and the
  dictionaries of the individual samples collected under the key
  `samples`.
  When the actual image data is needed, a dictionary `dlsample`
  is created (or read if it already exists) for each image required.
  The relation of these dictionaries is illustrated in the figure below.

  ![figure](../assets/2e6396dfcb2f38e2.svg)

  Schematic illustration of the different dataset dictionaries used for
  training and evaluation.
  For visibility purpose only few entries are registered and
  `BatchSize` is set to three.
  In this example we have $n$ samples. Thereof three samples are
  chosen randomly: i,j, and k.
  The corresponding dictionaries `dlsample` are created and joined
  in the tuple `dlsample_batch`.

  In the following we look at these dictionaries.
  - **`DLDataset`** —

    The dictionary `DLDataset` serves as a database.
    It stores general information about the dataset and collects the
    dictionaries of the individual samples.
    Thereby iconic data is not included in `DLDataset` but the paths
    to the respective images.
    The dictionary `DLDataset` is used by the training and evaluation
    procedures.
    It is not necessary for the model, but we highly recommend to create it.
    Its necessary entries are described below.
    This dictionary is either created directly when labeling your
    data using the MVTec Deep Learning Tool or it is created by one of the
    following method-specific procedures:

    - `read_dl_dataset_3d_gripping_point_detection`
      (3D Gripping Point Detection)
    - `read_dl_dataset_anomaly` (anomaly detection,
      Global Context Anomaly Detection)
    - `read_dl_dataset_classification` (classification)
    - `read_dl_dataset_ocr_detection` (Deep OCR - detection component)
    - `read_dl_dataset_ocr_recognition` (Deep OCR - recognition component)
    - `read_dl_dataset_from_coco` (object detection with
      *`"instance_type"`* = *`"rectangle1"`*)
    - `read_dl_dataset_segmentation` (semantic segmentation).

    Please see the respective procedure documentation for the requirements on
    the data in order to use these procedures.
    In case you create `DLDataset` in an other way, it has to
    contain at least the entries not marked with a number in the description
    below.
    During the preprocessing of your dataset the respective procedures include
    the further entries of the dictionary `DLDataset`.

    Depending on the model type, this dictionary can have the following
    entries:

    - **`image_dir`: Any** —

      Common base path to all images.

      *format:* string
    - **`dlsample_dir`: Any [1]** —

      Common base path of all sample files (if present).

      *format:* string
    - **`class_names`: Any except OCR-R** —

      Names of all classes that are to be distinguished.

      *format:* tuple of strings
    - **`class_ids`: Any except OCR-R** —

      IDs of all classes that are to be distinguished (range: 0-65534).

      *format:* tuple of integers
    - **`preprocess_param`: Any [1]** —

      All parameter values used during preprocessing.

      *format:* dictionary
    - **`samples`: Any** —

      Collection of sample descriptions.

      *format:* tuple of dictionaries
    - **`normals_dir`: 3D-GPD** —

      Optional. Common base path of all normals images.

      *format:* string
    - **`xyz_dir`: 3D-GPD** —

      Common base path of all XYZ-images.

      *format:* string
    - **`orig_3d_model`: 3D-PE** —

      3D CAD object model.

      *format:* string
    - **`anomaly_dir`: AD, GC-AD** —

      Common base path of all anomaly regions
      (regions indicating anomalies in the image).

      *format:* string
    - **`class_weights`: CL, SE [1]** —

      Weights of the different classes.

      *format:* tuple of reals
    - **`segmentation_dir`: SE, 3D-GPD** —

      Common base path of all segmentation images.

      *format:* string

    This dictionary is directly created when labeling your data using the
    MVTec Deep Learning Tool. It is also created by the
    procedures mentioned above for reading in your data.
    The entries marked with [1] are added by the preprocessing
    procedures.
  - **`samples`** —

    The `DLDataset` key `samples` gets a tuple of
    dictionaries as value, one for each sample in the dataset.
    These dictionaries contain the information concerning an individual
    sample of the dataset.
    Depending on the model type, this dictionary can have the following
    entries:

    - **`image_file_name`: Any** —

      File name of the image and its path relative to `image_dir`.

      *format:* string
    - **`image_id`: Any** —

      Unique image ID (encoding format: UINT8).

      *format:* integer
    - **`split`: Any [2]** —

      Specifies the assigned split subset
      (*`"train"`*,*`"validation"`*,*`"test"`*).

      *format:* string
    - **`dlsample_file_name`: Any [3]** —

      File name of the corresponding dictionary `dlsample` and its
      path relative to `dlsample_dir`.

      *format:* string
    - **`normals_file_name`: 3D-GPD** —

      Optional. File name of the normals image and its path relative to
      `normals_dir`.

      *format:* string
    - **`segmentation_file_name`: 3D-GPD, SE** —

      File name of the ground truth segmentation image and its path relative
      to `segmentation_dir`.

      *format:* string
    - **`xyz_file_name`: 3D-GPD** —

      File name of the XYZ-image and its path relative to `xyz_dir`.

      *format:* string
    - **`anomaly_file_name`: AD, GC-AD** —

      Optional. Path to region files with ground truth annotations
      (relative to `anomaly_dir`).

      *format:* string
    - **`anomaly_label`: AD, GC-AD** —

      Ground truth anomaly label on image level
      (in the form of `class_names`).

      *format:* string
    - **`image_label_id`: CL** —

      Ground truth label for the image (in the form of `class_ids`).

      *format:* tuple of integers
    - **`image_label_ids`: MLC** —

      Ground truth labels for the image (in the form of `class_ids`).

      *format:* tuple of integers
    - **`image_id_origin`: OCR-R** —

      ID of the original image the sample was extracted from.

      *format:* integer
    - **`word`: OCR-D, OCR-R** —

      Ground truth word.

      *format:* string
    - **`bbox_label_id`: OD, OCR-D** —

      Ground truth labels for the bounding boxes
      (in the form of `class_ids`).

      *format:* tuple of integers
    - **`bbox_row1`: OD:r1 [4]** —

      Ground truth bounding boxes: upper left corner, row coordinate.

      *format:* tuple of reals
    - **`bbox_col1`: OD:r1 [4]** —

      Ground truth bounding boxes: upper left corner, column coordinate.

      *format:* tuple of reals
    - **`bbox_row2`: OD:r1 [4]** —

      Ground truth bounding boxes: lower right corner, row coordinate.

      *format:* tuple of reals
    - **`bbox_col2`: OD:r1 [4]** —

      Ground truth bounding boxes: lower right corner, column coordinate.

      *format:* tuple of reals
    - **`coco_raw_annotations`: OD:r1** —

      Optional. It contains for every `bbox_label_id` within this
      image a dictionary with all raw COCO annotation information.

      *format:* tuple of dictionaries
    - **`bbox_row`: OCR-D, OCR-R, OD:r2 [4]** —

      Ground truth bounding boxes: center point, row coordinate.

      *format:* tuple of reals
    - **`bbox_col`: OCR-D, OCR-R, OD:r2 [4]** —

      Ground truth bounding boxes: center point, column coordinate.

      *format:* tuple of reals
    - **`bbox_phi`: OCR-D, OCR-R, OD:r2 [4]** —

      Ground truth bounding boxes: angle phi.

      *format:* tuple of reals
    - **`bbox_length1`: OCR-D, OCR-R, OD:r2 [4]** —

      Ground truth bounding boxes: half length of edge 1.

      *format:* tuple of reals
    - **`bbox_length2`: OCR-D, OCR-R, OD:r2 [4]** —

      Ground truth bounding boxes: half length of edge 2.

      *format:* tuple of reals
    - **`visibility`: OD** —

      Fractional visibility of bounding boxes.

      *format:* tuple of reals
    - **`mask`: 3D-PE, OD:is** —

      Ground truth mask marking the instance regions.

      *format:* tuple of regions
    - **`camera_parameter`: 3D-PE** —

      Camera parameter for the image.

      *format:* tuple of HALCON camera parameter
    - **`pose`: 3D-PE** —

      Poses of the objects in each bounding box.

      *format:* tuple of HALCON poses

    These dictionaries are part of `DLDataset` and thus they are
    created concurrently.
    An exception are the entries with a mark in the table,
    [2]: the procedure `split_dl_dataset` adds `split`,
    [3]: the procedure `preprocess_dl_samples` adds
    `dlsample_file_name`.
    [4]: Used coordinates: Pixel centered, subpixel accurate coordinates.
  - **`dlsample`** —

    The dictionary `dlsample` serves as input for the model.
    For a batch, they are handed over as the entries of the tuple
    `dlsample_batch` for [`apply_dl_model`](apply_dl_model.md) or
    [`train_dl_model_batch`](train_dl_model_batch.md).
    They are created out of `DLDataset` for every sample by the
    procedure `gen_dl_samples` followed by
    `preprocess_dl_samples`.
    Note, `preprocess_dl_samples` will update the corresponding
    `dlsample` dictionary.
    If preprocessing is done using the standard procedure
    `preprocess_dl_dataset`, the preprocessed samples are stored on
    the file system. Afterwards they need to be retrieved with the
    procedure `read_dl_samples`.

    `dlsample` contains the preprocessed image and, in case of training
    and evaluation, all ground truth annotations.
    Depending on the model type, it can have the following entries:

    - **`anomaly_ground_truth`: AD, GC-AD** —

      Anomaly image or region, read from `anomaly_file_name`.

      *format:* image or region
    - **`anomaly_label`: AD, GC-AD** —

      Ground truth anomaly label on image level
      (in the form of `class_names`).

      *format:* string
    - **`anomaly_label_id`: AD, GC-AD** —

      Ground truth anomaly label ID on image level
      (in the form of `class_ids`).

      *format:* integer
    - **`bbox_label_id`: OD** —

      Ground truth labels for the image part within the bounding box
      (in the form of `class_ids`).

      *format:* tuple of integers
    - **`bbox_row1`: OD:r1 [4]** —

      Ground truth bounding boxes: upper left corner, row coordinate.

      *format:* tuple of reals
    - **`bbox_col1`: OD:r1 [4]** —

      Ground truth bounding boxes: upper left corner, column coordinate.

      *format:* tuple of reals
    - **`bbox_row2`: OD:r1 [4]** —

      Ground truth bounding boxes: lower right corner, row coordinate.

      *format:* tuple of reals
    - **`bbox_col2`: OD:r1 [4]** —

      Ground truth bounding boxes: lower right corner, column coordinate.

      *format:* tuple of reals
    - **`bbox_row`: OCR-D, OD:r2 [4]** —

      Ground truth bounding boxes: center point, row coordinate.

      *format:* tuple of reals
    - **`bbox_col`: OCR-D, OD:r2 [4]** —

      Ground truth bounding boxes: center point, column coordinate.

      *format:* tuple of reals
    - **`bbox_phi`: OCR-D, OD:r2 [4]** —

      Ground truth bounding boxes: angle phi.

      *format:* tuple of reals
    - **`bbox_length1`: OCR-D, OD:r2 [4]** —

      Ground truth bounding boxes: half length of edge 1.

      *format:* tuple of reals
    - **`bbox_length2`: OCR-D, OD:r2 [4]** —

      Ground truth bounding boxes: half length of edge 2.

      *format:* tuple of reals
    - **`image`: Any** —

      Input image.

      *format:* image
    - **`image_label_id`: CL** —

      Ground truth label for the image (in the form of `class_ids`).

      *format:* integer
    - **`image_label_ids`: MLC** —

      Ground truth labels for the image (in the form of `class_ids`).

      *format:* tuple of integers
    - **`mask`: 3D-PE, OD:is** —

      Ground truth mask marking the instance regions.

      *format:* tuple of regions
    - **`normals`: 3D-GPD** —

      2D mappings (3-channel image)

      *format:* image
    - **`segmentation_image`: SE, 3D-GPD** —

      Image with the ground truth segmentations,
      read from `segmentation_file_name`.

      *format:* image
    - **`weight_image`: SE [5]** —

      Image with the pixel weights.

      *format:* image
    - **`target_orientation`: OCR-D** —

      Orientation target image for the word orientation.

      *format:* image
    - **`target_text`: OCR-D** —

      Text target image for the character detection.

      *format:* image
    - **`target_link`: OCR-D** —

      Link target image for the connection of detected character centers to a
      connected word.

      *format:* image
    - **`target_weight_orientation`: OCR-D** —

      Weight with respect to `target_orientation`.

      *format:* image
    - **`target_weight_link`: OCR-D** —

      Weight with respect to `target_link`.

      *format:* image
    - **`target_weight_text`: OCR-D** —

      Weight with respect to `target_text`.

      *format:* image
    - **`word`: OCR-D, OCR-R** —

      Ground truth word.

      *format:* string
    - **`x`: 3D-GPD** —

      X-image (values need to increase from left to right).

      *format:* image
    - **`y`: 3D-GPD** —

      Y-image (values need to increase from top to bottom).

      *format:* image
    - **`z`: 3D-GPD** —

      Z-image (values need to increase from points close to the sensor to
      far points; this is for example the case if the data is given in the
      camera coordinate system).

      *format:* image
    - **`camera_parameter`: 3D-PE** —

      Camera parameter for the image.

      *format:* tuple of HALCON camera parameter
    - **`pose`: 3D-PE** —

      Poses of the objects in each bounding box.

      *format:* tuple of HALCON poses
    - **`width_orig`: 3D-PE** —

      Original width of the bounding boxes.

      *format:* tuple of reals
    - **`height_orig`: 3D-PE** —

      Original height of the bounding boxes.

      *format:* tuple of reals

    These dictionaries are created by the procedure
    `gen_dl_samples` followed by `preprocess_dl_samples`.
    An exception is the entry marked in the table above, [5]: created
    by the procedure `gen_dl_segmentation_weights`.
    [4]: Used coordinates: Pixel centered, subpixel accurate coordinates.
- **Inference input data** —

  The inference input data consists of a single `dlsample` dictionary
  or a tuple of such. In contrast to training and evaluation, only
  the following keys are used:

  - **`image`: Any** —

    Input image

    *format:* image
  - **`normals`: 3D-GPD** —

    2D mappings (3-channel image).

    *format:* image
  - **`x`: 3D-GPD** —

    X-image (values need to increase from left to right).

    *format:* image
  - **`y`: 3D-GPD** —

    Y-image (values need to increase from top to bottom).

    *format:* image
  - **`z`: 3D-GPD** —

    Z-image (values need to increase from points close to the sensor to
    far points; this is for example the case if the data is given in the
    camera coordinate system).

    *format:* image

  Concerning the image requirements, find more information in the
  subsection “Images” below.

  For the inference, such a dictionary containing only the image data can be
  created using the procedure `gen_dl_samples_from_images` or
  `gen_dl_samples_3d_gripping_point_detection` (only for 3D Gripping
  Point Detection). These dictionaries can be passed one at a time or within
  a tuple `dlsample_batch`.
- **Training output data** —

  The training output data is given in the dictionary `dltrain_result`.
  Its entries depend on the model and thus on the operator used
  (for further information see the documentation of the corresponding
  operator):

  - **3D-GPD, 3D-PE, CL, MLC, OCR-D, OCR-R, GC-AD, OD, SE:** —

    The operator [`train_dl_model_batch`](train_dl_model_batch.md) returns

    - `total_loss`
    - possible further losses included in your model
  - **AD:** —

    The operator [`train_dl_model_anomaly_dataset`](train_dl_model_anomaly_dataset.md) returns

    - `final_error`
    - `final_epoch`
- **Inference and evaluation output data** —

  As output from the operator [`apply_dl_model`](apply_dl_model.md), the model will return
  a dictionary `dlresult` for each sample.
  An illustration is given in the figure below.
  The evaluation is based on these results and the annotations.
  Evaluation results are stored in the dictionary
  `EvaluationResult`.

  |  |  |
  | --- | --- |
  | ![figure](../assets/13e9c13530424c81.svg) | ![figure](../assets/69047da723ff40b9.svg) |
  | ( 1) | ( 2) |

  Schematic illustration of the dictionaries serving as model input:
  (1) Evaluation: `dlsample` includes the image
  as well as information about the image and its content.
  This data serves as basis for the evaluation.
  For visibility purpose `BatchSize` is set to three
  (containing the randomly chosen samples i,j,and k, see above)
  and only few entries are registered.
  (2) Inference: `dlsample` contains only the image.
  These dictionaries can be passed one at a time or within a tuple.

  Note that for model of type 3D-PE, inference and evaluation are not performed
  as described above. Please refer to [3D Matching / Deep 3D Matching](toc_3dmatching_deep3dmatching.md)
  on how to use Deep 3D Matching inference.

  Depending on the model type, the dictionary `dlresult` can have
  the following entries:

  - **`gripping_confidence`: 3D-GPD** —

    Image, containing raw, uncalibrated
    confidence values for every point in the scene.

    *format:* image
  - **`gripping_map`: 3D-GPD** —

    Binary image, indicating for each pixel of
    the scene whether the model predicted a gripping point
    (pixel value = *1.0*) or not (*0.0*).

    *format:* image
  - **`anomaly_image`: AD, GC-AD** —

    Single channel image whose gray values are scores, indicating how
    likely the corresponding pixel in the input image belongs to an anomaly.

    *format:* image
  - **`anomaly_image_combined`: GC-AD** —

    Single channel image whose gray values are scores, indicating how
    likely the corresponding pixel in the input image belongs to an anomaly.
    Calculated by combining the *`"local"`* and *`"global"`*
    subnetworks of the model.

    *Format:* image
  - **`anomaly_image_global`: GC-AD** —

    Single channel image whose gray values are scores, indicating how
    likely the corresponding pixel in the input image belongs to an anomaly.
    Calculated by the *`"global"`* subnetwork of the model.

    *format:* image
  - **`anomaly_image_local`: GC-AD** —

    Single channel image whose gray values are scores, indicating how
    likely the corresponding pixel in the input image belongs to an anomaly.
    Calculated by the *`"local"`* subnetwork of the model.

    *format:* image
  - **`anomaly_score`: AD, GC-AD** —

    Anomaly score on image level calculated from `anomaly_image`.

    *format:* real
  - **`anomaly_score_local`: GC-AD** —

    Anomaly score on image level calculated from
    `anomaly_image_local`.

    *format:* real
  - **`anomaly_score_global`: GC-AD** —

    Anomaly score on image level calculated from
    `anomaly_image_global`.

    *format:* real
  - **`classification_class_ids`: CL** —

    Inferred class ids for the image sorted by confidence values.

    *format:* tuple of integers
  - **`classification_class_names`: CL** —

    Inferred class names for the image sorted by confidence values.

    *format:* tuple of strings
  - **`classification_confidences`: CL** —

    Confidence values of the image inference for each class.

    *format:* tuple of reals
  - **`class_ids`: MLC** —

    Inferred class ids for the image sorted by confidence values.

    *format:* tuple of integers
  - **`class_names`: MLC** —

    Inferred class names for the image sorted by confidence values.

    *format:* tuple of strings
  - **`confidences`: MLC** —

    Confidence values of the image inference for each class.

    *format:* tuple of reals
  - **`selected_class_ids`: MLC** —

    Class ids for the image selected by the confidence
    threshold(`min_confidence`).

    *format:* tuple of integers
  - **`selected_class_names`: MLC** —

    Class names for the image selected by the confidence
    threshold (`min_confidence`).

    *format:* tuple of strings
  - **`selected_confidences`: MLC** —

    Confidence values of the image selected by the confidence
    threshold for each class.

    *format:* tuple of reals
  - **`char_candidates`: OCR-R** —

    Candidates for each character of the word and their confidences.

    *format:* tuple of dictionaries
  - **`word`: OCR-R** —

    Recognized word.

    *format:* string
  - **`score_maps`: OCR-D** —

    Scores given as image with four channels:

    - Character score: Score for the character detection.
    - Link score: Score for the connection of detected character centers to
      a connected word.
    - Orientation 1: Sine component of the predicted word orientation.
    - Orientation 2: Cosine component of the predicted word orientation.

    *format:* image
  - **`words`: OCR-D** —

    Dictionary containing the following entries.
    Thereby, the entries are tuples with a value for every found word.

    - `row`: Localized word: Center point, row coordinate.
    - `col`: Localized word: Center point, column
      coordinate.
    - `phi`: Localized word: Angle phi.
    - `length1`: Localized word: Half length of edge 1.
    - `length2`: Localized word: Half length of edge 2.
    - `line_index`: Line index of localized word if
      *`"detection_sort_by_line"`* set to *`"true"`*.

    *format:* dictionary with tuples of reals and strings
  - **`word_boxes_on_image`: OCR-D** —

    Dictionary with the word
    localization on the coordinate system of the preprocessed images placed in
    `image`. The entries are tuples with a value for every found word.

    - `row`: Localized word: Center point, row coordinate.
    - `col`: Localized word: Center point, column
      coordinate.
    - `phi`: Localized word: Angle phi.
    - `length1`: Localized word: Half length of edge 1.
    - `length2`: Localized word: Half length of edge 2.

    *format:* dictionary with tuples of reals
  - **`word_boxes_on_score_maps`: OCR-D** —

    Dictionary with the word
    localization on the coordinate system of the score images placed in
    `score_maps`. The entries are the same as for
    `word_boxes_on_image` above.
    *format:* dictionary with tuples of reals
  - **`bbox_class_id`: OD** —

    Inferred class for the bounding box
    (in the form of `class_ids`).

    *format:* tuple of integers
  - **`bbox_class_name`: OD** —

    Name of the inferred class for the bounding box.

    *format:* tuple of strings
  - **`bbox_confidence`: OD** —

    Confidence value of the inference for the bounding box.

    *format:* tuple of reals
  - **`bbox_row1`: OD:r1 [6]** —

    Inferred bounding boxes: upper left corner, row coordinate.

    *format:* tuple of reals
  - **`bbox_col1`: OD:r1 [6]** —

    Inferred bounding boxes: upper left corner, column coordinate.

    *format:* tuple of reals
  - **`bbox_row2`: OD:r1 [6]** —

    Inferred bounding boxes: lower right corner, row coordinate.

    *format:* tuple of reals
  - **`bbox_col2`: OD:r1 [6]** —

    Inferred bounding boxes: lower right corner, row coordinate.

    *format:* tuple of reals
  - **`bbox_row`: OD:r2 [6]** —

    Inferred bounding boxes: center point, row coordinate.

    *format:* tuple of reals
  - **`bbox_col`: OD:r2 [6]** —

    Inferred bounding boxes: center point, column coordinate.

    *format:* tuple of reals
  - **`bbox_phi`: OD:r2 [6]** —

    Inferred bounding boxes: angle phi.

    *format:* tuple of reals
  - **`bbox_length1`: OD:r2 [6]** —

    Inferred bounding boxes: half length of edge 1.

    *format:* tuple of reals
  - **`bbox_length2`: OD:r2 [6]** —

    Inferred bounding boxes: half length of edge 2.

    *format:* tuple of reals
  - **`mask`: OD:is** —

    Inferred mask marking the instance regions.

    *format:* tuple of regions
  - **`mask_probs`: OD:is** —

    Image with the confidence values of the inferred mask.

    *format:* image
  - **`segmentation_image`: SE** —

    Image with the segmentation result.

    *format:* image
  - **`segmentation_confidence`: SE** —

    Image with the confidence values of the segmentation result.

    *format:* image

  [6]: Used coordinates: Pixel centered, subpixel accurate coordinates.

  For a further explanation to the output values we refer to the chapters
  of the respective method, e.g.,
  [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md).
- **Images** —

  Regardless of the application, the network poses requirements on the
  images. The specific values depend on the network itself and can be
  queried using [`get_dl_model_param`](get_dl_model_param.md).
  In order to fulfill these requirements, you may have to preprocess your
  images.
  Standard preprocessing of the entire dataset and therewith also the
  images is implemented in `preprocess_dl_samples`.
  In case of custom preprocessing this procedure offers guidance on the
  implementation.

---

#### List of Operators

- [`add_dl_pruning_batch`](add_dl_pruning_batch.md) — Calculate scores to prune a deep learning model.

- [`apply_dl_model`](apply_dl_model.md) — Apply a deep-learning-based network on a set of images for inference.

- [`clear_dl_model`](clear_dl_model.md) — Clear a deep learning model.

- [`create_dl_pruning`](create_dl_pruning.md) — Create a pruning data handle.

- [`deserialize_dl_model`](deserialize_dl_model.md) — Deserialize a deep learning model.

- [`gen_dl_model_heatmap`](gen_dl_model_heatmap.md) — Infer the sample and generate a heatmap.

- [`gen_dl_pruned_model`](gen_dl_pruned_model.md) — Prune a deep learning model.

- [`get_dl_model_param`](get_dl_model_param.md) — Return the parameters of a deep learning model.

- [`get_dl_pruning_param`](get_dl_pruning_param.md) — Get information from a pruning data handle.

- [`read_dl_model`](read_dl_model.md) — Read a deep learning model from a file.

- [`serialize_dl_model`](serialize_dl_model.md) — Serialize a deep learning model.

- [`set_dl_model_param`](set_dl_model_param.md) — Set the parameters of a deep learning model.

- [`set_dl_pruning_param`](set_dl_pruning_param.md) — Set parameter in a pruning data handle.

- [`train_dl_model_batch`](train_dl_model_batch.md) — Train a deep learning model.

- [`write_dl_model`](write_dl_model.md) — Write a deep learning model in a file.
