# docker build -t bge-m3:v1 . --platform linux/amd64 -f BGE.Dockerfile

# FROM  pytorch/pytorch:2.0.1-cuda11.7-cudnn8-devel
FROM cnstark/pytorch:2.3.1-py3.10.15-cuda12.1.0-ubuntu22.04

USER root

ENV ROOT=/bge

# ENV BGE_BUILTIN=/built-in

ENV PYTHONPATH=${ROOT}:$PYTHONPATH


COPY ./app ${ROOT}/app


ENV DEBIAN_FRONTEND=noninteractive
ENV PORT=8000

LABEL MAINTAINER="hanxie"

RUN mkdir -p ${ROOT}

WORKDIR ${ROOT}

# RUN rm /etc/apt/sources.list.d/cuda.list \
#     && apt-get update -y && apt-get install -y tzdata && apt-get install python3 python3-pip curl -y
RUN apt-get update -y && apt-get install -y tzdata && apt-get install python3 python3-pip curl -y

RUN ln -fs /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
  dpkg-reconfigure -f noninteractive tzdata

ENV NVIDIA_DRIVER_CAPABILITIES compute,graphics,utility

# RUN apt-get update && \
#     apt-get install -y nvidia-container-toolkit-base && apt-get install libgl1-mesa-glx -y  && \
#     apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 libvulkan1 libvulkan-dev vulkan-tools git && apt-get clean
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python3 get-pip.py 

# RUN git clone https://github.com/timdettmers/bitsandbytes.git --depth 1 -b main
# RUN cd bitsandbytes && CUDA_VERSION=117 make cuda11x && python3 setup.py install


RUN pip3 install -r app/embedding/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn --timeout 600 && rm -rf `pip3 cache dir`

# RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip3 install llama-cpp-python


EXPOSE ${PORT}

CMD ["python3", "app/embedding/app/main.py" ]