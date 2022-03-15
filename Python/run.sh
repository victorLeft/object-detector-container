#! /bin/bash
#curl https://infocar.dgt.es/etraffic/data/camaras/673.jpg > ~/podman/Python/data/input/test.jpg
podman run --replace --name detector -v ~/podman/object-detector-container/Python/data/:/usr/src/app/:Z objectdetection:latest
echo ">>Finished<<"
