FROM python:3

WORKDIR /usr/src/app

# RUN python -m pip install --upgrade pip pip-tools setuptools
# RUN pip-sync requirements/*.txt
# RUN python -m pip install -e .
RUN wget https://developer.salesforce.com/media/salesforce-cli/sfdx/channels/stable/sfdx-linux-x64.tar.xz
RUN mkdir ~/sfdx
RUN tar xJf sfdx-linux-x64.tar.xz -C ~/sfdx --strip-components 1
RUN export PATH=~/sfdx/bin:$PATH
RUN PATH=~/sfdx/bin:$PATH
ADD . .
RUN make dev-install

CMD [ "executable" ]