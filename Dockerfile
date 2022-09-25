# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD . /uap
WORKDIR /uap

RUN chmod +x /uap/fuzz_parsers.py

CMD ["/uap/fuzz_parsers.py"]
