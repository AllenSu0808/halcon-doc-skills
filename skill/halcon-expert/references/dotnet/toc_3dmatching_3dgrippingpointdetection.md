## 3D Gripping Point Detection

List of Sections ↓

This chapter explains how to use 3D Gripping Point Detection.

3D Gripping Point Detection is used to find suitable gripping points on
the surface of arbitrary objects in a 3D scene.
The results can be used to target the gripping points with a robot arm and
pick up the objects using vacuum grippers with suction cups.

![figure](../assets/d8d79043efcd1583.svg)

A possible example for a 3D Gripping Point Detection application:
A 3D scene (e.g., an RGB image and XYZ-images) is analyzed and possible
gripping points are suggested.

HALCON provides a pretrained model which is ready for inference
without an additional training step. To finetune the model for a specific
task, it is possible to retrain it on a custom application domain.
3D Gripping Point Detection also works
on objects that were not seen in training.
Thus, there is no need to provide a 3D model of the objects that are to be
targeted. 3D Gripping Point Detection can also cope with scenes containing
various different objects at once, scenes with partly occluded objects,
and with scenes containing cluttered 3D data.

The general inference workflow as well as the retraining are described in the
following sections.

### General Inference Workflow

This paragraph describes how to determine a suitable gripping
point on arbitrary object surfaces using a 3D Gripping Point Detection model.
An application scenario can be seen in the HDevelop example
`3d_gripping_point_detection_workflow.hdev`.

1. Read the pretrained 3D Gripping Point Detection model by using

   - [`ReadDlModel`](read_dl_model.md).
2. Set the model parameter regarding, e.g.,
   the used devices or image dimensions using

   - [`SetDlModelParam`](set_dl_model_param.md).
3. Generate a data dictionary `DLSample` for each 3D scene.
   This can be done using the procedure

   - `gen_dl_samples_3d_gripping_point_detection`,

   which can cope with different kinds of 3D data. For further information
   on the data requirements see the section “Data” below.
4. Preprocessing of the data before the inference.
   For this, you can use the procedure

   - `preprocess_dl_samples`.

   The required preprocessing parameters can be generated from
   the model with

   - `create_dl_preprocess_param_from_model`

   or set manually using

   - `create_dl_preprocess_param`.

   Note that the preprocessing of the data has significant impact
   on the inference. See the section “3D scenes” below
   for further details.
5. Apply the model using the operator

   - [`ApplyDlModel`](apply_dl_model.md).
6. Perform a post-processing step on the resulting `DLResult`
   to retrieve gripping points for your scene using the procedure

   - `gen_dl_3d_gripping_points_and_poses`.
7. Visualize the 2D and 3D results using the procedure

   - `dev_display_dl_data` or
   - `dev_display_dl_3d_data`, respectively.

### Training and Evaluation of the Model

This paragraph describes how the 3D Gripping Point Detection model can be
retrained and evaluated using custom data.
An application scenario can be seen in the HDevelop example
`3d_gripping_point_detection_training_workflow.hdev`.

- **Preprocess the data** —

  This part is about how to preprocess your data.

  1. The information content of your dataset needs to be converted.
     This is done by the procedure

     - `read_dl_dataset_3d_gripping_point_detection`.

     It creates a dictionary `DLDataset` which serves as
     a database and stores all necessary information about your data.
     For more information about the data and the way it is transferred, see
     the section “Data” below and the chapter
     [Deep Learning / Model](toc_deeplearning_model.md).
  2. Split the dataset represented by the dictionary
     `DLDataset`. This can be done using the procedure

     - `split_dl_dataset`.
  3. The network imposes several requirements on the
     images. These requirements (for example the image
     size and gray value range) can be retrieved with

     - [`GetDlModelParam`](get_dl_model_param.md).

     For this you need to read the model first by using

     - [`ReadDlModel`](read_dl_model.md).
  4. Now you can preprocess your dataset.
     For this, you can use the procedure

     - `preprocess_dl_dataset`.

     To use this procedure, specify the preprocessing parameters as, e.g.,
     the image size.
     Store all the parameter with their values in a dictionary
     `DLPreprocessParam`, for which you can use the procedure

     - `create_dl_preprocess_param_from_model`.

     We recommend to save this dictionary `DLPreprocessParam` in
     order to have access to the preprocessing parameter values later
     during the inference phase.
- **Training of the model** —

  This part explains the finetuning of the 3D Gripping Point Detection model
  by retraining it.

  1. Set the training parameters and store them in the dictionary
     `TrainParam`.
     This can be done using the procedure

     - `create_dl_train_param`.
  2. Train the model. This can be done using the procedure

     - `train_dl_model`.

     The procedure expects:

     - the model handle `DLModelHandle`,
     - the dictionary `DLDataset` containing the data
       information,
     - the dictionary `TrainParam` containing the training
       parameters.
- **Evaluation of the retrained model** —

  In this part, we evaluate the 3D Gripping Point Detection model.

  1. Set the model parameters which may influence the evaluation.
  2. The evaluation can be done conveniently using the procedure

     - `evaluate_dl_model`.

     This procedure expects a dictionary `GenParam` with the
     evaluation parameters.
  3. The dictionary `EvaluationResult` holds the evaluation
     measures. To get a clue on how the retrained model performed
     against the pretrained model you can compare their evaluation values.
     To understand the different evaluation measures, see section
     “Evaluation Measures for 3D Gripping Point Detection Results”.

### Data

This section gives information on the data that needs to be provided
for the model inference or training and evaluation of a
3D Gripping Point Detection model.

As a basic concept, the model handles data by dictionaries, meaning it
receives the input data from a dictionary `DLSample` and returns
a dictionary `DLResult`.
More information on the data handling can be found in the chapter
[Deep Learning / Model](toc_deeplearning_model.md).

- **3D scenes** —

  3D Gripping Point Detection processes 3D scenes, which consist of regular
  2D images and depth information.

  In order to adapt these 3D data to the network input requirements, a
  preprocessing step is necessary for the inference. See the section
  “Specific Preprocessing Parameters” below for information on certain
  preprocessing parameters.
  It is recommended to use a high resolution 3D sensor, in order to ensure
  the necessary data quality.
  The following data are needed:

  - **2D image** —
    - RGB image, or
    - intensity (gray value) image

    ![figure](../assets/9cc021f3b8efc1c7.svg)

    Intensity image.
  - **Depth information** —
    - X-image (values need to increase from left to right)
    - Y-image (values need to increase from top to bottom)
    - Z-image (values need to increase from points close to the sensor to
      far points; this is for example the case if the data is given in the
      camera coordinate system)

    |  |  |  |
    | --- | --- | --- |
    | ![figure](../assets/1aa6e6c7467b80de.svg) | ![figure](../assets/ba240024cdc5b6d0.svg) | ![figure](../assets/aae397a5ab4f7fa3.svg) |
    | ( 1) | ( 2) | ( 3) |

    (1) X-image,
    (2) Y-image,
    (3) Z-image.
  - **Normals (optional)** —
    - 2D mappings (3-channel image)

    ![figure](../assets/2a396c218a24e168.svg)

    Normals image.

    Providing normal images improves the runtime, as this avoids the need
    for their computation.

  In order to restrict the search area, the domain of the RGB/intensity image
  can be reduced. For details, see the section
  “Specific Preprocessing Parameters” below.
  Note that the domain of the XYZ-images and the (optional) normals images
  need to be identical. Furthermore, for all input data, only valid pixels
  may be part of the used domain.
- **Data for Training and Evaluation** —

  The training data is used to train and evaluate a network specifically
  for your application.

  The dataset needed for this consists of 3D scenes and corresponding
  information on possible gripping surfaces given as segmentation images.
  They have to be provided in a way the model can process them.
  Concerning the 3D scene requirements, find more information in the
  section “3D scenes” above.

  How the data has to be formatted in HALCON for a DL model is explained
  in the chapter [Deep Learning / Model](toc_deeplearning_model.md).
  In short, a dictionary `DLDataset` serves as a database for
  the information needed by the training and evaluation procedures.

  The data for `DLDataset` can be read using
  `read_dl_dataset_3d_gripping_point_detection`. See the reference of
  `read_dl_dataset_3d_gripping_point_detection` for information on
  the required contents of a 3D Gripping Point Detection `DLDataset`.

  Along with 3D scenes, segmentation images need to be provided, which
  function as the ground truth.
  The segmentation images contain two gray values that denote every pixel in
  the scene to be either a valid gripping point or not.
  You can label your data using the MVTec Deep Learning Tool, available
  from the MVTec website.

  |  |  |
  | --- | --- |
  | ![figure](../assets/2ee1f56b567c24e8.svg) | ![figure](../assets/485384c552cb3c09.svg) |
  | ( 1) | ( 2) |

  (1) Labeling of an intensity image.
  (2) Segmentation image, denoting gripping points (gray).

  Make sure that the whole labeled area provides robust gripping
  points for the robot.
  Consider the following aspects when labeling your data:

  - Gripping points need to be on a surface that can be accessed by the
    robot arm without being obstructed.
  - Gripping points need to be on a surface that the robot arm can grip
    with its suction cup. Therefore, consider the object's material, shape,
    and surface tilt with regard to the ground plane.
  - Take the size of the robots suction cup into account.
  - Take the strength of the suction cup into account.
  - Tend to label gripping points near the object's center of mass
    (especially for potentially heavier items).
  - Gripping points should not be at an object's border.
  - Gripping points should not be at the border of visible object regions.
- **Model output** —

  As inference output, the model will return a dictionary `DLResult`
  for every sample. This dictionary includes the following entries:

  - `'gripping_map'`: Binary image, indicating for each pixel of
    the scene whether the model predicted a gripping point
    (pixel value = *1.0*) or not (*0.0*).
  - `'gripping_confidence'`: Image, containing raw, uncalibrated
    confidence values for every point in the scene.

### Evaluation Measures for 3D Gripping Point Detection Results

For 3D Gripping Point Detection, the following evaluation measures are
supported in HALCON:

- **`mean_pro`** —

  Mean overlap of all ground truth regions
  labeled as gripping class with the predictions (Per-Region Overlap).
  See the paper referenced below for a detailed description of this
  evaluation measure.
- **`mean_precision`** —

  Mean pixel-level precision of the predictions
  for the gripping class. The precision is the proportion of true
  positives to all positives (true (TP) and false (FP) ones).
  $$precision = \frac{TP}{TP + FP}$$ ![figure](../assets/4c6c4d9dc413e523.svg)
- **`mean_iou`** —

  Intersection over union (IoU) between the ground
  truth pixels and the predicted pixels of the gripping class. See
  [Deep Learning / Semantic Segmentation and Edge Extraction](toc_deeplearning_semanticsegmentation.md) for a detailed description of
  this evaluation measure.
- **`gripping_point_precision`** —

  Proportion of true positives
  to all positives (true and false ones).

  For this measure, a true positive is a correctly predicted gripping point,
  meaning the predicted point is located within a ground truth region.
  However, only one gripping point per region is considered a true positive,
  additional predictions in the same region are considered false positives.
- **`gripping_point_recall`** —

  The recall is the proportion
  of the number of correctly predicted gripping points to the number of
  all ground truth regions of the gripping class.

  $$\mathrm{recall} = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}$$ ![figure](../assets/bb83c2ccf4c45ed3.svg)
- **`gripping_point_f_score`** —

  To represent precision and recall
  with a single number, we provide the F-score, the harmonic mean of
  precision and recall.

  $$F\-score = 2 * \frac{precision * recall}{precision + recall}$$ ![figure](../assets/a73c1679c1ebd8ac.svg)

### Postprocessing

The model results `DLResult` can be postprocessed with
`gen_dl_3d_gripping_points_and_poses` in order to generate
gripping points.
Furthermore, this procedure can be parameterized in order to reject
small gripping regions using `min_area_size`,
or serve as a template to define custom selection criteria.

The procedure adds the following entry to the dictionary
`DLResult`:

- `'gripping_points'`: Tuple of dictionaries containing
  information on suitable gripping points in a scene:

  - `'region'`: Connected region of potential gripping points.
    The determined gripping point lies inside this
    region.
  - `'row'`: Row coordinate of the gripping point in the
    preprocessed RGB/intensity image.
  - `'column'`: Column coordinate of the gripping point in the
    preprocessed RGB/intensity image.
  - `'pose'`: 3D pose of the gripping point (relative to
    the coordinate system of the XYZ-images, i.e.,
    of the camera) which can be used
    by the robot.

### Specific Preprocessing Parameters

In the preprocessing step, along with the data, preprocessing parameters
need to be passed to `preprocess_dl_samples`.
Two pairs of those preprocessing parameters have
particularly significant impact:

- `'image_width'`, `'image_height'`:
  Determine the image dimensions of the images to be inferred.

  With larger image dimensions and thus a better resolution,
  smaller gripping surfaces can be detected. However, the runtime
  and memory consumption of the application increases.
- `'min_z'`, `'max_z'`:
  Determine the allowed distance from the camera for 3D points based on
  the Z-image.

  These parameters can therefore help to reduce erroneous outliers and
  therefore increase the application robustness.

A restriction of the search area can be done by reducing the domain of
the input images (using [`ReduceDomain`](reduce_domain.md)). The way
`preprocess_dl_samples` handles the domain is set using the
preprocessing parameter `'domain_handling'`. The parameter
`'domain_handling'` should be used in a way that only essential
information is passed on to the network for inference.
The following images show how an input image with reduced domain
is passed on after the preprocessing step depending on the set
`'domain_handling'`.

|  |  |  |  |
| --- | --- | --- | --- |
| ![figure](../assets/073e3224261a74a4.svg) | ![figure](../assets/7e203ebf7fc30d4a.svg) | ![figure](../assets/ef024feb909c9aa6.svg) | ![figure](../assets/d0e63c2d57fa28f0.svg) |
| ( 1) | ( 2) | ( 3) | ( 4) |

(1) Input image with reduced domain (red),
(2) image for `'full_domain'`,
(3) image for `'keep_domain'`,
(4) image for `'crop_domain'`.

### References

Bergmann, P., Batzner, K., Fauser, M., Sattlegger, D. and Steger, C., 2021.
The MVTec anomaly detection dataset: a comprehensive real-world dataset for
unsupervised anomaly detection. International Journal of Computer Vision,
129(4), pp.1038-1059.

---

#### List of Sections
