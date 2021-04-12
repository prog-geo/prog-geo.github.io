ARG BASE_IMAGE=qgis/qgis:release-3_16
FROM ${BASE_IMAGE}

LABEL img.author="Gilberto Ribeiro de Queiroz e Thales Körting" \
      img.description="Este script possibilita a criação de \
uma imagem com o ambiente computacional necessário ao \
desenvolvimento de plugins para o QGIS."

ARG ROOT_USER=root
ARG QGIS_USER_NAME=qgis
ARG QGIS_USER_ID=1000
ARG QGIS_USER_GROUP=qgis
ARG QGIS_USER_GROUP_ID=1000

RUN apt-get update && \
    apt-get install -y openjdk-8-jdk wget && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install --upgrade wheel && \
    pip3 install pb_tool

RUN groupadd --gid ${QGIS_USER_GROUP_ID} ${QGIS_USER_GROUP} && \
    useradd --create-home \
            --shell /bin/bash \
            --uid ${QGIS_USER_ID} \
            --gid ${QGIS_USER_GROUP} ${QGIS_USER_NAME}

USER ${QGIS_USER_NAME}

WORKDIR /home/${QGIS_USER_NAME}

ADD liclipse_6.1.0_linux.gtk.x86_64.tar.gz /home/${QGIS_USER_NAME}/

USER ${ROOT_USER}

CMD ["sleep", "infinity"]