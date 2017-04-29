
# install opencv
## env
python 2.7.13 /usr/local/bin/python
mac 10.12.4-x86_64
HOMEBREW_VERSION: 1.1.8
```shell
# add opencv
brew tap homebrew/science
# install opencv
brew install opencv
```

## error
```shell
# Invalid formula: /usr/local/Homebrew/Library/Taps/homebrew/homebrew-science/kmc.rb
# "cxx14" is not a recognized standard
# Error: Cannot tap homebrew/science: invalid syntax in tap!

# solution

vim ~/.bash_profile
# i
# export PATH=${PATH}:/usr/local/bin
# wq
source ~/.bash_profile

brew doctor
# Please note that these warnings are just used to help the Homebrew maintainers
# with debugging if you file an issue. If everything you use Homebrew for is
# working fine: please don't worry and just ignore them. Thanks!

# Warning: Broken symlinks were found. Remove them with `brew prune`:
#  /usr/local/share/man/man8/prlexec.8
brew config
# HOMEBREW_VERSION: 1.1.8
# ORIGIN: https://github.com/Homebrew/brew
# HEAD: e59ada508727f11464595893783beb914c26f60b
# Last commit: 3 months ago
# Core tap ORIGIN: https://github.com/Homebrew/homebrew-core
# Core tap HEAD: e202f1bbaccd89648600389e99def43d181104b7
# Core tap last commit: 74 minutes ago
# HOMEBREW_PREFIX: /usr/local
# HOMEBREW_REPOSITORY: /usr/local/Homebrew
# HOMEBREW_CELLAR: /usr/local/Cellar
# HOMEBREW_BOTTLE_DOMAIN: https://homebrew.bintray.com
# CPU: quad-core 64-bit skylake
# Homebrew Ruby: 2.0.0-p648
# Clang: 8.1 build 802
# Git: 2.10.1 => /usr/local/bin/git
# Perl: /usr/bin/perl
# Python: /usr/local/bin/python => /usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/bin/python2.7
# Ruby: /usr/bin/ruby => /System/Library/Frameworks/Ruby.framework/Versions/2.0/usr/bin/ruby
# Java: 1.8.0_111
# macOS: 10.12.4-x86_64
# Xcode: N/A
# CLT: 8.3.0.0.1.1490382677
# X11: N/A

# 然后就一直不停的运行，tm不信就过不去
# add opencv
brew tap homebrew/science
# install opencv
brew install opencv
# 然后就安装成功了... 可能是网络问题？

```

# use opencv

## error
```shell
# OpenCV Error: Assertion failed (scn == 3 || scn == 4) in cvtColor, file /tmp/opencv-20170224-1869-10nlf6f/opencv-2.4.13.2/modules/imgproc/src/color.cpp, line 3739
# Traceback (most recent call last):
#  File "/Users/huangshihe/bigdata/pycodes/face_photo/test.py", line 19, in <module>
#    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.error: /tmp/opencv-20170224-1869-10nlf6f/opencv-2.4.13.2/modules/imgproc/src/color.cpp:3739: error: (-215) scn == 3 || scn == 4 in function cvtColor

# solution
# 图片文件未找到，检查图片文件地址是否正确，修改后，通过。
```