## Anomaly Detection and Global Context Anomaly Detection

List of Operators ↓

This chapter explains how to use anomaly detection and Global Context Anomaly
Detection based on deep learning.

With those two methods we want to detect whether or not an image
contains anomalies.
An anomaly means something deviating from the norm, something unknown.

An anomaly detection or Global Context Anomaly Detection model learns common
features of images without anomalies.
The trained model will infer, how likely an input image contains
only learned features or if the image contains something
different. Latter one is interpreted as an anomaly.
This inference result is returned as a gray value image. The pixel values
therein indicate how likely the corresponding pixels in the input
image pixels show an anomaly.

We differentiate between two model types that can be used:

- **Anomaly Detection** —

  With anomaly detection (model type *`"anomaly_detection"`*)
  structural anomalies are targeted, thus any feature that was not learned
  during training.
  This can, e.g., include scratches, cracks or contamination.

  ![figure](../assets/cbbe47a0fbc2cee6.svg)

  A possible example for anomaly detection:
  Every pixel of the input image gets assigned a value that indicates how
  likely the pixel is to be an anomaly.
  The worm is not part of the worm-free apples the model has seen during
  training and therefore its pixels get a much higher score.
- **Global Context Anomaly Detection** —

  Global Context Anomaly Detection (model type
  *`"gc_anomaly_detection"`*) comprises two tasks:

  - **Detecting structural anomalies**

    As described for anomaly detection above, structural anomalies primarily
    include unknown features, like scratches, cracks or contamination.
  - **Detecting logical anomalies**

    Logical anomalies are detected if constraints regarding the image content
    are violated. This can, e.g., include a wrong number or wrong position of
    objects in an image.

  ![figure](../assets/e9966ed89e3aad7c.svg)

  A possible example for Global Context Anomaly Detection:
  Every pixel of the input image gets assigned
  a value that indicates how likely the pixel is to be an anomaly.
  Thereby two different types of anomalies can be detected, structural
  and logical ones.
  Structural anomaly: One apple contains a worm, which differs from the apples
  the model has seen during training.
  Logical anomaly: One apple is sorted among lemons. Although the apple
  itself is intact, the logical constraint is violated, as the model
  has only seen images with correctly sorted fruit during training.

  The Global Context Anomaly Detection model consists of two subnetworks.
  The model can be reduced to one of the subnetworks, in order to improve
  the runtime and memory consumption. This is recommended if a single
  subnetwork performs well enough. See the parameter
  *`"gc_anomaly_networks"`* in [`GetDlModelParam`](get_dl_model_param.md)
  for details. After setting
  *`"gc_anomaly_networks"`*, the model needs to be evaluated again,
  since this parameter can change the Global Context Anomaly Detection
  performance significantly.

  - **Local subnetwork**

    This subnetwork is used to detect anomalies that affect the image on a
    smaller, local scale. It is designed to detect structural anomalies but
    can find logical anomalies as well. Thus, if an anomaly can be
    recognized by analyzing single patches of an image, it is detected by the
    local component of the model. See the description of the parameter
    *`"patch_size"`* in [`GetDlModelParam`](get_dl_model_param.md) for information on
    how to define the local scale of this subnetwork.
  - **Global subnetwork**

    This subnetwork is used to detect anomalies that affect the image on a
    large, or global scale. It is designed to detect logical anomalies but
    can find structural anomalies as well.
    Thus, if you need to see most or all of the image
    to recognize an anomaly, it is detected by the
    global component of the model.

  ![figure](../assets/a1c2183e9ed2e84b.svg)

  Training image of an exemplary task. Apples and lemons are intact,
  sorted correctly, and tagged with the correct sticker.

  |  |  |
  | --- | --- |
  | ![figure](../assets/244d960ee89b153b.svg) | ![figure](../assets/f796f425aaa65e7d.svg) |
  | ( 1) | ( 2) |
  | ![figure](../assets/7541087b7e4f3614.svg) | ![figure](../assets/6c819eef759b1b03.svg) |
  | ( 3) | ( 4) |

  Some anomalies that can be detected with Global Context Anomaly Detection:
  (1) Logical anomaly, most likely detected by the local subnetwork (wrong sticker).
  (2) Structural anomaly, most likely detected by local subnetwork (wormy apple).
  (3) Logical anomaly, most likely detected by global subnetwork (wrong sorting).
  (4) Logical anomaly, most likely detected by global subnetwork (missing apples).

### General Workflow

In this paragraph, we describe the general workflow for an anomaly
detection or Global Context Anomaly Detection task based on deep learning.

- **Preprocess the data** —

  This part is about how to preprocess your data.

  1. The information content of your dataset needs to be converted.
     This is done by the procedure

     - `read_dl_dataset_anomaly`.

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

     In case of custom preprocessing, this procedure offers guidance on
     the implementation.

     To use this procedure, specify the preprocessing parameters as, e.g.,
     the image size.
     Store all the parameter with their values in a dictionary
     `DLPreprocessParam`, for which you can use the procedure

     - `create_dl_preprocess_param`.

     We recommend to save this dictionary `DLPreprocessParam` in
     order to have access to the preprocessing parameter values later
     during the inference phase.
- **Training of the model** —

  This part explains how to train a model.

  1. Set the training parameters and store them in the dictionary
     `TrainParam`.
     This can be done using the procedure

     - `create_dl_train_param`.
  2. Train the model. This can be done using the procedure

     - `train_dl_model`.

     The procedure

     - adapts models of type *`"gc_anomaly_detection"`* to the
       image statistics of the dataset calling the procedure
       `normalize_dl_gc_anomaly_features`,
     - calls the corresponding training operator
       [`TrainDlModelAnomalyDataset`](train_dl_model_anomaly_dataset.md) (*`"anomaly_detection"`*)
       or [`TrainDlModelBatch`](train_dl_model_batch.md) (*`"gc_anomaly_detection"`*),
       respectively.

     The procedure expects:

     - the model handle `DLModelHandle`
     - the dictionary `DLDataset` containing the data
       information
     - the dictionary `TrainParam` containing the training
       parameters
  3. Normalize the network. This step is only necessary when using a
     Global Context Anomaly Detection model. The anomaly scores need to be
     normalized by applying the procedure

     - `normalize_dl_gc_anomaly_scores`.

     This needs to be done in order to get reasonable results when applying
     a threshold on the anomaly scores later (see section
     “Specific Parameters” below).
- **Evaluation of the trained model** —

  In this part, we evaluate the trained model.

  1. Set the model parameters which may influence the evaluation.
  2. The evaluation can be done conveniently using the procedure

     - `evaluate_dl_model`.

     This procedure expects a dictionary `GenParam` with the
     evaluation parameters.
  3. The dictionary `EvaluationResult` holds the desired
     evaluation measures.
- **Inference on new images** —

  This part covers the application of an anomaly detection or
  Global Context Anomaly Detection model.
  For a trained model, perform the following steps:

  1. Request the requirements the model imposes on the images using
     the operator

     - [`GetDlModelParam`](get_dl_model_param.md)

     or the procedure

     - `create_dl_preprocess_param_from_model`.
  2. Set the model parameter described in the section “Model
     Parameters” below, using the operator

     - [`SetDlModelParam`](set_dl_model_param.md).
  3. Generate a data dictionary `DLSample` for each image.
     This can be done using the procedure

     - `gen_dl_samples_from_images`.
  4. Every image has to be preprocessed the same way as for the
     training. For this, you can use the procedure

     - `preprocess_dl_samples`.

     When you saved the dictionary `DLPreprocessParam` during
     the preprocessing step, you can directly use it as input to specify
     all parameter values.
  5. Apply the model using the operator

     - [`ApplyDlModel`](apply_dl_model.md).
  6. Retrieve the results from the dictionary `DLResult`.

### Data

We distinguish between data used for training, evaluation, and inference
on new images.

As a basic concept, the model handles data by dictionaries, meaning it
receives the input data from a dictionary `DLSample` and returns
a dictionary `DLResult` and `DLTrainResult`, respectively.
More information on the data handling can be found in the chapter
[Deep Learning / Model](toc_deeplearning_model.md).

- **Classes** —

  In anomaly detection and Global Context Anomaly Detection there are exactly
  two classes:

  - *`"ok"`*, meaning without anomaly, class ID *0*.
  - *`"nok"`*, meaning with anomaly, class ID *1*
    (on pixel values with an ID >*0*, see the subsection
    “Data for evaluation” below).

  These classes apply to the whole image as well as single pixels.
- **Data for training** —

  This dataset consists only of images without anomalies and the
  corresponding information.
  They have to be provided in a way the model can process them.
  Concerning the image requirements, find more information in the section
  “Images” below.

  The training data is used to train a model for your specific task.
  With the aid of this data the model can learn which features the
  images without anomalies have in common.
- **Data for evaluation** —

  This dataset should include images without anomalies but it can also
  contain images with anomalies.
  Every image within this set needs a ground truth label `image_label`
  specifying the class of the image (see the section above).
  This indicates if the image shows an anomaly (*`"nok"`*)
  or not (*`"ok"`*).

  Evaluating the model performance on finding anomalies can visually
  also be done on pixel level if an image `anomaly_file_name` is
  included in the `DLSample` dictionary.
  In this image `anomaly_file_name` every pixel indicates the
  class ID, thus if the corresponding pixel in the input image shows an
  anomaly (pixel value > *0*) or not (pixel value equal to *0*).

  |  |  |
  | --- | --- |
  | ![figure](../assets/15973046a4ced96c.svg) | ![figure](../assets/1facb0e72359d209.svg) |
  | ( 1) | ( 2) |

  Scheme of `anomaly_file_name`.
  For visibility, gray values are used to represent numbers.
  (1) Input image.
  (2) The corresponding `anomaly_file_name` providing the
  class annotations,
  *0*: *`"ok"`* (white and light gray),
  *2*: *`"nok"`* (dark gray).
- **Images** —

  The model poses requirements on the images, such as the dimensions,
  the gray value range, and the type.
  The specific values depend on the model itself. See the documentation
  of [`ReadDlModel`](read_dl_model.md) for the specific values of different models.
  For a read model they can be queried with [`GetDlModelParam`](get_dl_model_param.md).
  In order to fulfill these requirements, you may have to preprocess your
  images.
  Standard preprocessing of an entire sample, including the
  image, is implemented in `preprocess_dl_samples`.
  In case of custom preprocessing these procedure offers guidance on the
  implementation.
- **Model output** —

  The training output differs depending on the used model type:

  - Anomaly detection:
    As training output, the operator [`TrainDlModelAnomalyDataset`](train_dl_model_anomaly_dataset.md)
    will return a dictionary `DLTrainResult` with the best obtained
    error received during training and the epoch in which this error was
    achieved.
  - Global Context Anomaly Detection:
    As training output, the operator [`TrainDlModelBatch`](train_dl_model_batch.md)
    will return a dictionary `DLTrainResult` with
    the current value of the total loss as well as values for all other
    losses included in your model.

  As inference and evaluation output, the model will return a dictionary
  `DLResult` for every sample. For anomaly detection and
  Global Context Anomaly Detection, this dictionary includes the
  following extra entries:

  - `anomaly_score`: A score indicating how likely the entire
    image is to contain an anomaly.
    This score is based on the pixel scores given in
    `anomaly_image`.

    For Global Context Anomaly Detection, depending on the used subnetworks,
    the anomaly score can also be calculated by the local
    (`anomaly_score_local`) and the global
    (`anomaly_score_global`) subnetwork only. The
    `anomaly_score` is by default equal to the maximum of
    `anomaly_image`. The parameter `anomalyScoreTolerance`
    can be used to ignore a fraction of outliers in the
    `anomaly_image` when calculating the `anomaly_score`.
  - `anomaly_image`:
    An image, where the value of each pixel indicates how likely its
    corresponding pixel in the input image shows an anomaly
    (see the illustration below).
    For anomaly detection the values are
    $\in[0,1]$, whereas there are no constraints
    for Global Context Anomaly Detection.
    Depending on the used subnetworks, when using
    Global Context Anomaly Detection, an anomaly image can also be
    calculated by the local
    (`anomaly_image_local`) or the global
    (`anomaly_image_global`) subnetwork only.

  |  |  |
  | --- | --- |
  | ![figure](../assets/0f6e2f7b8e6d0fb3.svg) | ![figure](../assets/0fe79a0c941d8a0a.svg) |
  | ( 1) | ( 2) |

  Scheme of `anomaly_image`.
  For visualization purpose, gray values are used to represent numbers.
  (1) The `anomaly_file_name` providing the
  class annotations,
  *0*: *`"ok"`* (white and light gray),
  *2*: *`"nok"`* (dark gray)
  (2) The corresponding `anomaly_image`.

### Specific Parameters

For an anomaly detection or Global Context Anomaly Detection model,
the model parameters as well as the hyperparameters are set using
[`SetDlModelParam`](set_dl_model_param.md).
The model parameters are explained in more detail in
[`GetDlModelParam`](get_dl_model_param.md).
As the training for an anomaly detection model is done utilizing the full
dataset at once and not batch-wise, certain parameters as e.g.,
*`"batch_size_multiplier"`* have no influence.

The model returns scores but classifies neither pixel nor image as showing an
anomaly or not.
For this classification, thresholds need to be given, setting the minimum
score for a pixel or image to be regarded as anomalous.
You can estimate possible thresholds using the procedure
`compute_dl_anomaly_thresholds`.
Applying these thresholds can be done with the procedure
`threshold_dl_anomaly_results`.
As results the procedure adds the following (threshold depending) entries
into the dictionary `DLResult` of a sample:

- **`anomaly_class`** —

  The predicted class of the entire image (for the given threshold).
  For Global Context Anomaly Detection, depending on the used subnetworks,
  the anomaly class can also be calculated by the local
  (`anomaly_class_local`) and the global
  (`anomaly_class_global`) subnetwork only.
- **`anomaly_class_id`** —

  ID of the predicted class of the entire image (for the given threshold).
  For Global Context Anomaly Detection, depending on the used subnetworks,
  the anomaly class ID can also be calculated by the local
  (`anomaly_class_id_local`) and the global
  (`anomaly_class_id_global`) subnetwork only.
- **`anomaly_region`** —

  Region consisting of all the pixels that are regarded as showing an anomaly
  (for the given threshold, see the illustration below).
  For Global Context Anomaly Detection, depending on the used subnetworks,
  the anomaly region can also be calculated by the local
  (`anomaly_region_local`) and the global
  (`anomaly_region_global`) subnetwork only.

  |  |  |
  | --- | --- |
  | ![figure](../assets/c1adaa677446fb22.svg) | ![figure](../assets/b31c32de48daae59.svg) |
  | ( 1) | ( 2) |

  Scheme of `anomaly_region`.
  For visualization purpose, gray values are used to represent numbers.
  (1) The `anomaly_image` with the obtained pixel scores.
  (2) The corresponding `anomaly_region`.

### Domain Handling During Inference

A restriction of the search area can be done by reducing the domain of
the input images (e.g., [`ReduceDomain`](reduce_domain.md)). The way
`preprocess_dl_samples` handles the domain is set using the
preprocessing parameter `'domain_handling'`. The parameter
`'domain_handling'` should be used in a way that only essential
information is passed on to the network for inference. For instance, use
`'keep_domain'` to exclude unwanted anomalies in the background
when computing the anomaly score and image.

The following images show how an input image with reduced domain
is inferred after the preprocessing step depending on the set
`'domain_handling'`.

![figure](../assets/d4b75f885e218d46.svg)

Input image for inference with domain (blue).

|  |  |
| --- | --- |
| ![figure](../assets/f7c65172f41b1648.svg) | ![figure](../assets/01b9e89652e7a58f.svg) |
| ( 1) | ( 2) |

(1) `anomaly_image` after inference with `'full_domain'`
(result: *`"nok"`*),
(2) `anomaly_image` after inference with `'keep_domain'`
(result: *`"ok"`*).

---

#### List of Operators

- [`TrainDlModelAnomalyDataset`](train_dl_model_anomaly_dataset.md) — Train a deep learning model for anomaly detection.
