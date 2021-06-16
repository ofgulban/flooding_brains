Data is derived from <https://braincatalogue.org/>. The okapi cerebrum segmentation is done by:
1. Applying N4 bias correction (as implemented in [3DSlicer](https://www.slicer.org/)).
2. Using [Segmentator](https://github.com/ofgulban/segmentator) to get n initial binary mask.
3. Removing the cerebellum and brainstem by manually editing in [ITKSNAP](http://www.itksnap.org/pmwiki/pmwiki.php).
4. Manually clenaing up the rest of the sulci again in ITKSNAP (manual work is done through using a Wacom drawing tablet).
5. Smoothing the binary file and re-binarizing it by using `fslsmaths <input.nii> -s XX -thr 0.5 -bin <output.nii>` (Smoothing FWHM is selected as 2 * voxel resolution of the input file).
