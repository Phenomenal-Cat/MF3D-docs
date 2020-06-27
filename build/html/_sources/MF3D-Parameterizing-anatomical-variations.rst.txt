==============================
MF3D 'Face-space' construction
==============================

.. contents:: :local:

Parameterizing anatomical variations
------------------------------------

.. figure:: _images/DocFigs/FaceSpace_DurerLeopold.png
  :align: right
  :figwidth: 50%
  :width: 100%
  :alt: Parameterization of facial shape

  **A.** `Dürer (1528) <https://en.wikipedia.org/wiki/Albrecht_D%C3%BCrer>`_ originally proposed mathematical descriptions of variation in face shape using deformation grids. **B.** `Leopold et al., 2006 <https://doi.org/10.1038/82947>`_ used digital 3D scans of human faces to generate visual stimuli for neuroscientific research. The 'face-space' construct of facial identity variation features the average face at the center of a high-dimensional parameter space, in which distance from the center corresponds to facial distinctiveness.

One of the earliest studies of variation in anatomical proportions was
by the German Renaissance artist `Albrecht Dürer
(1528) <https://www.nlm.nih.gov/exhibition/historicalanatomies/durer_bio.html>`__,
who described the application of `deformation
grids <https://www.virtual-anthropology.com/virtual-anthropology/compare/geometric-morphometrics/thin-plate-spline/>`__
to mathematically describe variation in human facial anatomy. This approach was further developed by Scottish mathematical biologist D'Arcy Thompson in `On Growth and Form (1917) <https://en.wikipedia.org/wiki/On_Growth_and_Form>`_. 

In the digital age, a pioneering study by `Blanz & Vetter (1999) <https://doi.org/10.1145/311535.311556>`__ was the first to apply this approach to 3D face data acquired through laser scans of 200 human participants. Specifically, the authors used `principal component analysis (PCA) <https://en.wikipedia.org/wiki/Principal_component_analysis>`_ to identify the major components of morphological variation in their sample. The resulting statistical description or 'morphable model' of 'face space' can be used to generate an infinite number of plausible novel human faces. This resource has since be used in a vast number of neuroscience and psychology studies, and is commercially available as the `FaceGen <https://facegen.com/>`__ software.


Craniofacial morphology analysis for MF3D
-----------------------------------------

The methods for creating the macaque face-space used to generate identity
variations in MF3D is broadly similar to that used by Blanz & Vetter. The steps
Involved are described in `Murphy & Leopold
(2019) <https://doi.org/10.1016/j.jneumeth.2019.06.001>`__ and
illustrated in figure 5 from that paper (shown below). Briefly, Corresponding vertices
were manually selected on a low polygon count (50,000 vertices) base mesh topology
(created based on individual M02 of the CT data sample) and the high poly raw
surface meshes of each other individual (panel A). This was performed in the
commercial software `Wrap3 <https://www.russian3dscanner.com/>`__, which then applies
a warping process to produces a surface mesh with topology A and
morphology B (bottom left of panel A). This process was repeated for each individual in the sample, and the resulting mesh data were then manually cleaned by a professional digital artist (bottom right of panel A).

The cleaned corresponding meshes of all individuals (N = 24 in the initial sample) were then imported into Matlab, their vertex positions were averaged to generate the mesh of 
the sample mean and a PCA was run. 


.. figure:: _images/ML_Figs/MurphyLeopold_Fig5.jpg
  :alt: Facial morphology analysis

  **Morphable face model construction. A.** Example of manual selection of corresponding vertices on the low-poly base mesh topology (topology A) created from individual M02 (morphology A) and the high-poly raw surface mesh of individual M09 (right). The warping process produces a surface mesh with topology A and morphology B (bottom left), which can then be manually edited (bottom right). **B.** Sample mean mesh surface. **C.** First five principal components (mean ± 2σ) of macaque face-space. **D.** Locations of original sample identities (n = 23) projected into principal component face-space (first 3 PC dimensions only). **E.** Distribution of CT scan voxel volume for each individual plotted against their Euclidean distance from the sample mean (σ). **F.** Percentage of variance in sample cranio-facial morphology explained by each principal component. **G.** Distributions of demographic variables for Rhesus macaque CT data sample. **H.** Age trajectory through face-space for males calculated by averaging 5 youngest (2nd column) and 5 oldest (4th column) males, and extrapolating. **I.** Sexual dimorphism trajectory through face-space calculated by averaging 5 males (2nd column) and 5 females (4th column), and extrapolating. Colour map indicates the displacement of each vertex relative to the mean (middle column) for each mesh. Meshes were aligned via Procrustes method.


Sample space expansion
-----------------------------------

.. plot:: PlotDemo_UNC.py
  :include-source: False
  :width: 300px
  :align: right

The validity of a 'face-space' is fundamentally limited by the sample used to construct it. The demographic make-up of the sample used to construct the original MF3D face-space is shown in Figure 5G above. All animals in this sample (N = 36) were over 4 years of age, and only a small proportion were female (N = 7). Although it is possible to identify an axis within the N-dimensional face-space that corresponds to age and then linearly extrapolate (Figure 5H), the resulting constructions of facial morphology are unlikely to be realistic (e.g. due to non-linear age related changes in facial morphology).


To resolve this issue, we expanded the sample used to construct the face-space model, using the `UNC-Wisconsin Rhesus macaque Neurodevelopment Database <https://data.kitware.com/#collection/54b582c38d777f4362aa9cb3>`_ (`Young et al., 2017 <https://doi.org/10.3389/fnins.2017.00029>`_). This database includes anatomical (T1-weighted) MRI scans from 36 infant Rhesus macaques between the ages of 2 weeks to 4 years old, collected longitudinally (150 scans total). The demographic distribution of this additional sample is shown in the plot on the right. The figure below illustrates raw soft tissue surface reconstructions from the T1 data for an individual at 5 time points during the first year of life. The segmentation of soft tissue from MRI data is noticeably noisier than segmentations from CT data, requires more smoothing and therefore lacks comparable detail. However, the data are sufficient to estimate craniofacial morphology since we fit the existing base mesh (clean topology) constructed from CT data to these raw MRI-derived meshes.

.. figure:: _images/Renders/UNC_Summary_Fig1.png
  :align: left
  :figwidth: 60%
  :width: 100%
  :alt: Craniofacial development in Rhesus macaque

  Raw soft tissue reconstructions of an individual Rhesus macaque across time, generated from the `UNC Wisconsin Rhesus macaque Neurodevelopment Database <https://data.kitware.com/#collection/54b582c38d777f4362aa9cb3>`_ (`Young et al, 2017 <https://doi.org/10.3389/fnins.2017.00029>`_).


.. container:: clearer

    .. image :: _images/spacer.png
       :width: 1


Expression transfer
------------------------------------

Another limitation of the original MF3D model was that identity was parameterized separately from expression, and it was therefore not possible to generate faces of different individuals with the various modeled expressions. To resolve this issue we performed expression cloning, transferring the expression component of the original model into the face-space framework. This was achieved using `Wrap3 (RS3D) <https://www.russian3dscanner.com/>`_ software.
