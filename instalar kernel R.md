# Cómo instalar el kernel de R en jupyter

Para instalar el kernel, primero se tienen que satisfacer las dependencias de librerías de R

En Ubuntu:
```Shell
sudo apt-get install libxml2-dev openssl libssl-dev libcurl4-openssl-dev curl #devtools
sudo apt-get install libcairo2-dev libunwind jupyter-client #JuniperKernel
```

En CentOS/RH:
```Shell
sudo yum install libxml2-devel openssl openssl-libs curl nettools cairo cairo-devel
sudo yum install libunwind libXt-devel jupyter-client
```
Después, se necesita tener instalado R:
```Shell
sudo yum install R #sudo apt-get install R
```
Se instala el cliente de Jupyter en Python:
```Shell
sudo pip install jupyter_client
```
En la máquina virtual de pythonista, no se puede instalar el kernel para todos los usuarios. Entonces hacemos lo siguiente:
```Shell
sudo mkdir /usr/local/share/jupyter
sudo chmod 777 /usr/local/share/jupyter
```
En R se instalan los paquetes necesarios:
```R
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), dependencies=TRUE)
devtools::install_github('IRkernel/IRkernel')
#Se habilita el kernel
IRkernel::installspec(user=FALSE) #Esto causa error en la VM de pythonista
```
Si se tiene problemas porque el usuario no puede habilitar el kernel, la última línea se corre como usuario regular:
```R
#Se habilita el kernel
IRkernel::installspec(user=FALSE)
```
Con esto, el kernel de R aparece habilitado y se puede probar con el siguiente código:
```R
print(head(mtcars))
#Se imprimen las primeras líneas del dataset mtcars.
```
Listo.
