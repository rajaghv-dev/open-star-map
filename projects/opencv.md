---
name: OpenCV
url: https://github.com/opencv/opencv
license: Apache-2.0
language: C++, Python
difficulty: intermediate
status: active
---

## What it does

The world's largest computer vision library. 2500+ optimized algorithms for image processing, ML, 3D reconstruction, object detection, and more. Used in robotics, medical imaging, autonomous vehicles.

## Why contribute

- Teaches C++ performance optimization and SIMD/NEON intrinsics
- Real-world ML and image processing algorithms
- Python bindings mean you can prototype in Python, implement in C++
- Massive impact — billions of deployments

## Dev environment setup

```bash
git clone https://github.com/opencv/opencv
git clone https://github.com/opencv/opencv_contrib  # extra modules

cd opencv
mkdir build && cd build
cmake -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -DBUILD_TESTS=ON \
      -DBUILD_EXAMPLES=ON ..
make -j$(nproc)

# Python bindings test
python3 -c "import cv2; print(cv2.__version__)"
```

## Where to find good first issues

- https://github.com/opencv/opencv/labels/good%20first%20issue
- https://github.com/opencv/opencv/labels/help%20wanted
- Documentation and Python sample improvements are great entry points

## Community

- Forum: https://forum.opencv.org/
- Q&A: https://answers.opencv.org/
- Mailing list: opencv-dev@googlegroups.com

## Learning resources

- Docs: https://docs.opencv.org/
- Tutorials: https://docs.opencv.org/4.x/d9/df8/tutorial_root.html
- Start with: add a Python tutorial or fix a failing test in `modules/python/test/`
