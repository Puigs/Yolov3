FROM continuumio/miniconda3

WORKDIR /picsServer

COPY . .

EXPOSE 5000

RUN conda env create -f IA.yml -n IA

RUN echo "conda activate IA" >> ~/.bashrc

SHELL ["/bin/bash", "--login", "-c"]

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]