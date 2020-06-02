MF3D Stimulus Editor
====================

We provide a graphical user interface (GUI) programmed in Matlab ``MF3D_StimEditor.m`` to help users of the MF3D R1 stimulus set
to download, select, load, edit, analyse and save the images that they wish to use in
their experiments. The GUI is intended to provide an easy way for users
to select subsets of the 14,000 images and apply simple image
manipulations without requiring them to write their own code. However,
the code can easily be adapted by users who wish to perform other
operations that are not currently implemented in the GUI.

Getting started
---------------

`MF3D Tools <https://github.com/MonkeyGone2Heaven/MF3D-Tools>`_ contains scripts that can be used to downloaded the MF3D R1 stimulus sets from Figshare, unzip them and reorganize the directory structure. If you are using Matlab, this can be done using the
``MF3D_Installer.m`` GUI as follows:

-  Clone the `MF3D-Tools <https://github.com/MonkeyGone2Heaven/MF3D-Tools>`_ GitHub repository by opening a terminal window, navigating to the directory where you want MF3D-Tools installed and run:

.. code-block:: none

  git clone https://github.com/MonkeyGone2Heaven/MF3D-Tools.git

- Alternatively, you can `download MF3D Tools <https://github.com/MonkeyGone2Heaven/MF3D-Tools/archive/master.zip>`_ directly and unzip the folder.

-  Open Matlab, navigate to the 'MF3D Tools' folder and run ``MF3D_Installer.m`` in the Matlab command line. Note that the script requires permissions to move the code and image files around.

.. figure:: _images/GUIs/MF3D_Installer.png
  :width: 400
  :align: right
  :class: align-right
  :alt: MF3D Installer GUI

-  The MF3D Installer GUI window appears. Select a destination folder where you would like the MF3D R1 stimulus set installed. If the MF3D R1 stimulus set is already fully or partially installed, the corresponding fields will turn green.

-  Select which subsets of the MF3D R1 stimulus set you want to install using the check boxes. 

-  Click the **Download** button to begin download and unzipping. If the files are already downloaded (indicated by a full progress bar) but the files have not been reorganized, select **Reorganize** button.




The parameters used to generate each image in the MF3D R1 stimulus set
are provided in the accompanying spreadsheets (.csv files) - one for the
expression set and another for the identity set. When the GUI is
initialized it first reads these data into Matlab.

Stimulus selection
------------------

The stimulus set contains 14,000 images, which is more than a single
experiment is likely to need. In order to simplify the selection of a
subset of the stimuli, the top panel of the GUI allows the selection by
stimuli by a variety of parameters. The drop down menu at the top left
allows you to select between the 'Expressions' and 'Identities' subsets,
and will activate and deactivate the corresponding parameter lists.
Multiple rows can be selected in each active parameter list, and the
total number of images currently selected appears in the top right hand
corner of the GUI.

.. figure:: _images/MF3D_Tools_StimEditor_Fig3.png
   :alt: MF3D Stimulus Editor GUI selection panel

Preview panel
-------------

Whenever the stimulus selection is changed, the list of selected images
is updated in the dropdown menu of the ``Preview panel``. Selected
images can be previewed by either selecting the file name in the
dropdown menu, or using the slider to scroll through the selected
images.

Image masking
-------------

Each color image in the MF3D R1 stimulus set has a corresponding label
map, which can be used to mask parts of the image in order to create new
variations. In the ``Masking panel`` of the stimulus editor GUI users
can select color-coded parts of the face, body and background to toggle
on or off, which will update the ``Preview panel`` image. Additional
controls to the left of the ``Masking panel`` provide the following
functionality:

-  ``Apply Smoothing``: Apply image smoothing to the label map before
   masking the color image. This option reduces pixelated edges in the
   alpha transparency layer of the final images, as can be seen in the
   ``Preview panel``.

-  ``Kernel width``: Sets the width of the smoothing kernel (pixels)
   applied to the label map before masking.

-  ``Background``: Sets the type of background to use for the output
   images. The default is transparent (same as input images), but it can
   also be set to use a solid color or a Fourier scrambled version of
   the original image.

-  ``Ellipse crop``: Displays an ellipse in the ``Preview panel`` that
   can be dragged, scaled and resized with the mouse. Pixels outside of
   the ellipse will have alpha transparency values of 0 (fully
   transparent) when saved. When ellipse crop is enabled, the background
   selected will only appear inside the ellipse.

-  ``Isotropic``: Maintain a 1:1 aspect ratio ellipse (i.e. circular)
   crop.

-  ``Cyclopean center``: this will center the cropping ellipse on the
   'cyclopean eye' (indicated in the ``Preview panel`` by a white
   astrisk) by finding the centroid of each group of pixels belonging to
   the 'eye' label group (indicated by red astrisks) and calculating the
   mid-point. Turning this option on will cause the location of the
   avatar's body on the screen to shift as the head turns, but will keep
   the eyes either side of the centre on the horizontal meridian of the
   screen across head angles.

-  ``Radius (px)``: Sets the radius of the elliptical crop selection in
   pixels.

.. figure:: _images/MF3D_Tools_StimEditor_Fig2.png   
   :alt: MF3D Stimulus Editor GUI preview panel

Cropping and rescaling
----------------------

To apply custom cropping of the images, select the

Image analysis and normalization
--------------------------------

In vision science, it is often desirable to either quantify or control the
low-level visual properties of the stimuli. The MF3D Stimulus Editor
allows users to run functions from the `SHINE
Toolbox <http://www.mapageweb.umontreal.ca/gosselif/SHINE/>`__
(`Willenbockel et al., 2010 <https://doi.org/10.3758/BRM.42.3.671>`__)
once it has been downloaded and added to the Matlab path.
