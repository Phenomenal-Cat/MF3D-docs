
===============================
About MF3D
===============================

.. raw:: html

	<iframe src="https://player.vimeo.com/video/323447440?autoplay=1&loop=1&color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="right" allow="autoplay; fullscreen" allowfullscreen></iframe>

The Macaque Face 3D project is an effort to develop a parametrically controlled, anatomically accurate, three-dimensional, virtual avatar of the Rhesus macaque face and head, for visual stimulation in behavioral neuroscience experiments involving this important model species. The avatar has been used to produced the first ever publicly available database :bdg-ref-primary:`MF3D R1 <MF3D-Release-1>` of computer generated images of macaque facial expression and identity, which you can learn more about below. Full details of how the model and rendered images were generated are published in the methods paper by `Murphy & Leopold (2019) <https://doi.org/10.1016/j.jneumeth.2019.06.001>`_ linked below, while subsequent publications that have utilized this resource can be found in the :bdg-ref-primary:`publications <Pubs>` section.

.. card::
  :class-body: sd-bg-white p-2 m-0
  :class-footer: sd-bg-light p-1 m-0

  :fa:`book` **Murphy AP & Leopold DA (2019)**. `A parameterized digital 3D model of the Rhesus macaque face for investigating the visual processing of social cues. <https://doi.org/10.1016/j.jneumeth.2019.06.001>`_ :link-badge:`https://doi.org/10.1016/j.jneumeth.2019.06.001,"J.Neurosci.Methods",cls=badge-primary text-white` 324: 108309. 

  +++++

  .. image:: _images/Logos/OpenAccess.png
    :height: 30
    :alt: OpenAccess
    :target: https://publicaccess.nih.gov/
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/PDF_button.png
    :height: 30
    :alt: PDF download
    :target: _static/PDFs/MF3D_Papers/MurphyLeopold_2019-MacaqueAvatar.pdf
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/PubMed_button.png
    :height: 30
    :alt: PubMed
    :target: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7446874/
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/GoogleScholar.png
    :height: 30
    :alt: Google Scholar
    :target: https://scholar.google.com/scholar?cites=9006831545148241977&as_sdt=5,47&sciodt=0,47&hl=en
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/ResearchGate.png
    :height: 30
    :alt: ResearchGate
    :target: https://www.researchgate.net/publication/333700889_A_parameterized_digital_3D_model_of_the_Rhesus_macaque_face_for_investigating_the_visual_processing_of_social_cues
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Mendeley.png
    :height: 30
    :target: https://www.mendeley.com/catalogue/1e719e6b-6d3c-3182-b801-fe4f26b058da/
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Figshare_Icon.png
    :height: 30
    :alt: Figshare
    :target: https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544


:fa:`video` Video Demos
===============================

.. card-carousel:: 2

  .. card:: 
    :class-header: sd-bg-primary sd-text-white sd-font-weight-bold
    :class-body: sd-bg-white p-0 m-0
    :class-footer: sd-bg-white sd-text-dark p-1


    .. raw:: html

      <iframe src="https://player.vimeo.com/video/326460055?color=ff9933&byline=0&portrait=0" style="display:block;padding:0px;border:0px" width="355" height="200" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>

    +++

    .. dropdown:: :fa:`face-grimace` **Facial expression and gaze**
      :color: success
      :chevron: down-up
      :margin: 0
      :class-title: p-1


      This video demonstrates how our macaque model of emotional facial
      expressions (for a single identity) can be continuously and
      parametrically varied to adjust appearance. The model was constructed
      using computed tomography (CT) data from a real Rhesus macaque, acquired
      under anesthesia, and edited and rigged by a professional digital
      artist. In addition to control of various facial expressions, the
      model's head and eye gaze direction can be programmatically controlled,
      as well as other variables such as environmental lighting and surface
      coloration, amongst others.
    

  .. card:: 
    :class-header: sd-bg-primary sd-text-white sd-font-weight-bold
    :class-body: sd-bg-white p-0 m-0
    :class-footer: sd-bg-white sd-text-dark p-1

    .. raw:: html

      <iframe src="https://player.vimeo.com/video/323447440?loop=1&color=ff9933&byline=0&portrait=0" style="display:block;padding:0px;border:0px" width="355" height="200" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>

    +++

    .. dropdown:: :fa:`dice-d20` Identity morphing
      :color: success
      :chevron: down-up
      :margin: 0
      :class-title: p-1

      Individual variations in cranio-facial morphology (3D face shape) can be continuously and
      parametrically varied to adjust appearance, as in the `MF3D R1
      Identity <https://doi.org/10.6084/m9.figshare.8226311>`_ stimulus set.
      The statistical model was constructed through principal component
      analysis (PCA) of the 3D surface reconstructions of 23 real Rhesus
      monkeys from computed tomography (CT) data acquired under anesthesia.
      The 3D plot in the top right corner illustrates the first three
      principal components of this 'face-space', where the origin of the plot
      represents the sample average face.


  .. card:: 
    :class-header: sd-bg-primary sd-text-white sd-font-weight-bold
    :class-body: sd-bg-white p-0 m-0
    :class-footer: sd-bg-white sd-text-dark p-1


    .. raw:: html

      <iframe src="https://player.vimeo.com/video/394782616?color=ff9933&byline=0&portrait=0" style="display:block;padding:0px;border:0px" width="355" height="200" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>

    +++
    .. dropdown:: :fa:`film` Animated sequences
      :color: success
      :chevron: down-up
      :margin: 0
      :class-title: p-1


      Animated facial expression clips from the `MF3D R1
      Animation <https://figshare.com/articles/MF3D_R1_Animations/8226317>`_
      stimulus set can be combined to form a longer continuous animation
      sequence for use in experiments that require more naturalistic dynamics.
      This example was generated using the Python script
      `MF3D_ConcatClips_Demo.py <https://github.com/Phenomenal-Cat/MF3D-Tools/blob/master/MF3D_Blender/MF3D_ConcatClips_Demo.py>`_
      to interleave the appropriate head rotation sequences between consecutive expression clips, controlled via the open-source `Blender <https://www.blender.org>`_ video sequence editor.


  .. card:: 
    :class-header: sd-bg-primary sd-text-white sd-font-weight-bold
    :class-body: sd-bg-white p-0 m-0
    :class-footer: sd-bg-white sd-text-dark p-1

    .. raw:: html

      <iframe src="https://player.vimeo.com/video/329805226?color=ff9933&byline=0&portrait=0" style="display:block;padding:0px;border:0px" width="355" height="200" frameborder="0" align="left" allow="autoplay; fullscreen" allowfullscreen></iframe>

    +++

    .. dropdown:: :fa:`chart-line` Facial dynamics estimation
      :color: success
      :chevron: down-up
      :margin: 0
      :class-title: p-1


      In order to simulate naturalistic facial dynamics in the macaque avatar,
      we estimate the time courses of facial motion from video footage of real
      animals. Applying these time courses to the animation of bones and shape
      keys of the model, we can mimic the facial motion of the original clip,
      while retaining independent control over a wide range of other
      variables. The output animation can be rendered at a higher resolution
      and frame rate (using interpolation) than the input video. (Original
      video footage in the left panel is used with permission of Off The
      Fence™).


:fa:`location-arrow` Site Navigation
========================================

.. grid:: 6
   :gutter: 2
   :margin: 0
   :padding: 0

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Background
      :link-type: doc
      :text-align: center
   
      :fa:`graduation-cap` History

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Stimuli
      :link-type: doc
      :text-align: center
   
      :fa:`film` Stimuli

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Tools
      :link-type: doc
      :text-align: center
   
      :fa:`gears` Tools

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Database
      :link-type: doc
      :text-align: center
   
      :fa:`database` Database

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Methods
      :link-type: doc
      :text-align: center
   
      :fa:`flask` Methods

   .. grid-item-card::
      :class-card: sd-bg-primary sd-text-white sd-rounded-3 sd-font-weight-bold
      :link: MF3D-Research
      :link-type: doc
      :text-align: center
   
      :fa:`book` Research



:fa:`circle-info` Developing the avatar
========================================

The graphical abstract below summarizes how biometric data from real animals were acquired, analysed and parameterized to generate a realistic digital model. For more details and information on continuing development of MF3D, browse the table of contents.


.. image:: _images/ML_Figs/MurphyLeopold_GraphicalAbstract.png
  :width: 550
  :alt: MF3D construction summary
  :align: left


.. raw:: html

  <iframe src="https://player.vimeo.com/video/243763351?autoplay=1&loop=1&color=ff9933&byline=0&portrait=0" width="225" height="225" frameborder="0" align="right" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>

.. container:: clearer

    .. image :: _images/spacer.png
       :width: 1

.. dropdown:: :fa:`lock-open` Promoting Open Science
  :container: + shadow
  :title: bg-primary text-white font-weight-bold
  :body: bg-light 
  :animate: fade-in
  :open:

  The MF3D project strives to utilize open-source software tools where possible (`Blender <https://www.blender.org>`_, `Slicer <https://www.slicer.org>`_, Python) and provides open access **media** (hosted on `Figshare <https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544>`_ under Creative Commons `CC BY-NC 4.0 <http://creativecommons.org/licenses/by-nc/4.0/>`_) and **code** (hosted on `GitHub <https://github.com/Phenomenal-Cat/MF3D-Tools>`_ under GNU General Public License `GNU GPLv3 <https://choosealicense.com/licenses/gpl-3.0/#>`_). 

  .. image:: _images/Logos/OpenSource.png
    :height: 30
    :alt: OpenSource
    :target: https://opensource.org/
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/OpenAccess_logo.png
    :height: 30
    :alt: OpenAccess
    :target: https://en.wikipedia.org/wiki/Open_access
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Copyleft.png
    :height: 30
    :alt: Copyleft
    :target: https://en.wikipedia.org/wiki/Copyleft
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/cc-by-nc.svg
    :height: 30
    :alt: CC-BY-NC
    :target: http://creativecommons.org/licenses/by-nc/4.0/
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/gplv3.png
    :height: 30
    :alt: GPL v3
    :target: https://choosealicense.com/licenses/gpl-3.0/#
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Blender.svg
    :height: 30
    :alt: Blender
    :target: https://www.blender.org
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Slicer.png
    :height: 30
    :alt: Slicer
    :target: https://www.slicer.org
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/Figshare.svg
    :height: 30
    :alt: Figshare
    :target: https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544
  .. image:: _images/spacer.png
    :width: 5
  .. image:: _images/Logos/GitHub.png
    :height: 30
    :alt: GitHub
    :target: https://github.com/MonkeyGone2Heaven/MF3D-Tools
  .. image:: _images/spacer.png
    :width: 5


.. image:: _images/Logos/NALabs_b.png
  :width: 1


.. toctree::
   :hidden:
   :maxdepth: 2

   MF3D-Background
   MF3D-Stimuli
   MF3D-Tools
   MF3D-Database
   MF3D-Methods
   MF3D-Research
