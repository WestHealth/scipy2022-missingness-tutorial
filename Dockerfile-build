from jupyter/tensorflow-notebook
RUN conda install mamba
RUN mamba install missingno
RUN pip install autoimpute mkl-service
USER root
RUN apt update
RUN apt install gcc g++ -y
COPY docker-README.md README.md
COPY colab/helpers.py .
COPY docker/*.ipynb docker/*.py .
COPY slides.pdf .
COPY data/* data/
RUN chown -R jovyan .
USER jovyan
ENV DOCKER_STACKS_JUPYTER_CMD notebook
