# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

## Setup.py requires git to install
RUN apt-get update && \
        DEBIAN_FRONTEND=noninteractive apt-get install -y git

ADD . /uap
WORKDIR /uap

# Build
RUN python3 setup.py install

RUN chmod +x mayhem/fuzz_parsers.py

CMD ["/uap/mayhem/fuzz_parsers.py"]
