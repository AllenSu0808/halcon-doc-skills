## Deep OCR

List of Operators ↓

This chapter explains how to use deep-learning-based optical character
recognition (Deep OCR).

With Deep OCR we want to detect and/or recognize text in an image.
Deep OCR detects and recognizes connected characters, which will be
referred to as 'words' (in contrast to OCR methods which are used to
read single characters).

![figure](../assets/6b1036635175abe6.svg)

A possible example for deep-learning-based optical character recognition:
Words in an image are detected and recognized.

A Deep OCR model can contain two components, which are dedicated to
two distinct tasks, the detection, thus the localization of words, and the
recognition of words. By default, a model is created with both components,
but the model can also be limited to either task.

HALCON already provides pretrained components, which are suited for a
multitude of applications without additional training as
the model is trained on a varied dataset and can
therefore cope with many different fonts. Information on the
available character set and model parameters can be
retrieved using [`GetDeepOcrParam`](get_deep_ocr_param.md).
To further adjust the reading to a specific task, it is possible to retrain
the recognition or detection component separately on a given application
domain using deep learning operators.
Note that only one component can be retrained at a time.

![figure](../assets/9ccda945b12e793a.svg)

The detection can be fine-tuned for an application by retraining
the Deep OCR model with custom data.

![figure](../assets/a8a6b811566755e4.svg)

The recognition can be fine-tuned for an application by retraining
the Deep OCR model with custom data.

In HALCON the recognition component requires tight word crops around a word
in an image to read the contained text.
One way to obtain these tight crops is by applying the detection component,
which is trained to find the exact position of multiple word boxes in an image.
For images containing a single word on a large background, HALCON offers the
recognition alignment feature, that ensures that relevant text regions are
properly aligned for the recognition component.

![figure](../assets/8f763541c0467319.svg)

The recognition can be fine-tuned to support alignment for an application
by retraining the recognition component with custom data.
The pretrained alignment generalizes well on a large variety of font and
printing types and cannot be fine-tuned with custom data.

The general workflow as well as the retraining are described in the
following paragraphs.

### General Workflow for Deep OCR Inference

This paragraph describes the workflow how to localize and read words using
a Deep OCR model. An application scenario can be seen in the HDevelop
example `deep_ocr_workflow.hdev`.

- **Creation of the Deep OCR model** —

  Create a Deep OCR model containing either one or both of the two
  model components

  - `detection_model` and
  - `recognition_model`

  using the operator [`CreateDeepOcr`](create_deep_ocr.md).

  To use a retrained model component instead of the provided one,
  adjust the created model by setting the retrained model component as
  *`"recognition_model"`* or *`"detection_model"`* using
  [`SetDeepOcrParam`](set_deep_ocr_param.md).
- **Inference** —

  Model parameters regarding, e.g., the used devices, image dimensions,
  or minimum scores can be set using [`SetDeepOcrParam`](set_deep_ocr_param.md).

  The Deep OCR model is applied on your acquired images using
  [`ApplyDeepOcr`](apply_deep_ocr.md). The inference results depend on the used
  model components. See the operator reference of [`ApplyDeepOcr`](apply_deep_ocr.md)
  for details regarding which dictionary entries are computed for
  each model composite.

  The inference results can be retrieved from the dictionary
  `deepOCRResult`.
  Some procedures are provided in order to visualize results and score maps:

  - Show location and/or recognized word using
    `dev_display_deep_ocr_results`.
  - Show location (and, if inferred, recognized word) on preprocessed
    image using `dev_display_deep_ocr_results_preprocessed`
    (if the model contains `detection_model`).
  - Show score maps using `dev_display_deep_ocr_score_maps`
    (if the model contains `detection_model`).

### Training and Evaluation of the Model Components

This paragraph describes the retraining and evaluation of the recognition or
detection components of a Deep OCR model using custom data. See also the
HDevelop examples `deep_ocr_recognition_training_workflow.hdev` or
`deep_ocr_detection_training_workflow.hdev` for an application scenario.

- **Preprocess the data** —

  This part is about how to preprocess your data. See the section “Data”
  below for information on what data is to be provided at what stage of
  the Deep OCR workflow.

  1. The information that is to be obtained from the images of your
     training dataset needs to be transferred. This is done by the
     procedure

     - `read_dl_dataset_ocr_recognition` for the recognition
       component of a Deep OCR model.
     - `read_dl_dataset_ocr_detection` for the detection
       component of a Deep OCR model.

     It creates a dictionary `DLDataset` which serves as
     a database and stores all necessary information about your data.
     For more information about datasets, see the chapter
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

  This part explains how to train the recognition or detection component of a
  Deep OCR model.

  1. Set the training parameters and store them in the dictionary
     `TrainParam`.
     This can be done using the procedure

     - `create_dl_train_param`.
  2. Train the model. This can be done using the procedure

     - `train_dl_model`.

     The procedure expects:

     - the model handle `DLModelHandle`
     - the dictionary `DLDataset` containing the data
       information
     - the dictionary `TrainParam` containing the training
       parameters
- **Evaluation of the retrained model** —

  In this part, we evaluate the Deep OCR model.

  1. Set the model parameters which may influence the evaluation.
  2. The evaluation can be done conveniently using the procedure

     - `evaluate_dl_model`.

     This procedure expects a dictionary `GenParamEval` with the
     evaluation parameters.
  3. The dictionary `EvaluationResult` holds the evaluation
     measures. To get a clue on how the retrained model performed
     against the pretrained model you can compare their evaluation values.
     To understand the different evaluation measures, see section
     “Evaluation Measures for Deep OCR Results”.

  After a successful evaluation the retrained model can be used for
  inference (see section “General Workflow for Deep OCR Inference”
  above).

### Data

This section gives information on the data that needs to be provided in
different stages of the Deep OCR workflow.

We distinguish between data used for training and evaluation, consisting
of images with their information about the instances, and data for
inference, which are bare images.
How the data needs to be provided is explained in the according sections
below.

As a basic concept, the model handles data over dictionaries, meaning it
receives the input data over a dictionary `DLSample` and
returns a dictionary `DLResult` and `DLTrainResult`,
respectively. More information on the
data handling can be found in the chapter [Deep Learning / Model](toc_deeplearning_model.md).

- **Data for training and evaluation** —

  The dataset consists of images and corresponding information.
  They have to be provided in a way the model can process them.
  Concerning the image requirements, find more information in the
  section “Images” below.

  The training data is used to train and evaluate a network for your
  specific application.
  With the aid of this data the network can learn to
  detect or recognize text samples that resemble text that occurs during
  inference. The necessary information is given by providing the depicted
  word for each image.

  How the data has to be formatted in HALCON for a DL model is explained
  in the chapter [Deep Learning / Model](toc_deeplearning_model.md).
  In short, a dictionary `DLDataset` serves as a database for
  the information needed by the training and evaluation procedures.

  The data for `DLDataset` can be read using
  `read_dl_dataset_ocr_recognition` or
  `read_dl_dataset_ocr_detection` depending on which model type is used.

  - **Dataset based on images with word labels (for detection and
    recognition with alignment support)** —

    In this case, images with words that are labeled with rotated
    bounding boxes need to be provided. You can label your data
    using the MVTec Deep Learning Tool, available from the MVTec website.
    The dataset must be built as follows:

    - `'class_ids'`: class IDs
    - `'class_names'`: class names
      (Needs to contain the class 'word'. All other classes are ignored.)
    - `'image_dir'`: path to the image directory
    - `'samples'`: tuple of dictionaries, one for each sample

      - `'image_file_name'`: name of the image file
      - `'image_id'`: image ID
      - `'bbox_col'`: bounding box column coordinate
      - `'bbox_row'`: bounding box row coordinate
      - `'bbox_phi'`: bounding box angle
      - `'bbox_length1'`: first half edge length of the
        bounding box
      - `'bbox_length2'`: second half edge length of the
        bounding box
      - `'label_custom_data'`: list of dictionaries containing
        custom label data for each bounding box

        - `'text'` word to be read
  - **Dataset based on word crop images (only recognition without
    alignment support)** —

    In this case, only images that are cropped to a single word each are
    included in the dataset. The dataset must be built as follows:

    - `'image_dir'`: path to the image directory
    - `'samples'`: tuple of dictionaries, one for each sample

      - `'image_file_name'`: name of the image file
      - `'image_id'`: image ID
      - `'word'`: word to be read in the image

  The example program `deep_ocr_prelabel_dataset.hdev` can provide
  assistance by prelabeling your data.

  Your training data should cover the full range of characters that
  might occur during inference. If a character is not or only very rarely
  contained in the training dataset the model might not properly learn to
  recognize that character. To keep track of the character distribution
  within the dataset the procedure
  `gen_dl_dataset_ocr_recognition_statistics` is provided, which
  generates statistics on how often every single character is contained in
  your dataset.

  For the training of the recognition component that supports alignment, it is
  crucial that the dataset contains images with one word, that is labeled with
  rotated bounding boxes. The alignment feature ensures that relevant text
  regions are properly transformed and aligned for the recognition component.

  You also want enough training data to split it into three subsets, used
  for training, validation and testing the network. These subsets are
  preferably independent and identically distributed, see the section
  “Data” in the chapter [Deep Learning](toc_deeplearning.md).
- **Images** —

  The model poses requirements on the images, such as the dimensions,
  the gray value range, and the type.
  See the documentation of [`ReadDlModel`](read_dl_model.md) for the specific values
  of the trainable Deep OCR model.
  For a read model they can be queried with [`GetDlModelParam`](get_dl_model_param.md).
  In order to fulfill these requirements, you may have to preprocess your
  images.
  Standard preprocessing of an entire sample, including the
  image, is implemented in `preprocess_dl_samples`.

  Requirements for images used for inference are described in
  [`ApplyDeepOcr`](apply_deep_ocr.md).
- **Model output** —

  The network output depends on the task:

  - **training** —

    As output, the operator will return a dictionary `DLTrainResult`
    with the current value of the total loss as well as values for all
    other losses included in your model.
  - **inference and evaluation** —

    As output, the network will return a dictionary `DLResult`
    for every sample.
    This dictionary will include the recognized word as well as the
    candidates and their confidences for every character of the word.

### Evaluation Measures for Deep OCR Results

- **Deep OCR Detection** —

  The following evaluation measures are supported in HALCON.
  To compute these metrics for testing or validation, ground truth
  annotation is needed.

  - Precision, Recall and F-score

    The performance of Deep OCR Detection is evaluated using precision and
    recall on word boxes. The evaluation uses the intersection over union (IoU)
    in order to compare ground truth and predicted word boxes.
    The default IoU threshold for a match is *0.5*, it can be
    increased or decreased if needed.

    |  |  |
    | --- | --- |
    | ![figure](../assets/50e88fc01d1e7d2b.svg) | ![figure](../assets/3eaec845b73f2d9a.svg) |
    | ( 1) | ( 2) |

    Visual example of the IoU.
    (1) The input image with the ground truth bounding box (orange)
    and the predicted bounding box (light blue).
    (2) The IoU is the ratio between the area intersection and the
    union.

    The precision is the proportion of true positives to all positives
    (true and false ones). Thus, it is a measure of how trustworthy the
    detector is.

    $$precision = \frac{TP}{TP + FP}$$ ![figure](../assets/4c6c4d9dc413e523.svg)

    The recall is the proportion of the number of correctly detected words
    to all labeled words.

    $$\mathrm{recall} = \frac{\mathrm{TP}}{\mathrm{TP} + \mathrm{FN}}$$ ![figure](../assets/bb83c2ccf4c45ed3.svg)

    To represent this with a single number, we compute the F-score,
    the harmonic mean of precision and recall.

    $$F\-score = 2 * \frac{precision * recall}{precision + recall}$$ ![figure](../assets/a73c1679c1ebd8ac.svg)
  - Score of Angle Precision (SoAP)

    The SoAP value is a score for the precision of the inferred
    orientation angles. This score is determined by the angle differences
    between the inferred bounding boxes (I) and the corresponding ground
    truth annotations (GT):
    $$SoAP = 1.0 - \frac{1}{\pi} \frac{1}{k} \cdot \sum_k \lvert \varphi_k^I - \varphi_k^{GT} \rvert,$$ ![figure](../assets/5e7a7b1de452eae9.svg)
    where the index $k$ runs over all inferred bounding boxes.
- **Deep OCR Recognition** —

  The accuracy for a Deep OCR Recognition task is given as the percentage of
  correctly read words (CR) to the ground truth words (GT) of a dataset.
  The accuracy is then defined as:

  $$Accuracy = \frac{CR}{GT} \ast 100$$ ![figure](../assets/8915231f074ba229.svg)

---

#### List of Operators

- [`ApplyDeepOcr`](apply_deep_ocr.md) — Apply a Deep OCR model on a set of images for inference.

- [`CreateDeepOcr`](create_deep_ocr.md) — Create a Deep OCR model.

- [`GetDeepOcrParam`](get_deep_ocr_param.md) — Return the parameters of a Deep OCR model.

- [`ReadDeepOcr`](read_deep_ocr.md) — Read a Deep OCR model from a file.

- [`SetDeepOcrParam`](set_deep_ocr_param.md) — Set the parameters of a Deep OCR model.

- [`WriteDeepOcr`](write_deep_ocr.md) — Write a Deep OCR model in a file.
