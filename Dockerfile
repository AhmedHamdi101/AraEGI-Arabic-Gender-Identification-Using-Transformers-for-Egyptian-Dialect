From python:3.9
# Install Python dependencies
RUN apt-get update && \
    apt-get install -y \
    # Add any additional dependencies here \
    vim g++\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /reqs
COPY requirement.txt /reqs

#Run pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
#RUN pip install -r requirement.txt
RUN pip install torch==1.11+cu115 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirement.txt
RUN apt-get update && \
    apt-get install -y \
    # Add any additional dependencies here \
    vim g++ ffmpeg libsm6 libxext6 git build-essential openssh-server tmux htop \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN apt update && apt install default-jre
RUN pip install comet_ml arabert
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config # buildkit
RUN sed -i '/#force_color_prompt=yes/s/^#//g' ~/.bashrc # buildkit
RUN echo 'root:root' | chpasswd # buildkit
RUN service ssh restart # buildkit
EXPOSE 7860
