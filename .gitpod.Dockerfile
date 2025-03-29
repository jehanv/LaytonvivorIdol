FROM gitpod/workspace-mysql

USER root

USER gitpod

RUN pyenv update  && \
    pyenv install 3.10.1  && \
    pyenv global 3.10.1