.. _MF3D_Database:

============================
:fa:`database` MF3D Database
============================

CT data acquisition
------------------------

All 3D surface data used in MF3D databases were derived from *in vivo* computed tomography (CT) scans of anesthetized captive Rhesus macaque (*m.mulatta*) monkeys. Data were acquired at a range of research institutions, under protocols approved by local Institutional Animal Care and Use Committee (IACUC)'s that conform to national animal welfare law (e.g. the `Animal Welfare Act <https://www.nal.usda.gov/animal-health-and-welfare>`_ in the US).


Database demographics
------------------------

The validity of a morphable model for a given application is fundamentally limited by the sample data that were used to construct it. In particular, while the central tendency of a sample will quickly converge towards an accurate representation of the population mean, the accuracy of linearly interpolated morphs into the extreme periphery of the model space will suffer if that region is under sampled. For example, changes in craniofacial morphology with age are non-linear: there is an early period of bone and muscle growth, followed by loosening of the skin and eventual loss of muscle tone. The demographic make-up of the samples used to construct the original MF3D face-space and other morphable models are provided below.

.. tab:: MF3D (faces)

  .. plot:: PlotDemo_MF3D.py
    :include-source: False
    :width: 300px
    :align: right

  The demographic make-up of the sample used to construct the original MF3D face-space is shown in the plot to the right. All animals in this sample (N = 36) were over 4 years of age, and only a small proportion were female (N = 7). The voxel resolution of CT volumes varied from 0.25 - 0.37mm in-plane, and 0.125 - 0.5mm slice thickness. 

  .. container:: clearer

    .. image :: _images/spacer.png
       :width: 1

  .. dropdown:: MF3D Demographics Table
    :title: bg-primary text-white

    .. csv-table:: 
      :widths: auto
      :file: _static/CSVs/MF3D_database.csv
      :header-rows: 1
      :align: left 

.. tab:: MF3Di (infants)

  .. plot:: PlotDemo_UNC.py
    :include-source: False
    :width: 300px
    :align: right

  To extend the face-space model to more accurately cover the craniofacial morphology of infant macaques, we used data from the `UNC-Wisconsin Rhesus macaque Neurodevelopment Database <https://data.kitware.com/#collection/54b582c38d777f4362aa9cb3>`_ (`Young et al., 2017 <https://doi.org/10.3389/fnins.2017.00029>`_). This database includes anatomical (T1-weighted) MRI scans from 36 infant Rhesus macaques between the ages of 2 weeks to 4 years old, collected longitudinally (150 scans total). The demographic distribution of this sample is shown in the plot on the right. 

  .. container:: clearer

    .. image :: _images/spacer.png
       :width: 1

  .. dropdown:: MF3Di Demographics Table
    :title: bg-primary text-white

    .. csv-table:: 
      :widths: auto
      :file: _pyplots/UNC_Demographics.csv
      :header-rows: 1
      :align: left 

.. tab:: MB3D (bodies)

  .. plot:: PlotDemo_MB3D.py
    :include-source: False
    :width: 300px
    :align: right

  To extend the theoretical concept underlying 'face-space' to macaque bodies, we used a sample of whole-body CT data from 200 adult Rhesus macaques from the `CNPRC <https://cnprc.ucdavis.edu/>`_, that was acquired by researchers at UC Davis (`Buck et al., 2021 <https://doi.org/10.1016/j.jhevol.2021.103049>`_). A subset of these data are available via `Morphosource <https://www.morphosource.org/projects/00000C291?f%5Bmember_of_project_ids_ssim%5D%5B%5D=00000C291&locale=en>`_. 

  .. container:: clearer

    .. image :: _images/spacer.png
       :width: 1

  .. dropdown:: MB3D Demographics Table
    :title: bg-primary text-white

    .. csv-table:: 
      :widths: auto
      :file: _static/CSVs/MB3D_table.csv
      :header-rows: 1
      :align: left 

