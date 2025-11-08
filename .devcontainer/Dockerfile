# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/miniconda:0-3

ENV MAMBA_NO_BANNER=1

COPY environment/environment.yml /tmp/environment.yml

RUN mamba env create -f /tmp/environment.yml \
    && mamba clean -afy \
    && rm -rf /tmp/environment.yml \
    && echo \". /opt/conda/etc/profile.d/conda.sh\" >> /etc/profile.d/intro-gis.sh \
    && echo \"conda activate intro-gis\" >> /etc/profile.d/intro-gis.sh

SHELL [\"/bin/bash\", \"-lc\"]

ENV PATH=\"/opt/conda/envs/intro-gis/bin:${PATH}\"
ENV CONDA_DEFAULT_ENV=intro-gis
