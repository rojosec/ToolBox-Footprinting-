#!/bin/bash

echo "Verificando"

Dependencias(){
    pip3 install flask
    pip3 install python-whois
    pip3 install dnspython
    pip3 install builtwith
}

Servidor(){
    python3 index.py	
}

if [ -d /bin/pip3 ];
then
    echo "pip instalado"
    Dependencias
    Servidor
else
    apt-get install python3-pip -y
    Dependencias
    Servidor
fi


	
