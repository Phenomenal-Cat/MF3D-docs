.. MF3D documentation master file, created by
   sphinx-quickstart on Fri May 22 11:05:57 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


About MF3D
===============================

.. raw:: html

	<iframe src="https://player.vimeo.com/video/323447440?autoplay=1&loop=1&color=ff9933&byline=0&portrait=0" style="display:block;padding:10px;border:5px" width="400" height="225" frameborder="0" align="right" allow="autoplay; fullscreen" allowfullscreen></iframe>

The Macaque Face 3D project is an effort to develop a parametrically controlled,
anatomically accurate, three-dimensional, virtual avatar of the Rhesus macaque face and head, for visual stimulation in behavioral neuroscience experiments involving this important model species. The avatar has been used to produced the first ever publicly available database :link-badge:`MF3D-Release-1,MF3D R1,ref,badge-primary text-white` of computer generated images of macaque facial expression and identity, which you can learn more about below.

Full details of how the model and rendered images were generated have been published here:

.. panels::
  :column: col-lg-12 p-1 border-0

  **Murphy AP & Leopold DA, (2019)**. `A parameterized digital 3D model of the Rhesus macaque face for investigating the visual processing of social cues. <https://doi.org/10.1016/j.jneumeth.2019.06.001>`_ *J.Neurosci.Methods*, 324: 108309. 
  :link-badge:`https://doi.org/10.1016/j.jneumeth.2019.06.001,"DOI:10.1016/j.jneumeth.2019.06.001", cls=badge-secondary badge-pill` 
  :link-badge:`https://pubmed.ncbi.nlm.nih.gov/31229584/, "PMID: 31229584", cls=badge-secondary badge-pill` 
  :link-badge:`https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7446874/, "PMCID: PMC7446874", cls=badge-secondary badge-pill`


The graphical abstract below summarizes how biometric data from real animals were acquired, analysed and parameterized to generate a realistic digital model. For more details and information on continuing development of MF3D, browse the table of contents.

.. image:: _images/ML_Figs/MurphyLeopold_GraphicalAbstract.png
  :width: 800
  :alt: MF3D construction summary

Supporting Open Science
--------------------------

.. image:: _images/Logos/Blender.svg
  :height: 30
  :alt: Blender
  :target: https://www.blender.org
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/Slicer.png
  :height: 30
  :alt: Blender
  :target: https://www.slicer.org
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/Figshare.svg
  :height: 30
  :alt: Figshare
  :target: https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/GitHub.png
  :height: 30
  :alt: GitHub
  :target: https://github.com/MonkeyGone2Heaven/MF3D-Tools
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/Copyleft.png
  :height: 30
  :alt: Copyleft
  :target: https://en.wikipedia.org/wiki/Copyleft
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/cc-by-nc.svg
  :height: 30
  :alt: CC-BY-NC
  :target: http://creativecommons.org/licenses/by-nc/4.0/
.. image:: _images/spacer.png
  :width: 10
.. image:: _images/Logos/gplv3.png
  :height: 30
  :alt: GPL v3
  :target: https://choosealicense.com/licenses/gpl-3.0/#

The MF3D project utilizes open-source software tools (`Blender <https://www.blender.org>`_, `Slicer <https://www.slicer.org>`_, Python) and provides open access **media** (hosted on `Figshare <https://figshare.com/projects/MF3D_Release_1_A_visual_stimulus_set_of_parametrically_controlled_CGI_macaque_faces_for_research/64544>`_ under Creative Commons `CC BY-NC
4.0 <http://creativecommons.org/licenses/by-nc/4.0/>`_) and **code** (hosted on `GitHub <https://github.com/MonkeyGone2Heaven/MF3D-Tools>`_ under GNU General Public License `GNU GPLv3 <https://choosealicense.com/licenses/gpl-3.0/#>`_). 


Contents
--------------------------

.. toctree::
   :maxdepth: 2

   Overview <MF3D-Overview>
   Background <MF3D-Background>
   MF3D Release 1 <MF3D-Release-1>
   MF3D Release 2 <MF3D-Release-2>
   MF3D Tools - Stimulus Editor <MF3D-Stimulus-Editor>
   MF3D Tools - Video Parameter GUI <MF3D-Video-Parameter-Estimation-GUI>
   MF3D Tools - Video Clip Compiler <MF3D-Video-Clip-Compiler>
   Methods - Face Space <MF3D-Parameterizing-anatomical-variations>
   MF3D Publications <MF3D-Research>


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`