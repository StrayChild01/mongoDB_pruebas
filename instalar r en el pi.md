Para instalar R compilándolo desde 0, por si R se quedó una versión vieja en raspbian, necesitamos lo siguiente:

```shell
sudo apt-get install -y gfortran libreadline6-dev libx11-dev libxt-dev \
       libpng-dev libjpeg-dev libcairo2-dev xvfb \
       libbz2-dev libzstd-dev liblzma-dev \
       libcurl4-openssl-dev \
       texinfo texlive texlive-fonts-extra \
       screen wget openjdk-8-jdk
cd /usr/local/src
sudo wget https://cran.rstudio.com/src/base/R-3/R-3.6.0.tar.gz
sudo su
tar zxvf R-3.6.0.tar.gz
cd R-3.6.0
# esto --with-x=no es para poder ejecutar R y el kernel de Jupyter.
./configure --with-x=no --with-cairo=yes --with-libpng=yes --enable-R-shlib #--with-blas --with-lapack #optional
make
make install
cd ..
rm -rf R-3.6.0*
exit
cd
```
