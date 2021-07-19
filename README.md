# pyocrsrt
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1BdJG31zinrMFWxRt2utGBU2jdpv8xSgju)](https://en.cryptobadges.io/donate/1BdJG31zinrMFWxRt2utGBU2jdpv8xSgju)

[中文版Readme](README.zh.md)

**pyocrsrt** is a project based on [VideoSubFinder](https://sourceforge.net/projects/videosubfinder/), aims at rip hard subtitles into *.srt* format by using online ocr services. It uses image files generate by VideoSubFinder from videos to create .srt files.

> We only support [Baidu OCR](https://ai.baidu.com/tech/ocr/general) currently, you can contribute to our project to add other ocr backends.

## Installation
    git clone https://github.com/Xavier-Lam/pyocrsrt.git
    cd pyocrsrt
    python setup.py install

## Quickstart
You can use VideoSubFinder GUI to generate subtitle images by yourself, then using pyocrsrt to transform into text subtitles.

    > pyocrsrt --ak <your access key> --sk <your secret key> -I /path/to/VideoSubFinder/TXTImages <output.srt>


Or you can use pyocrsrt to complete the whole rip and ocr process.

    > pyocrsrt --ak <your access key> --sk <your secret key> -V /path/to/your/video <output.srt> -f /path/to/your/VideoSubFinderWXW.exe -c /path/to/your/settings.cfg

> It may takes a long time without any progress bar, please wait patiently.