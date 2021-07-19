# pyocrsrt
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1BdJG31zinrMFWxRt2utGBU2jdpv8xSgju)](https://en.cryptobadges.io/donate/1BdJG31zinrMFWxRt2utGBU2jdpv8xSgju)

**pyocrsrt**基于[VideoSubFinder](https://sourceforge.net/projects/videosubfinder/)开发,旨在将影片里的硬字幕通过ocr工具转换为.srt格式.

> 目前仅支持[百度OCR](https://ai.baidu.com/tech/ocr/general).

## 安装
    git clone https://github.com/Xavier-Lam/pyocrsrt.git
    cd pyocrsrt
    python setup.py install

## 快速开始
采用VideoSubFinder生成的TXTImages文件夹转化为srt字幕

    > pyocrsrt --ak <your access key> --sk <your secret key> -I /path/to/VideoSubFinder/TXTImages <output.srt>

或者完全采用本工具完成硬字幕提取,ocr为srt字幕

    > pyocrsrt --ak <your access key> --sk <your secret key> -V /path/to/your/video <output.srt> -f /path/to/your/VideoSubFinderWXW.exe -c /path/to/your/settings.cfg

> 这个过程可能很长,并且没有进度条,请耐心等待