# Super fast color transfer between images
In this we’ll learn how to use create a simple Python + OpenCV script to transfer the color between images.  


### Steps
- Take inputs from argparse(source,target). The source image contains the color space that you want your target image to mimic.
- convert the images from the RGB to *Lab* color space, being sure to utilizing the floating point data type (note: OpenCV expects floats to be 32-bit, so use that instead of 64-bit).The L*a*b* color space does a substantially better job mimicking how humans interpret color than the standard RGB color space, and as you’ll see, works very well for color transfer.
- Split the channels for both the source and target.
- Compute the mean and standard deviation of each of the L*a*b* channels for the source and target images.
- Subtract the mean of the L*a*b* channels of the target image from target channels.
- Scale the target channels by the ratio of the standard deviation of the target divided by the standard deviation of the source, multiplied by the target channels.
- Add in the means of the L*a*b* channels for the source.
- Clip any values that fall outside the range [0, 255].
- Merge the channels back together.
- Convert back to the RGB color space from the L*a*b* space.

**commands to run**
- python color_transfer.py -s images/ocean_sunset.jpg -t images/ocean_day.jpg
- python color_transfer.py -s images/autumn.jpg -t images/fallingwater.jpg