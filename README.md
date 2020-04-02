#  RGB 3D Color Histogram Image Retrieval

Simple Color Histogram search implementation.

##   Project Objectives
>  Use 3d Color Histogram descriptor to extract features

>  Use distance metric to find similar color histograms

##Results
To index dataset photos use following command, (index.cpickle is the file where we will store indexes):

    python3 index.py --dataset images --index index.cpickle
Output:
    [INFO] done...indexed 25 images

To search images write:

    python3 search.py --dataset images --index index.cpickle

Output:

![](https://sun9-53.userapi.com/c854528/v854528409/2187b4/ytGIVg8MPgk.jpg)

![](https://sun9-44.userapi.com/c854528/v854528409/2187cf/ZZHzRJoFd24.jpg)

### References

 - [https://www.pyimagesearch.com/2014/01/27/hobbits-and-histograms-a-how-to-guide-to-building-your-first-image-search-engine-in-python/](https://www.pyimagesearch.com/2014/01/27/hobbits-and-histograms-a-how-to-guide-to-building-your-first-image-search-engine-in-python/)
