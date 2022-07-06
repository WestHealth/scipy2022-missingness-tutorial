from jupyter/tensorflow-notebook
RUN conda install mamba
RUN mamba install missingno
RUN pip install autoimpute mkl-service
USER root
RUN apt update
RUN apt install gcc g++ -y
USER jovyan
COPY docker-README.md README.md
COPY docker/*.ipynb docker/*.py .
COPY data/* data/
