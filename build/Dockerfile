FROM archlinux:latest

# Install necessary packages
RUN pacman -Syyu --noconfirm \
    && pacman -S --noconfirm rustup \
    && rustup install stable \
    && rustup default stable \
    && pacman -S --noconfirm \
    git \
    make \
    gcc \
    cmake \
    clang \
    llvm \
    vim \
    git \
    python3 \
    python-pip    
# Clone Git repository
RUN git clone https://github.com/Jeremy-Gstein/supreme-redis-cs213Project /opt/repository

WORKDIR /opt/repository

# Run Startup Script
RUN tar xvf SCD-1937.txt.tar 

WORKDIR /opt/repository/rusty-redis

# Install Python packages
RUN pip3 install redis


# Install rust packages
RUN cargo update && \
    cargo build 

RUN cargo run ../SCD-1937.txt


# Set working directory
WORKDIR /opt/repository

# Start application
CMD ["python3", "sort-db-words.py"]
